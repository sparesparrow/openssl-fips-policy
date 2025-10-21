#!/bin/bash
# Basic FIPS validation test - demonstrates core functionality

set -euo pipefail

echo "🔐 OpenSSL FIPS 140-3 Basic Validation Test"
echo "=========================================="

# Check if OpenSSL is available
if ! command -v openssl >/dev/null 2>&1; then
    echo "❌ OpenSSL not found - install OpenSSL to run FIPS validation"
    exit 1
fi

echo "✅ OpenSSL found: $(openssl version)"

# Create test data
echo "test data for FIPS validation" > testfile.txt

# Test basic OpenSSL functionality
if openssl sha256 -in testfile.txt >/dev/null 2>&1; then
    echo "✅ Basic SHA-256 hashing works"
else
    echo "❌ Basic SHA-256 hashing failed"
    exit 1
fi

# Test that MD5 is available (will be restricted in FIPS mode)
if openssl md5 -in testfile.txt >/dev/null 2>&1; then
    echo "✅ MD5 available (will be restricted in FIPS mode)"
else
    echo "⚠️  MD5 not available - system may already be in FIPS mode"
fi

# Check for FIPS module in common locations
FIPS_LOCATIONS=(
    "/usr/lib/x86_64-linux-gnu/ossl-modules/fips.so"
    "/usr/lib64/ossl-modules/fips.so"
    "/usr/local/lib/ossl-modules/fips.so"
)

FIPS_FOUND=false
for location in "${FIPS_LOCATIONS[@]}"; do
    if [ -f "$location" ]; then
        echo "✅ FIPS module found at: $location"
        FIPS_MODULE="$location"
        FIPS_FOUND=true
        break
    fi
done

if [ "$FIPS_FOUND" = false ]; then
    echo "⚠️  FIPS module not found in standard locations"
    echo "   (This is expected if FIPS-enabled OpenSSL hasn't been built yet)"
fi

# Test deprecated API compilation (basic check)
cat > test_deprecated_basic.c << 'EOF'
#include <openssl/evp.h>

int main() {
    // This should work (not deprecated)
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx) EVP_MD_CTX_free(ctx);
    return 0;
}
EOF

if gcc test_deprecated_basic.c -lcrypto -o test_deprecated_basic 2>/dev/null; then
    echo "✅ Basic OpenSSL compilation works"
    rm -f test_deprecated_basic
else
    echo "❌ Basic OpenSSL compilation failed"
    exit 1
fi

# Cleanup
rm -f testfile.txt test_deprecated_basic.c

echo ""
echo "🎉 Basic FIPS validation test completed!"
echo ""
echo "To run full FIPS validation:"
echo "  ./scripts/fips-validation/fips-compliance-validation.sh"
echo ""
echo "Or trigger automated validation via GitHub Actions."
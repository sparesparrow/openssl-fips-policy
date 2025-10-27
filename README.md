# ARCHIVED: openssl-fips-policy

**This repository has been merged into [openssl-conan-base/fips/](https://github.com/sparesparrow/openssl-conan-base/tree/main/fips).**

All FIPS 140-3 data is now maintained in the unified foundation package.

## Migration

FIPS certificate #4985 metadata is now automatically included in openssl-conan-base.

```python
# Old
python_requires = "openssl-fips-policy/140-3.2"

# New (use this)
python_requires = "openssl-conan-base/1.1.0"
```

## What Was Merged

- **fips-140-3/certificates/** → openssl-conan-base/fips/certificates/
- **scripts/fips-validation/** → openssl-conan-base/scripts/fips-validation/
- **FIPS compliance tools** → openssl-conan-base/scripts/

## FIPS 140-3 Support

The unified foundation package provides:

- Certificate #4985 metadata
- Test vectors and constraints
- Validation scripts
- Compliance testing tools
- SBOM generation with FIPS metadata

## Benefits of Consolidation

- Single source of truth for FIPS data
- Integrated with profiles and utilities
- Simplified dependency management
- Unified security scanning

See [openssl-conan-base](https://github.com/sparesparrow/openssl-conan-base) for current usage and FIPS integration.

---

**Archived on**: October 27, 2024
**Merged into**: openssl-conan-base v1.1.0
**Tag**: `archived/merged-into-conan-base-v1.1.0`

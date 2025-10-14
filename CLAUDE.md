# OpenSSL FIPS Policy - AI Context

Role: FIPS 140-3 compliance data for government deployments.

Certificate: #4985 (Level 1) with validated algorithms and platforms.

Usage:
- Consumed by `openssl-build-tools` when `deployment_target=fips-government`.
- Exposes `FIPS_DATA_ROOT` for consumers.

Architecture:
```mermaid
graph LR
  CERT[Certificate #4985] --> DATA[openssl-fips-data/140-3.1]
  SCHEMAS[Schemas] --> DATA
  TESTV[Vectors] --> DATA
  DATA --> TOOLS[openssl-build-tools/1.2.0]
```

# OpenSSL FIPS Policy

FIPS 140-3 policy definitions and compliance artifacts.

## Usage

```bash
conan remote add ${CONAN_REPOSITORY_NAME} ${CONAN_REPOSITORY_URL} --force
conan install --requires=openssl-fips-data/140-3.1 -r=${CONAN_REPOSITORY_NAME}
```

## Architecture

Schemas
------
This repository reserves `fips-140-3/schemas/` for future JSON schema validation of certificate and vector formats.

```mermaid
graph LR
  A[Certificate 4985] --> D[FIPS Data Package]
  B[Test Vectors] --> D
  C[Schemas] --> D
  D --> E[OpenSSL Build Tools]
```

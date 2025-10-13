# OpenSSL FIPS Policy

FIPS 140-3 policy definitions and compliance artifacts.

## Usage

```bash
conan remote add sparesparrow-conan https://conan.cloudsmith.io/sparesparrow-conan/openssl-conan/ --force
conan install --requires=openssl-fips-data/140-3.1 -r=sparesparrow-conan
```

## Architecture

```mermaid
graph LR
  A[Certificate 4985] --> D[FIPS Data Package]
  B[Test Vectors] --> D
  C[Schemas] --> D
  D --> E[OpenSSL Build Tools]
```

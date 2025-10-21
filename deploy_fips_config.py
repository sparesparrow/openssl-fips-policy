#!/usr/bin/env python3
import os
import json
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Deploy FIPS config into full_deploy bundle")
    parser.add_argument("--deploy-dir", default="full_deploy", help="Path to full_deploy root")
    parser.add_argument("--config", default="fipsmodule.cnf", help="Path to FIPS config file")
    args = parser.parse_args()

    deploy_dir = Path(args.deploy_dir)
    cfg_dest = deploy_dir / "res" / "fipsmodule.cnf"
    cfg_dest.parent.mkdir(parents=True, exist_ok=True)

    src = Path(args.config)
    cfg_dest.write_bytes(src.read_bytes())

    manifest = {
        "OPENSSL_FIPS": "1",
        "OPENSSL_CONF": str(cfg_dest.resolve()),
    }
    (deploy_dir / "env.json").write_text(json.dumps(manifest, indent=2))
    print("FIPS config deployed and env.json generated")


if __name__ == "__main__":
    main()

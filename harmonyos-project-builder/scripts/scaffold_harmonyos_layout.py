#!/usr/bin/env python3
"""Create a baseline HarmonyOS module directory layout.

This script is intentionally conservative: it creates directories only.
It does not overwrite config files or generate feature code.
"""

from __future__ import annotations

import argparse
from pathlib import Path


BASE_DIRS = [
    "src/main/ets/pages",
    "src/main/ets/view",
    "src/main/ets/viewmodel",
    "src/main/ets/service",
    "src/main/ets/model",
    "src/main/ets/common",
    "src/main/resources/base/profile",
    "src/main/resources/base/element",
    "src/main/resources/base/media",
]

OPTIONAL_DIRS = {
    "vpn": "src/main/ets/vpn",
    "extension": "src/main/ets/extension",
    "bridge": "src/main/ets/bridge",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a baseline HarmonyOS module layout."
    )
    parser.add_argument(
        "module_root",
        help="Path to a HarmonyOS module root, for example entry/",
    )
    parser.add_argument("--include-vpn", action="store_true", help="Create vpn/ directory")
    parser.add_argument(
        "--include-extension", action="store_true", help="Create extension/ directory"
    )
    parser.add_argument("--include-bridge", action="store_true", help="Create bridge/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    return parser.parse_args()


def collect_dirs(args: argparse.Namespace) -> list[str]:
    dirs = list(BASE_DIRS)
    if args.include_vpn:
        dirs.append(OPTIONAL_DIRS["vpn"])
    if args.include_extension:
        dirs.append(OPTIONAL_DIRS["extension"])
    if args.include_bridge:
        dirs.append(OPTIONAL_DIRS["bridge"])
    return dirs


def main() -> int:
    args = parse_args()
    module_root = Path(args.module_root).resolve()
    dirs = collect_dirs(args)

    print(f"Module root: {module_root}")
    for relative_dir in dirs:
        full_path = module_root / relative_dir
        action = "Would create" if args.dry_run else "Creating"
        print(f"{action}: {full_path}")
        if not args.dry_run:
            full_path.mkdir(parents=True, exist_ok=True)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

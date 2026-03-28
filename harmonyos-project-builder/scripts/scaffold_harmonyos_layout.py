#!/usr/bin/env python3
"""Create a baseline HarmonyOS module directory layout.

The default layout matches the official Stage-model project skeleton.
Additional engineering layers can be opted into explicitly when the
project scope and official sample patterns justify them.
"""

from __future__ import annotations

import argparse
from pathlib import Path


BASE_DIRS = [
    "src/main/ets/entryability",
    "src/main/ets/pages",
    "src/main/resources/base/profile",
    "src/main/resources/base/element",
    "src/main/resources/base/media",
]

OPTIONAL_DIRS = {
    "view": "src/main/ets/view",
    "views": "src/main/ets/views",
    "viewmodel": "src/main/ets/viewmodel",
    "model": "src/main/ets/model",
    "service": "src/main/ets/service",
    "common": "src/main/ets/common",
    "vpn": "src/main/ets/vpn",
    "extension": "src/main/ets/extension",
    "bridge": "src/main/ets/bridge",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a HarmonyOS module layout. By default this creates the official "
            "Stage-model skeleton; optional engineering layers can be added with flags."
        )
    )
    parser.add_argument(
        "module_root",
        help="Path to a HarmonyOS module root, for example entry/",
    )
    parser.add_argument("--include-view", action="store_true", help="Create view/ directory")
    parser.add_argument("--include-views", action="store_true", help="Create views/ directory")
    parser.add_argument(
        "--include-viewmodel", action="store_true", help="Create viewmodel/ directory"
    )
    parser.add_argument("--include-model", action="store_true", help="Create model/ directory")
    parser.add_argument(
        "--include-service", action="store_true", help="Create service/ directory"
    )
    parser.add_argument("--include-common", action="store_true", help="Create common/ directory")
    parser.add_argument(
        "--include-extension", action="store_true", help="Create extension/ directory"
    )
    parser.add_argument("--include-bridge", action="store_true", help="Create bridge/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    return parser.parse_args()


def collect_dirs(args: argparse.Namespace) -> list[str]:
    dirs = list(BASE_DIRS)
    if args.include_view:
        dirs.append(OPTIONAL_DIRS["view"])
    if args.include_views:
        dirs.append(OPTIONAL_DIRS["views"])
    if args.include_viewmodel:
        dirs.append(OPTIONAL_DIRS["viewmodel"])
    if args.include_model:
        dirs.append(OPTIONAL_DIRS["model"])
    if args.include_service:
        dirs.append(OPTIONAL_DIRS["service"])
    if args.include_common:
        dirs.append(OPTIONAL_DIRS["common"])
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

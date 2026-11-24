#!/usr/bin/env python3
"""Organize files in a directory into subfolders by type."""
import argparse
import shutil
import sys
from pathlib import Path

CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "documents": {".pdf", ".docx", ".txt", ".md", ".odt"},
    "archives": {".zip", ".tar", ".gz", ".tgz", ".7z"},
    "video": {".mp4", ".mkv", ".mov"},
    "audio": {".mp3", ".wav", ".flac"},
}


def category_for(path: Path) -> str:
    ext = path.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return "other"


def unique_destination(dest: Path) -> Path:
    """Return dest, or dest_1, dest_2... if it already exists."""
    if not dest.exists():
        return dest
    counter = 1
    while True:
        candidate = dest.with_name(f"{dest.stem}_{counter}{dest.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(source: Path, dry_run: bool) -> int:
    moved = 0
    for item in sorted(source.iterdir()):
        if not item.is_file() or item.is_symlink() or item.name.startswith("."):
            continue
        dest_dir = source / category_for(item)
        dest = unique_destination(dest_dir / item.name)
        label = "would move" if dry_run else "moved"
        print(f"{label}: {item.name} -> {dest.relative_to(source)}")
        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(item, dest)
        moved += 1
    return moved


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="directory to organize")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="show what would happen without changing anything")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        print(f"error: {source} is not a directory", file=sys.stderr)
        return 1
    count = organize(source, args.dry_run)
    print(f"{count} file(s) {'would be ' if args.dry_run else ''}processed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
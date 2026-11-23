#!/usr/bin/env python3
"""
Count lines, words and characters in a file.
"""

import argparse
import sys
from pathlib import Path


def parse_args(argv: None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Count lines, words and characters in a file."
    )
    parser.add_argument(
        "files", nargs="+", type=Path, help="Path to the file to be counted."
    )
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines.")
    parser.add_argument("-w", "--words", action="store_true", help="Count words.")
    parser.add_argument("-c", "--chars", action="store_true", help="Count characters.")
    return parser.parse_args()


def count_lines(file_path: Path) -> int:
    """Count the number of lines in a file."""
    with file_path.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_words(file_path: Path) -> int:
    """Count the number of words in a file."""
    with file_path.open("r", encoding="utf-8") as f:
        return sum(len(line.split()) for line in f)


def count_characters(file_path: Path) -> int:
    """Count the number of characters in a file."""
    with file_path.open("r", encoding="utf-8") as f:
        return sum(len(line) for line in f)


def main(argv=None) -> int:
    args = parse_args(argv)
    failed = False

    for file_path in args.files:
        if not file_path.exists():
            print(f"Error: {file_path} does not exist.", file=sys.stderr)
            failed = True
            continue
        if not file_path.is_file():
            print(f"Error: {file_path} is not a file.", file=sys.stderr)
            failed = True
            continue

        if args.lines:
            print(f"{file_path}: {count_lines(file_path)} lines")
        if args.words:
            print(f"{file_path}: {count_words(file_path)} words")
        if args.chars:
            print(f"{file_path}: {count_characters(file_path)} characters")

    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)

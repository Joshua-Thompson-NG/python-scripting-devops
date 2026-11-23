#!/usr/bin/env python3
"""
Greet someone by name.
Example usage: ./greet.py John -c 3 -v --shout --lang es
"""

import argparse
import sys

GREETINGS = {"en": "Hello", "es": "Hola", "fr": "Bonjour"}


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Greet someone by name")
    parser.add_argument("names", nargs="*", help="Name of the person to greet")
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of times to greet"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    parser.add_argument(
        "--shout", action="store_true", help="Shout the greeting in uppercase"
    )
    parser.add_argument(
        "--lang", choices=GREETINGS, default="en", help="Use language-specific greeting"
    )
    args = parser.parse_args(argv)

    if args.count < 1:
        parser.error("Count must be a positive integer")
    if not args.names and not sys.stdin.isatty():  # For piped input
        args.names = [line.strip() for line in sys.stdin if line.strip()]
    if not args.names:
        parser.error("no names provided (pass them as arguments or on stdin)")
    return args


def main(argv=None) -> int:
    args = parse_args(argv)
    if any(not name.strip() for name in args.names):
        print("error: names must not be empty", file=sys.stderr)
        return 1

    for name in args.names:
        greeting = f"{GREETINGS[args.lang]}, {name}"
        if args.shout:
            greeting = greeting.upper()
        for _ in range(args.count):
            print(greeting)
        if args.verbose:
            plural = "s" if args.count > 1 else ""
            print(
                f"Greeted {name} {args.count} time{plural} in {args.lang} language.",
                file=sys.stderr,
            )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(130)

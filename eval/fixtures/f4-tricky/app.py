"""CLI entry point. The KeyError traceback ends here, but the bug is in parser.py."""

import parser


def main():
    data = parser.parse("name=alice;age=30")
    print("parsed:", data)
    print("greeting: Hello,", data["name"].upper())


if __name__ == "__main__":
    main()

import argparse

from .scanner import Scanner


def main():
    parser = argparse.ArgumentParser(description="OpenGuard security scanner")
    parser.add_argument("command", choices=["scan"])
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    args = parser.parse_args()

    if args.command == "scan":
        report = Scanner().run()
        print(report)


if __name__ == "__main__":
    main()

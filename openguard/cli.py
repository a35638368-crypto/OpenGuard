import argparse
from .scanner import Scanner


def main():
    parser = argparse.ArgumentParser(description="OpenGuard security scanner")
    parser.add_argument("command", choices=["scan"])
    args = parser.parse_args()

    if args.command == "scan":
        report = Scanner().run()
        print(report)


if __name__ == "__main__":
    main()

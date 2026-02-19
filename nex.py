import sys
from commands.run import run_file


def show_help():
    print("""
NEX - Universal Developer Tool

Commands:
  python nex.py run <file>     Run a file
  python nex.py --version      Show version
  python nex.py --help         Show help
""")


def show_version():
    try:
        with open("version.txt", "r") as f:
            print("NEX version:", f.read().strip())
    except FileNotFoundError:
        print("Version file missing.")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "run":
        if len(sys.argv) < 3:
            print("Error: No file provided.")
            return
        run_file(sys.argv[2])

    elif command == "--version":
        show_version()

    elif command == "--help":
        show_help()

    else:
        print("Unknown command.")
        show_help()


if __name__ == "__main__":
    main()

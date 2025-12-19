import sys
from telly.engine import run_launcher

def main():
    if len(sys.argv) < 2:
        print("Usage: telly <launcher>")
        sys.exit(1)
    launcher_name = sys.argv[1]
    run_launcher(launcher_name)

if __name__ == "__main__":
    main()

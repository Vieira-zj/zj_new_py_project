import sys

from browser_sandbox import hello_world_help, help


def main():
    help()
    hello_world_help()
    print("python version:", sys.version)


if __name__ == "__main__":
    main()

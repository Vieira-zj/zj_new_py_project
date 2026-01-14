import sys

from browser_sandbox import hello_world_help, help


def main():
    print("python version:", sys.version)

    help()
    hello_world_help()


if __name__ == "__main__":
    main()

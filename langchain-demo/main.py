import sys

from browser_sandbox import hello_world_help, pkg_help


def main():
    print("python version:", sys.version)

    pkg_help()
    hello_world_help()


if __name__ == "__main__":
    main()

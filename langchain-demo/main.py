import sys

from dotenv import load_dotenv

from sandbox import pkg_help, playwright_sandbox_help

load_dotenv()


def main():
    print("python version:", sys.version)

    pkg_help()
    playwright_sandbox_help()


if __name__ == "__main__":
    main()

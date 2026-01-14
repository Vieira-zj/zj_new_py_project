import os

from dotenv import load_dotenv

from browser_sandbox.hello_world import hello_world_help

load_dotenv()


def pkg_help():
    print("PYTHONPATH:", os.getenv("PYTHONPATH"))
    print("This is a langchain browser sandbox package.")

import os

from dotenv import load_dotenv

from browser_sandbox.hello_world import hello_world_help

load_dotenv()


def help():
    print("PYTHONPATH:", os.getenv("PYTHONPATH"))
    print("This is the langchain browser sandbox package.")

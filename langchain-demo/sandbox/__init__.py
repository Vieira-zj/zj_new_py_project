import os

from sandbox.play_wright.hello_world import playwright_sandbox_help


def pkg_help():
    print("python path:", os.getenv("PYTHONPATH"))
    print("this is a langchain browser sandbox package.")

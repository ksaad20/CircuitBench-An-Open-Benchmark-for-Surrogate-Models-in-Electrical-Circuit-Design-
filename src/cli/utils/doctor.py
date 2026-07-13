"""Environment diagnostics."""

import platform
import sys


def execute(args):
    print("Circuit-Bench Doctor")
    print("--------------------")
    print(f"Python : {platform.python_version()}")
    print(f"Platform : {platform.system()}")
    print(f"Executable : {sys.executable}")

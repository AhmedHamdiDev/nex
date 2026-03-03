import os
from handlers.c_handler import run_c
from handlers.java_handler import run_java
from handlers.python_handler import run_python
from utils.timer import measure_time


def find_main_file(folder):
    """Search for a main file in a folder."""

    possible_files = ["main.py", "Main.java", "main.c"]

    for file in possible_files:
        path = os.path.join(folder, file)
        if os.path.exists(path):
            return path

    return None
def find_python_file(folder):
    """Find first Python file in folder."""
    for file in os.listdir(folder):
        if file.endswith(".py"):
            return os.path.join(folder, file)
    return None
def read_config(folder):
    """Read nex.config and return entry file if exists."""
    config_path = os.path.join(folder, "nex.config")

    if not os.path.exists(config_path):
        return None

    with open(config_path, "r") as f:
        for line in f:
            if line.startswith("entry="):
                return os.path.join(folder, line.strip().split("=")[1])

    return None


def run_file(target):

    # If user runs current folder: nex run .
    if target == ".":

        # 1️⃣ Check config first
        config_entry = read_config(os.getcwd())

        if config_entry and os.path.exists(config_entry):
            print("Using config entry:", config_entry)
            target = config_entry

        else:
            # 2️⃣ Try main file detection
            main_file = find_main_file(os.getcwd())

            if not main_file:
                # 3️⃣ Try any Python file
                python_file = find_python_file(os.getcwd())

                if python_file:
                    print("Python project detected:", python_file)
                    target = python_file
                else:
                    print("No runnable project found.")
                    return
            else:
                print("Project detected:", main_file)
                target = main_file

    if not os.path.exists(target):
        print("Error: File not found.")
        return

    try:
        if target.endswith(".c"):
            measure_time(run_c, target)

        elif target.endswith(".java"):
            measure_time(run_java, target)

        elif target.endswith(".py"):
            measure_time(run_python, target)

        else:
            print("Unsupported file type.")

    except Exception as e:
        print("Execution failed:", e)

import subprocess
import os

def run_java(file_name):
    print("Compiling Java file...")

    compile_result = subprocess.run(["javac", file_name])

    if compile_result.returncode != 0:
        print("Compilation failed.")
        return

    class_name = os.path.splitext(os.path.basename(file_name))[0]

    print("Running Java program...")
    subprocess.run(["java", class_name])

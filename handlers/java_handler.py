import subprocess
import os

def run_java(file_name):
    print("Compiling Java file...")

    class_name = os.path.splitext(os.path.basename(file_name))[0]
    class_file = class_name + ".class"

    # Only compile if .class does not exist or .java is newer
    if not os.path.exists(class_file) or os.path.getmtime(file_name) > os.path.getmtime(class_file):
        compile_result = subprocess.run(
            ["javac", file_name],
            capture_output=True,
            text=True
        )
        if compile_result.returncode != 0:
            print("Compilation failed:\n", compile_result.stderr)
            return
    else:
        print("Skipping compilation (up-to-date)")

    print("Running Java program...")
    subprocess.run(["java", class_name])
import subprocess

def run_python(file_name):
    print("Running Python file...")
    subprocess.run(["python", file_name])

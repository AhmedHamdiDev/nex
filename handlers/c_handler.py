import subprocess
import os

def run_c(file_name):
    print("Compiling C file...")

    output_file = "program"

    compile_result = subprocess.run(
        ["gcc", file_name, "-o", output_file]
    )

    if compile_result.returncode != 0:
        print("Compilation failed.")
        return

    print("Running C program...")
    subprocess.run([f"./{output_file}"])

    # optional cleanup
    if os.path.exists(output_file):
        os.remove(output_file)

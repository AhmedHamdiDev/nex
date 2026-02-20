import subprocess
import os

def run_c(file_name):
    print("Compiling C file...")

    output_file = "program"
    exe_file = output_file + (".exe" if os.name == "nt" else "")

    # Only compile if .exe does not exist or .c is newer
    if not os.path.exists(exe_file) or os.path.getmtime(file_name) > os.path.getmtime(exe_file):
        compile_result = subprocess.run(
            ["gcc", file_name, "-o", exe_file],
            capture_output=True,
            text=True
        )

        if compile_result.returncode != 0:
            print("Compilation failed:\n", compile_result.stderr)
            return
    else:
        print("Skipping compilation (up-to-date)")

    print("Running C program...")
    subprocess.run([exe_file])
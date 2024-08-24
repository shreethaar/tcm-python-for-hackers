import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the command:")
        print("Error code:", e.returncode)
        print("Error message:\n", e.stderr)

if __name__ == "__main__":
    command = "ls -l"
    run_command(command)


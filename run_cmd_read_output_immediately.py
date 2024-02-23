import subprocess

# Command to execute
cmd = ["your_command_here"]

# Open the subprocess with bufsize=1 for line-buffered output
process = subprocess.Popen(cmd, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

# Read and print the output line by line
for line in process.stdout:
    print(line, end='', flush=True)  # Flush the output immediately

# Wait for the process to complete
process.wait()

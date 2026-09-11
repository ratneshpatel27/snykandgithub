import subprocess

# VULNERABLE CODE
filename = input("Enter filename: ")
subprocess.run(f"cat {filename}", shell=True)  # Input like 'file.txt; rm -rf /' is dangerous

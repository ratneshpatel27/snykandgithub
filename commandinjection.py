import subprocess
# VULNERABLE
filename = input("Enter filename: ")
subprocess.run(f"cat {filename}", shell=True)

import subprocess

from psutil import process_iter

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result)
print(result.returncode)
print(result.stdout.decode().split())
process = subprocess.run(['rm', 'no_catalog'], capture_output=True)
print(process.returncode)
print(result.stdout)
print(result.stderr)

# access = subprocess.run(['chmod', '+x', 'ex_04_1.py'])
# code = subprocess.run(['./ex_04_1.py', 'my_new_file.txt'])

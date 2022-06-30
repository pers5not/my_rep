import subprocess

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result)
print(result.returncode)
print(result.stdout.decode().split())
result = subprocess.run(['rm', 'no_catalog'], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)

# access = subprocess.run(['chmod', '+x', 'ex_04_1.py'])
# code = subprocess.run(['./ex_04_1.py', 'my_new_file.txt'])

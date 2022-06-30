import subprocess

subprocess.run(['sleep', '1'])
print(subprocess.run(['date']))
result = subprocess.run(["ls", '../../../'])
print(result.returncode)
result = subprocess.run(["sudo", "chmod", '777', 'ex_04_6.py'])
print(result.returncode)
result = subprocess.run(["ls", "-l"])
print(result.returncode)

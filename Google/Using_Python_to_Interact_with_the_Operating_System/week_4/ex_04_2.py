import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.getenv("VAR", ""))
# Создавать переменные окружения необходимо в ~/.bashrc

import re

print(re.split(
    r"[.,!?]", "Hello, I'm learning Python. Why? Very interesting regular expressions! You ask, and rightly so."))
print(re.split(
    r"([.,!?])", "Hello, I'm learning Python. Why? Very interesting regular expressions! You ask, and rightly so."))

print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]',
      "Recived an e-mail for go_nuts95@my.example.com"))


# ICT 09 – Programming 1

# FINAL PROJECT

# 8. Password generator:
# - Generate password from random alphanumeric string.

import random
import string

def password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

generated_password = password_generator()
print("Generated password:", generated_password)

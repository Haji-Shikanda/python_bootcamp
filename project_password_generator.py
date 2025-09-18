#PROJECT PASSWORD GENERATOR
# 1. Never share your password
# 2. Use a strong password
# 3. Do not reuse your password
# 4. Use 2FA

import random
import string
print("PASSWORD GENERATOR")
print(""" Please Keep This in Mind:
1. Never share your password
2. Use a strong password
3. Do not reuse your password
4. Use 2FA 
""")
chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Password length: "))
password = ''
for _ in range(length):
    c = random.choice(chars)
    password = password + c

print(f"Your random password is: {password}")

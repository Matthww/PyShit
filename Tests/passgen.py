import random

letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
password = ""

for i in range(8):
    next_index = random.randrange(len(letters))
    password += letters[next_index]

print(password)

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

while 1:
    password_len = int(input("How many characters do you need the password to have?\n"))
    password_amount = int(input("How many passwords do you need?\n"))
    for x in range(0,password_amount):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Passwords provided:", password)

import random


def generate_password(pass_len):
    characters = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ0123456789!@#$%&?"
    password = ""
    for i in range(0, pass_len):
        password = password + str(random.choice(characters))
    return password


print(generate_password(8))


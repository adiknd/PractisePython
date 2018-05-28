def return_max(a, b, c):
    max = a
    if b>max:
        max = b
    elif c>max:
        max =c
    return max


print(return_max(56,133,22))

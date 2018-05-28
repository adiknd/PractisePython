def fibonacci(num):
    if num == 1:
        fib = [1]
        return fib
    if num == 2:
        fib = [1, 1]
        return fib
    else:
        fib = [1, 1]
        for i in range(2, num):
            fib.append(fib[i-2]+fib[i-1])
        return fib


number = int(input("How many fibonacci numbers would you like to generate?: "))
print(fibonacci(number))

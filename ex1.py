name = input("Enter your name: ")
age = input("Enter your age: ")

print("%s, you will turn 100 yo in %s." %(name, 2018 - int(age) + 100))

number_of_copies = int(input("How many copies ?: "))

for x in range(0, number_of_copies):
    print("%s, you will turn 100 yo in %s." % (name, 2018 - int(age) + 100))
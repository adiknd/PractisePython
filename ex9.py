import random

user_num = ""

while not user_num == "exit":
    num = random.randint(1, 9)
    num_of_guesses = 1
    user_num = input("Enter your number (1-9): ")

    while not user_num == "exit":

        if int(user_num) == num:
            print("You guessed, congratulations ! (%s guesses)" % num_of_guesses)
            break
        elif int(user_num) < num:
            user_num = input("Too low ... Try again: ")
            num_of_guesses += 1
        elif int(user_num) > num:
            user_num = input("Too high ... Try again: ")
            num_of_guesses += 1
        elif user_num == "exit":
            break

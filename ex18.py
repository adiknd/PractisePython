import random


def generate_number():
    random_number = random.sample(range(0, 9), 4)
    print(random_number)
    return random_number


def check_user_number(user_number):
    if user_number.isdigit() and len(user_number) == 4:
            return True
    else:
        print("Incorrect number! 4 digit number is required. Try again.\n")
        return False


def get_user_number():
    user_number = input("Enter a 4 digit number: ")
    while check_user_number(user_number) is not True:
        user_number = input("Enter a 4 digit number: ")
    user_number = [int(i) for i in str(user_number)]
    return user_number


def check_result(user_number, drawn_number):
    bulls = 0
    cows = 0
    if user_number == drawn_number:
        print("WINNER !")
        print("Number of guesses: %s" % number_of_guesses)
        return True
    else:
        for i in range(4):
            if user_number[i] == drawn_number[i]:
                cows += 1
            elif user_number[i] in drawn_number:
                bulls += 1

        print("%s cows, %s bulls\n" % (cows, bulls))


if __name__ == "__main__":
    _drawn_number = generate_number()
    number_of_guesses = 1
    while check_result(get_user_number(), _drawn_number) is not True:
        number_of_guesses += 1





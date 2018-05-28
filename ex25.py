# ---GUESS GAME---
# You have to choose and remember a number in range 0-100.
# Computer have to guess your number and you have to answer for every guess of computer.
# Available answers:
#   - "l" (lower) that means that the number provided by computer is too high
#   - "h" (higher) that means that the number provided by computer is too low.
#   - "w" (win) that means that computer guessed your number and the game is over.

computer_number = 50
temp_1 = 25
temp_2 = 25
running = True
number_of_guesses = 0
user_answer_copy = ""

while running:
    print(computer_number)
    user_answer = input("Your answer ([l]lower, [h]higher, [w]win): ")
    if user_answer == "w":
        running = False
    elif user_answer == "h":
        if user_answer_copy == "l":
            temp_1 = temp_2
        if temp_1 < 3:
            computer_number += 1
        else:
            computer_number = computer_number + temp_1
            temp_1 = temp_1 // 2
        user_answer_copy = user_answer
    elif user_answer == "l":
        if user_answer_copy == "h":
            temp_2 = temp_1
        if temp_2 < 3:
            computer_number -= 1
        else:
            computer_number = computer_number - temp_2
            temp_2 = temp_2 // 2
        user_answer_copy = user_answer
    number_of_guesses += 1

print("Congratulations, you guessed ! Number of guesses: {0}".format(number_of_guesses))

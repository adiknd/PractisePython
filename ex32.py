import random


print("Welcome to Hangman!")


def get_random_word():
    with open("sowpods.txt", 'r') as sowpods:
        list_of_sowpods = []
        for line in sowpods:
            list_of_sowpods.append(line)
    random_number = random.randint(0, len(list_of_sowpods))
    word = list_of_sowpods[random_number].strip()
    return word


def initialize_guessing_word(word):
    for i in range(0, len(word)):
        guessing_word.append("_")


def get_letter():
    guess = input(str("\nGuess your letter: ")).upper()
    if guess in user_guesses:
        print("The letter already guessed.")
        return False
    user_guesses.add(guess)
    return guess


def print_result():
    print()
    for j in guessing_word:
        print(j, end=' ')


def check_result(guess, word, guessing_word):
    global running
    global incorrect_guesses
    if guess is False:
        return
    if guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                guessing_word[i] = word[i]
    else:
        if incorrect_guesses > 5:
            print("Too much incorrect guesses !")
            running = False
        else:
            incorrect_guesses += 1
            print("Incorrect!")
    if guessing_word == word:
        print_result()
        running = False


if __name__ == '__main__':
    game_is_on = True
    while game_is_on:
        word = get_random_word()
        print(word)
        word = list(word)
        running = True
        guessing_word = []
        incorrect_guesses = 0
        user_guesses = set()

        initialize_guessing_word(word)

        while running:
            print_result()
            check_result(get_letter(), word, guessing_word)
            if running is False:
                break
            print("#You have %s incorrect guesses left" % (6-incorrect_guesses))
        play_again = input("Wanna play again ? (Y/N)").upper()
        if play_again == "N":
            break

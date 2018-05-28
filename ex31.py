print("Welcome to Hangman!")


def initialize_guessing_word():
    for i in range(0, len(word)):
        guessing_word.append("_")


def get_letter():
    guess = input(str("\nGuess your letter: ")).upper()
    return guess


def print_result():
    for j in guessing_word:
        print(j, end=' ')


def check_result(guess, word, guessing_word):
    if guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                guessing_word[i] = word[i]

    else:
        print("Incorrect!")

    if guessing_word == word:
        print_result()
        global running
        running = False


if __name__ == '__main__':

    word = "EVAPORATE"
    word = list(word)
    running = True
    guessing_word = []
    incorrect_guesses = 0

    initialize_guessing_word()

    while running:
        print_result()
        check_result(get_letter(), word, guessing_word)



import os

player1 = input("Name for player 1: ")
player2 = input("Name for player 2: ")
player1_output = ""
player2_output = ""
values = ["rock", "scissors", "paper", "exit"]
start_new_game = True


def is_correct(player_output):
    player_output = str(player_output).lower()
    if player_output in values:
        return True
    else:
        return False


def is_exit(player_output):
    player_output = str(player_output).lower()
    if player_output == "exit":
        print("Exiting...")
        return True
    else:
        return False


def who_wins(pl1, pl2):
    pl1 = str(pl1).lower()
    pl2 = str(pl2).lower()
    if pl1 == pl2:
        return 0
    elif pl1 == "scissors" and pl2 == "paper":
        return 1
    elif pl1 == "rock" and pl2 == "scissors":
        return 1
    elif pl1 == "paper" and pl2 == "rock":
        return 1
    else:
        return 2


def clear():
    os.system('clear')


while start_new_game:

    while not is_correct(player1_output):
        player1_output = input("{0}, what is your choice ? (paper/rock/scissors/exit): ".format(player1))

        if not is_correct(player1_output):
            print("Wrong value!")

    if is_exit(player1_output):
        break

    while not is_correct(player2_output):
        player2_output = input("{0}, what is your choice ? (paper/rock/scissors/exit): ".format(player2))

        if not is_correct(player2_output):
            print("Wrong value!")

    if is_exit(player2_output):
        break

    if who_wins(player1_output, player2_output) == 0:
        print("Draw!")

    elif who_wins(player1_output, player2_output) == 1:
        print("%s wins!" % player1)

    elif who_wins(player1_output, player2_output) == 2:
        print("%s wins!" % player2)

    play_again = input("Wanna play again ? (Y/N): ")
    if play_again == "Y" or play_again == "y":
        clear()
        player1_output = ""
        player2_output = ""
    else:
        start_new_game = False







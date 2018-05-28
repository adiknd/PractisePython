def draw_game_board(size):
    for h in range(size):
        for i in range(size):
            print(" ---", end="")
        print()
        for j in range(size+1):
            print("|   ", end="")
        print()
    for k in range(size):
        print(" ---", end="")


draw_game_board(3)
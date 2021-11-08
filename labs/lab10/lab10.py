"""
Maeve O'Toole

lab9.py

This program is my lab10 functions.

This assignment is entirely my own work.

"""

def build_board():
    tictactoe_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return tictactoe_list

def display_board(tictactoe_list):
    print("-" * 10)
    acc = 0
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tictactoe_list[acc], end="|")
            acc = acc + 1
        print()
    print("-" * 10)

def fill_a_spot(tictactoe_list, spot, marker):
    tictactoe_list[spot - 1] = marker

def legal_spot(tictactoe_list, spot):
    if ((tictactoe_list[spot] == "X" or tictactoe_list[spot] == "O") or (spot < 1 or spot > 9)):
        return False
    else:
        return True

def game_won(tictactoe_list):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot - 1] == "X":
                counter = counter + 1
            if counter == 3:
                return "X wins!"
    for condition in winCon:
        counter = 0
        for spot in condition:
            if tictactoe_list[spot - 1] == "Y":
                counter = counter + 1
            if counter == 3:
                return "Y wins!"

def game_over(tictactoe_list, turnCount):
    if ((game_won(tictactoe_list) == "X wins!" or game_won(tictactoe_list) == "Y wins!") or (turnCount > 9)):
        return True
    else:
        return False

def play():

    tictactoe_list = build_board()
    turnCount = 0

    display_board(tictactoe_list)

    while not game_over(tictactoe_list, turnCount):

        x_spot = eval(input("X where do you want to place your marker? "))

        if legal_spot(tictactoe_list, x_spot):
            fill_a_spot(tictactoe_list, x_spot, "X")
            turnCount = turnCount + 1

        display_board(tictactoe_list)

        if game_won(tictactoe_list) == ("X wins!"):
            print("X wins!")
            break
        if game_won(tictactoe_list) == ("Y wins!"):
            print("Y wins!")
            break
        if game_won(tictactoe_list) or turnCount > 9:
            print("Game is a draw!")

        y_spot = eval(input("Y where do you want to place your marker? "))

        if legal_spot(tictactoe_list, y_spot):
            fill_a_spot(tictactoe_list, y_spot, "O")
            turnCount = turnCount + 1

        display_board(tictactoe_list)

        if game_won(tictactoe_list) == ("X wins!"):
            print("X wins!")
            break
        if game_won(tictactoe_list) == ("Y wins!"):
            print("Y wins!")
            break
        if game_won(tictactoe_list) or turnCount > 9:
            print("Game is a draw!")

def main():

    play()

if __name__ == '__main__':
    main()

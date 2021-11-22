"""

Maeve O'Toole

lab12.py

This program will be the functions of lab12.

This assignment is entirely my own work.

"""
from random import randint


def find_and_remove_first(lst, value):

    try:
        i = lst.index(value)
        lst[i] = "Maeve"
    except:
        pass

def read_data(filename):

    f = open(filename, "r")
    data = f.read()
    data = data.split()
    return data

def is_in_linear(search_val, values):

    i = 0
    while i < len(values):
        if search_val in values:
            return True
        i = i + 1
    return False

def good_input():

    number = eval(input("Enter a number between 1 and 10: "))
    while not number >= 1 and not number <= 10:
        number = eval(input("Enter a number between 1 and 10: "))
    return number

def num_digits():

    number = eval(input("Enter a positive integer: "))
    while number >= 1:
        digits = 0
        while number != 0:
            number = number // 10
            digits = digits + 1
        print("There are", digits, "digits in the number")
        number = eval(input("Enter a positive integer: "))

def hi_lo_game():

    secret = randint(1, 100)
    guesses = 1
    number = eval(input("Guess a number: "))
    while secret != number and guesses < 7:
        guesses = guesses + 1
        if number > secret:
            print("Your guess was too high!")
        else:
            if number < secret:
                print("Your guess was too low!")
        number = eval(input("Guess a number: "))

    if number == secret:
        print("You win in", guesses, "guesses!")
    else:
        print("Sorry, you lose. The number was", secret)

def main():

    find_and_remove_first()
    read_data()
    is_in_linear(3, [4, 3, 6, 7])
    good_input()
    num_digits()
    hi_lo_game()

if __name__ == '__main__':
    main()

"""
Maeve O'Toole

lab11.py

These are my functions for lab 11.

This assignment is entirely my own work.

"""

from random import randint

def words(infile_name):
    infile = open(infile_name, "r")
    contents = infile.read()
    return contents.split("\m")

def random_word(list):
    return list[randint(0, len(list) - 1)]

def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)

def won(word, letters):
    x = fill(word, letters)
    if x == word:
        return True
    else:
        return False

def play():
    list_of_words = words("words.txt")
    secret_word = random_word(list_of_words)
    incorrect_guesses = 0
    guesses = []
    current = "_" * len(secret_word)
    while incorrect_guesses < 7 and not won(secret_word, guesses):

        display = fill(secret_word, guesses)
        print("Your word: ", display)
        print("Guesses: ", guesses)

        letter = input("Enter your letter guess: ")
        while letter in guesses:
            letter = input("Enter your letter guess: ")
        guesses.append(letter)

        display = fill(secret_word, guesses)
        if display == current:
            incorrect_guesses = incorrect_guesses + 1
        else:
            current = display

    if current == secret_word:
        print("You win")
    else:
        print("You lose")

def main():

    play()

main()

"""
Maeve O'Toole

lab6.py

This lab practices using Python strings, lists, indexing, and slicing facilities.

This assignment is entirely my own work.

"""


def name_reverse():
    first = input("Enter first name here: ")
    last = input("Enter last name here: ")
    print(str(last) + ', ' + str(first))

def company_name():
    name = input("Enter the website name here: ")
    company = name.split('.')[1]
    print(str(company))

def initials():
    names = eval(input("How many names will be in the input? "))

    for i in range(1, names + 1):
        first = input("Enter the first name of student " + str(i) + ": ")
        last = input("Enter " + str(first) + "'s last name: ")
        print(str(first) + "'s initials are " + first[0] + last[0] + '.')

def names():
    names = input("Enter people's names, separated by commas: ")
    names = names.split(", ")

    for name in names:
        name = name.split(" ")
        initials = name[0][0] + name[1][0]
        print(initials, end=" ")
    print()

def thirds():
    n = eval(input("Enter the number of sentences that will be inputed: "))

    for i in range(1, n + 1):
        sentence = input("Enter sentence " + str(i) + " here: ")
        print(sentence[2::3])

def word_average():
    sentence = input("Enter sentence here: ")
    sentence = sentence.split(" ")
    acc = 0

    for word in sentence:
        acc = acc + len(word)
    print(acc / len(sentence))

def pig_latin():
    sentence = input("Enter the sentence here: ")
    sentence = sentence.lower()
    sentence = sentence.split(" ")

    for word in sentence:
        word = word[1:]
        word = word + word[0] + "ay"
        print(word, end=" ")

def main():

    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

if __name__ == '__main__':
    main()
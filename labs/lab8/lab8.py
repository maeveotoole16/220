"""
Maeve O'Toole

lab8.py

This lab practices writing functions.

This assignment is entirely my own work.

"""

from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+') # + writes to a file that does not exist at first

    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + str(word) + '\n')
            i = i + 1

    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')

    for line in in_file:
        parts = line.split()

        wage = float(parts[2])
        wage = wage + 1.65
        wages = wage * int(parts[3])
        out_file.write(parts[0] + " " + parts[1] + " " + str(wages) + "\n")

    in_file.close()
    out_file.close()

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc = acc + int(isbn) * position
    return acc

def send_message(file, friend):

    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')

    for line in in_file:
        out_file.write(line)

    in_file.close()
    out_file.close()

def send_safe_message(file, friend, key):

    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')

    for line in in_file:
        out_file.write(encode(line, key))

    in_file.close()
    out_file.close()

def send_uncrackable_message(file, friend, pad):

    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w+')
    pad_file = open(pad, 'r')
    key = pad_file.read()

    for line in in_file:
        out_file.write(encode_better(line, key))

    in_file.close()
    out_file.close()

def main():

    number_words()
    hourly_wages()
    calc_check_sum()
    send_message()
    send_safe_message()
    send_uncrackable_message()

if __name__ == '__main__':
    main()

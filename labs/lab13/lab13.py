"""

Maeve O'Toole

lab13.py

This program will be the functions of lab13.

This assignment is entirely my work.

"""

def is_in_binary(search_val, values):

    midpoint = values[len(values) // 2]
    while midpoint != search_val and len(values) != 1:
        if search_val > midpoint:
            values = values[midpoint + 1:]
        else:
            values = values[:midpoint]
        midpoint = values[len(values) // 2]
    if len(values) == 1 and values[0] != search_val:
        return False
    else:
        return True

def selection_sort(values):

    for i in range(len(values)):
        lowest_val = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest_val:
                lowest_val = values[j]
                position = j
            values[i], values[position] = values[position], values[i]

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy

def rect_sort(rectangles):

    my_dict = {}
    areas = []

    for rect in rectangles:
        my_dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))

    selection_sort(areas)

    for i in range(len(areas)):
        rectangles[i] = my_dict[areas[i]]

def star_find(filename):

    # find 5 numbers that fall in the range 4,000 - 5,000 (inclusive)

    in_file = open(filename, "r")
    signals = in_file.read().split() # will return list of signals (list of strings)

    signals_found = []

    for i in range(len(signals)):
        if eval(signals[i]) >= 4000 and eval(signals[i]) <= 5000:
            signals_found.append(signals[i])
        else:
            if len(signals_found) >= 5:
                break

    print("Number of signals:", len(signals_found))
    print("The strength of each signal is:", signals_found)
    if len(signals_found) < 5:
        print("Could not find 5 signals within the acceptable range")
    else:
        print("The fifth signal was in position:", i)

def main():

    is_in_binary()
    selection_sort()
    star_find("signals.txt")

main()

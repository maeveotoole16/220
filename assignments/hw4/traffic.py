"""
Maeve O'Toole

traffic.py

This program is aimed to help practice accumulations and nested loops.
It specifically works to anaylze traffic patterns based on the users input.

This assignment is entirely my own work.

"""

def main():

    roads = eval(input(" How many roads were surveyed? "))
    acc1 = 0

    for i in range(1, roads + 1):
        days = eval(input(" How many days was road " + str(i) + " surveyed? "))
        acc = 0

        for vehicles in range(1, days + 1):
            cars = eval(input(" How many cars traveled on day " + str(vehicles) + " ? "))
            acc1 = acc1 + cars
            acc = acc + cars
        print(" Road " + str(i) + " average vehicles per day: " + str(round((acc/days), 2)))

    print(" Total number of vehicles traveled on all roads: ", acc1)
    print(" Average number of vehicles per road: ", round((acc1 / roads), 2))

if __name__ == '__main__':
    main()

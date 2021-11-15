"""
Name: <Maeve O'Toole>

Problem: This function calculates the area of a rectangle

"""

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)
calc_area()

"""if you wrap the input with eval, the eval will convert the input to code"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)
calc_volume()

def shooting_percentage():
    total_shots = eval(input("Enter the number of total shots: "))
    total_shots_made = eval(input("Enter the number of shots made: "))
    percentage = (total_shots_made / total_shots) * 100
    print("Percentage =", percentage, "%")
shooting_percentage()

def coffee():
    cost = 10.50
    shipping = 0.86
    fixed_cost = 1.50
    pounds = eval(input("Enter the number of pounds of coffee purchased: "))
    print("Coffee Order = ", "$", (cost * pounds) + (shipping * pounds) + fixed_cost )
coffee()

def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers traveled: "))
    total_miles = (kilometers/1.61)
    print("Total Miles =", total_miles)
kilometers_to_miles()
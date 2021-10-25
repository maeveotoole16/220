"""

Maeve O'Toole

weighted_average.py

This program will develop a Python program that uses numerical data from a test file.

This assignment is entirely my own work.

"""

def weighted_average(in_file_name, out_file_name):

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    class_average = 0
    content = in_file.readlines()
    num = 0

    for line in content:
        halves = line.strip().split(":")
        values = halves[1].strip().split()
        total_weight = 0
        total_grade = 0

        for i in range(0, len(values), 2):
            total_weight = total_weight + int(values[i])
        if total_weight < 100:
            out_file.write(halves[0] + "'s average:" + " Error: The weights are less than 100." + "\n")
            continue
        if total_weight > 100:
            out_file.write(halves[0] + "'s average:" + " Error: The weights are more than 100." + "\n")
            continue
        for i in range(0, len(values), 2):
            weight = int(values[i])
            grade = int(values[i + 1])
            total_grade = total_grade + (weight * grade)

        total_grade = total_grade / 100
        total_grade = round(total_grade, 1)
        class_average = class_average + total_grade
        out_file.write(halves[0] + "'s average: ")
        out_file.write(str(total_grade) + "\n")
        num += 1

    if num == 0:
        class_average = 0
    else:
        class_average = class_average / num
    out_file.write("Class average: {:.1f}".format(class_average))

    out_file.close()

def main():

    weighted_average("grades.txt", "avg.txt")

if __name__ == '__main__':
    main()


"""

Maeve O'Toole

sales_force.py

This program encapsulates a class for a sales person.

This assignment is entirely my own work.

"""

from sales_person import SalesPerson

class SalesForce:

    """

    SalesForce is a class that encapsulates data for a sales person

    """

    def __init__(self):
        """ initiates instance variables """
        self.sales_people = []

    def add_data(self, file_name):
        """ reads data from a file of salesData and adds the sales together """
        with open(file_name, 'r') as in_file:
            for line in in_file.readlines():
                parts = line.split(", ")
                person = SalesPerson(int(parts[0]), parts[1])
                sales = parts[2].split()
                for sale in sales:
                    person.enter_sale(float(sale))
                self.sales_people.append(person)

    def quota_report(self, quota):
        """ returns a list, where each element is itself a list of
        each seller’s employee_id, name, total sales, and a boolean
        value of whether or not they hit the specified quota """
        data = []
        for person in self.sales_people:
            person_data = [person.get_id(), person.get_name(),
                           person.total_sales(), person.met_quota(quota)]
            data.append(person_data)
        return data

    def top_seller(self):
        """ returns a list of the sales person who sold the most """
        top = []
        for i in range(len(self.sales_people)):
            for j in range(i + 1, len(self.sales_people)):
                if self.sales_people[j].compare_to(self.sales_people[i]) > 0:
                    self.sales_people[i], self.sales_people[j] = \
                        self.sales_people[j], self.sales_people[i]
        top.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() >= top[0].total_sales():
                top.append(self.sales_people[i])
            else:
                break
        return top

    def individual_sales(self, employee_id):
        """ returns the sales person with the given id number """
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
        return None

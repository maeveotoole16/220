"""

Maeve O'Toole

sales_person.py

This program encapsulates a class for a sales person.

This assignment is entirely my own work.

"""

class SalesPerson:

    """

    SalesPerson is a class that encapsulates information about an employee

    """

    def __init__(self, employee_id, name):
        """ initializes instance variables """
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """ returns employee id """
        return self.employee_id

    def get_name(self):
        """ returns employee name """
        return self.name

    def set_name(self, name):
        """ sets the employee name """
        self.name = name

    def enter_sale(self, sale):
        """ adds a sale amount """
        self.sales.append(float(sale))

    def total_sales(self):
        """ accumulates the total sale amount """
        acc = 0
        for sale in self.sales:
            acc = acc + sale
        return acc

    def get_sales(self):
        """ returns the sales """
        return self.sales

    def met_quota(self, quota):
        """ returns a Booleon if the employee has met the quota of sales """
        return self.total_sales() >= quota

    def compare_to(self, other):
        """ compares one employees sales to anothers """
        my_sales = self.total_sales()
        other_sales = other.total_sales()
        if my_sales > other_sales:
            return 1
        if my_sales < other_sales:
            return -1
        return 0

    def __str__(self):
        """ returns a string of an employees id, name, and total sales """
        return str(self.get_id()) + "-" + self.name + ": " + str(self.total_sales())

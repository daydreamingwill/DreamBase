from Main import *

class Employee(People):                                                   

    def __init__(self, person_type = None, Employee_ID = None, name = None, address = None, phone_number = None, Job = None, Salary = None):
        People.__init__(self, person_type = None, name = None, address = None, phone_number = None)

        self.Employee_ID = Employee_ID
        self.Job = Job
        self.Salary = Salary


class Customer(People):  

    def __init(self, person_type = None, Customer_ID = None, name = None, address = None, phone_number = None, Order_numbers = None):
        People.__init__(self, person_type = None, name = None, address = None, phone_number = None)

        self.Customer_ID = Customer_ID
        self.Order_number/s


class ShareHolder(People):                                             

    def __init__(self, person_type = None, Investor_ID = None, name = None, address = None, phone_number = None, Percentage_owned = None):
        People.__init__(self, person_type = None, name = None, address = None, phone_number = None)

        self.Percentage_owned = Percentage_owned






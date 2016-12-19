class People(object):
    """
    base class for all types of People involved in company
    """

    def __init__(self, person_type, name, address, phone_number):

        self.person_type = person_type
        self.name = name
        self.address = address
        self.phone_number = phone_number


class Employee(People):                                                   

    def __init__(
            self,
            person_type,
            employee_id,
            name,
            address,
            phone_number,
            job,
            salary
    ):

        People.__init__(self, person_type, name, address, phone_number)

        self.employee_ID = employee_id
        self.job = job
        self.Salary = salary


class Customer(People):  

    def __init(
            self,
            person_type,
            customer_id,
            name,
            address,
            phone_number,
            order_numbers
    ):

        People.__init__(self, person_type, name, address, phone_number)

        self.customer_id = customer_id
        self.order_number = order_numbers


class ShareHolder(People):                                             

    def __init__(
            self,
            person_type,
            investor_id,
            name,
            address,
            phone_number,
            percentage_owned
    ):

        People.__init__(self, person_type, name, address, phone_number)

        self.Percentage_owned = percentage_owned
        self.investor_id = investor_id

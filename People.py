class People(object):
    """
    base class for all types of People involved in company
    """

    def __init__(self, person_type=None, name=None, address=None, phone_number=None):

        self.person_type = person_type
        self.name = name


class Employee(People):                                                   

    def __init__(
            self,
            person_type=None,
            employee_id=None,
            name=None,
            address=None,
            phone_number=None,
            job=None,
            salary=None
    ):

        People.__init__(self, person_type=None, name=None, address=None, phone_number=None)

        self.employee_ID = employee_id
        self.job = job
        self.Salary = salary


class Customer(People):  

    def __init(
            self,
            person_type=None,
            customer_id=None,
            name=None,
            address=None,
            phone_number=None,
            order_numbers=None):
        People.__init__(self, person_type=None, name=None, address=None, phone_number=None)

        self.customer_id = customer_id
        self.order_number = order_numbers


class ShareHolder(People):                                             

    def __init__(
            self,
            person_type=None,
            investor_ID=None,
            name=None,
            address=None,
            phone_number=None,
            percentage_owned=None
    ):
        People.__init__(self, person_type=None, name=None, address=None, phone_number=None)

        self.Percentage_owned = percentage_owned






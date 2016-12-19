"""
Module provides the necessary controls to add new objects to the data base, via a factory function.
"""
from people_classes import Customer, Employee, ShareHolder

data_base_objects = {}


def create_database_object(database_object, args):
    database_object = None

    if database_object.lower == "employee":
        pass

    elif database_object.lower() == "customer":
        if len(args) != 6:
            pass

        customer_object = Customer()

    elif database_object.lower == "investor":
        pass

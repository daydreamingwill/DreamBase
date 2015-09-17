object_dictionary = {}

class People(object):

    """
    base class for all types of People involved in company
    """
    
    def __init__(self, person_type = None, name = None, address = None, phone_number = None):
        
        self.person_type = person_type
        self.name = name

    @classmethod
    def add_object(cls):

        """
        Functionality to allow the user to create a new object via raw_input.
        """    
    
        global object_dictionary
        finished_adding_object = False             
        
        while finished_adding_object == False:
            
            print "System >>> Please enter new " + cls.__name__ + " name. If the user doesn't want to create a new " + cls.__name__ + ", please enter \"exit\"."   
            pending_new_object = raw_input("User >>> ")

            while pending_new_object == "exit":                                       

                print "System >>> Please confirm, the user wishes to abandon creating a new " + cls.__name__ + "? (y/n)"
                abandon_confirmation = raw_input("User >>> ")

                if abandon_confirmation == "y":                             

                    pending_new_object = None
                    finished_adding_object = True

                elif abandon_confirmation == "n":                                                      

                    pending_new_object = None
                
                elif abandon_confirmation != "n" or "y":  # User told if input is invalid.               

                     print "System >>> " + abandon_confirmation + " is an invalid command."
   
            while pending_new_object != None:                                         

                print "System >>> Please confirm, user wishes to create a new " + cls.__name__ + " called " + pending_new_object + " (y/n)?"
                create_object_confirmation = raw_input("User >>> ")
                

                if create_object_confirmation == "y":

                    new_object = pending_new_object
                    new_object = cls()
                    setattr(new_object, 'name', eval('pending_new_object'))
                    
                    print "System >>> Creating new " + cls.__name__ + ", please wait."

                    object_dictionary[pending_new_object] = new_object  # Object appended to global list so it can be refrenced outside the class.
                    
                    pending_new_object = None                                       

                    print "System >>> Done."

                elif create_object_confirmation == "n":

                    pending_new_object = None

                else:

                    print "System >>> " + create_object_confirmation + " is an invalid command."


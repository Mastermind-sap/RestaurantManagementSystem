# importing all the necessary python files
import Manager
import Employee
import data
import database_connectivity


# This is the main class of the Restaurant Management System which calls methods from
# other classes from all the other python files
class RestaurantManagementSystem:

    # init method or constructor to initialise the stuffs related to this class
    def __init__(self):
        #   Data() class of the data.py file called
        data.Data()

        # Object of Database() class of database_connectivity.py created and its required methods called
        self.db = database_connectivity.Database()
        self.db.check_connection()
        self.db.main()

    # main method of this class
    def main(self):
        # Endless while loop of which runs throught the execution of the program
        while True:
            # Printing the restaurant name
            print(data.restaurant.capitalize() + " Management System")
            # Taking user input to whether he/she wants to continue as a manager or an employee
            # or wants to quit the program
            choice = input("""Enter 1 for Manager
            2 for Employee
            Any other number to exit""")
            if choice.isnumeric():
                if int(choice) == 1:
                    # Object of Manager() class of Manager.py created and its main method called
                    manager = Manager.Manager()
                    manager.main()
                elif int(choice) == 2:
                    # Object of Employee() class of Employee.py created and its main method called
                    employee = Employee.Employee()
                    employee.main()
                else:
                    break
            else:
                print("Invalid choice")


# Object of RestaurantManagementSystem() class created and the main method called
system = RestaurantManagementSystem()
system.main()

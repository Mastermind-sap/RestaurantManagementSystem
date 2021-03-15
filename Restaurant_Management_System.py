import Manager
import Employee
import data
import database_connectivity


class RestaurantManagementSystem:

    def __init__(self):
        data.Data()
        self.db = database_connectivity.Database()
        self.db.check_connection()
        self.db.main()

    def main(self):
        while True:
            print(data.restaurant.capitalize()+" Management System")
            choice = input("""Enter 1 for Manager
            2 for Employee
            Any other number to exit""")
            if choice.isnumeric():
                if int(choice) == 1:
                    manager = Manager.Manager()
                    manager.main()
                elif int(choice) == 2:
                    employee = Employee.Employee()
                    employee.main()
                    pass
                else:
                    break
            else:
                print("Invalid choice")


system = RestaurantManagementSystem()
system.main()

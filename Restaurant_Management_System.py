import Manager
import Employee
import data
import database_connectivity


class RestaurantManagementSystem:

    def __init__(self):
        data.Data()
        self.db=database_connectivity.Database()
        self.db.check_connection()
        self.db.main()
        self.manager=Manager.Manager()
        self.employee=Employee.Employee()
        pass

    def main(self):
        while True:
            print("Restaurant Management System")
            choice=input("""Enter 1 for Manager
            2 for Employee
            Any other number to exit""")
            if choice.isnumeric():
                if int(choice)==1:
                    self.manager.main()
                elif int(choice)==2:
                    self.employee.main()
                    pass
                else:
                    break
            else:
                print("Invalid choice")


system=RestaurantManagementSystem()
system.main()
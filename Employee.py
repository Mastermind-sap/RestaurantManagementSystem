import database_connectivity
# package to take masked input for passwords in terminal
import stdiomask

class Employee:
    def __init__(self):
        self.db = database_connectivity.Database()
        self.db.use_database("restaurant")

    def employee_login(self):
        id = input("Employee ID: ")
        passwd = stdiomask.getpass("Password: ", mask="*")
        if self.db.login_employee(id,passwd):
            return True
        else:
            return False

    def employee_signup(self):
        id=database_connectivity.vacant_employee_id
        print("Your Employee ID: "+str(id))
        name=input("Enter name: ")
        passwd=stdiomask.getpass("Password: ",mask="*")
        self.db.add_employee(id,name,passwd)
        print("Account created successfully")

    def main(self):
        while True:
            print("EMPLOYEE")

            choice = input("""Enter 1 for Login,
            2 for New Account,
            Any other number to Go back""")

            if choice.isnumeric():
                if int(choice) == 1:
                    if self.employee_login():
                        print("LOGIN SUCCESSFUL")
                        pass
                    else:
                        print("LOGIN UNSUCCESSFUL")
                        continue
                elif int(choice) == 2:
                    self.employee_signup()
                else:
                    break
            else:
                print("Invalid choice")
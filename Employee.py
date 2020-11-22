import database_connectivity
# package to take masked input for passwords in terminal
import stdiomask


class Employee:
    def __init__(self):
        self.db = database_connectivity.Database()
        self.db.use_database("restaurant")
        self.id = 0

    def employee_login(self):
        id = int(input("Employee ID: "))
        passwd = stdiomask.getpass("Password: ", mask="*")
        if self.db.login_employee(id, passwd):
            self.id = id
            return True
        else:
            return False

    def employee_signup(self):
        id = self.db.vacancy_read("vacant_employee_id")
        print("Your Employee ID: " + str(id))
        name = input("Enter name: ")
        passwd = stdiomask.getpass("Password: ", mask="*")
        self.db.add_employee(id, name, passwd)
        print("Account created successfully")
        self.db.vacancy_update("vacant_employee_id")

    def orders_related(self):
        pass

    def account_related(self):
        while True:
            choice = input("""Enter 1 to see your account details,
            2 to delete your account,
            Any other number to Go back""")
            if choice.isnumeric():
                if int(choice) == 1:
                    self.db.show_employee(self.id)
                elif int(choice) == 2:
                    self.db.remove_employee(self.id)
                    print("Account deleted")
                    self.id = 0
                    return False
                else:
                    return True

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
                        while True:
                            options = input("""Enter 1 for orders-related functions,
                                        2 to show menu,
                                        3 for account-related functions,
                                        Any other number to Log Out""")
                            if options.isnumeric():
                                if int(options) == 1:
                                    self.orders_related()
                                elif int(options) == 2:
                                    self.db.show_menu()
                                elif int(options) == 3:
                                    check = self.account_related()
                                    if check:
                                        continue
                                    else:
                                        break
                                else:
                                    self.id = 0
                                    break
                    else:
                        print("LOGIN UNSUCCESSFUL")
                        continue
                elif int(choice) == 2:
                    self.employee_signup()
                else:
                    break
            else:
                print("Invalid choice")

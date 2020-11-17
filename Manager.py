import database_connectivity
# package to take masked input for passwords in terminal
import stdiomask

class Manager:

    def __init__(self):
        self.db=database_connectivity.Database()
        self.db.use_database("restaurant")

    def manager_login(self):
        id = int(input("Manager ID: "))
        passwd = stdiomask.getpass("Password: ", mask="*")
        if self.db.login_manager(id,passwd):
            return True
        else:
            return False

    def manager_signup(self):
        id=self.db.vacancy_read("vacant_manager_id")
        print("Your Manager ID: " + str(id))
        name=input("Enter name: ")
        passwd=stdiomask.getpass("Password: ",mask="*")
        self.db.add_manager(id,name,passwd)
        print("Account created successfully")
        self.db.vacancy_update("vacant_manager_id")


    def main(self):
        while True:
            print("MANAGER")

            choice=input("""Enter 1 for Login,
            2 for New Account,
            Any other number to Go back""")

            if choice.isnumeric():
                if int(choice) == 1:
                    if self.manager_login():
                        print("LOGIN SUCCESSFUL")
                        pass
                    else:
                        print("LOGIN UNSUCCESSFUL")
                        continue
                elif int(choice) == 2:
                    self.manager_signup()
                else:
                    break
            else:
                print("Invalid choice")
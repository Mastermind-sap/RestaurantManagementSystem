import data
import database_connectivity
import data
# package to take masked input for passwords in terminal
import stdiomask

class Manager:

    def __init__(self):
        data.Data()
        self.db=database_connectivity.Database()
        self.db.check_connection()
        pass

    def manager_login(self):
        pass

    def manager_signup(self):
        id=int(input("Enter manager id: "))
        name=input("Enter name: ")
        passwd=stdiomask.getpass("Password: ",mask="*")

        pass


    def main(self):
        while True:
            print("MANAGER")

            choice=input("""Enter 1 for Login,
            2 for New Account,
            Any other number to Go back""")

            if choice.isnumeric():
                if int(choice) == 1:
                    if self.manager_login():
                        pass
                    else:
                        continue
                elif int(choice) == 2:
                    self.manager_signup()
                else:
                    break
            else:
                print("Invalid choice")
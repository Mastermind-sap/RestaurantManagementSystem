import data
import database_connectivity


class Employee:
    def __init__(self):
        data.Data()
        self.db=database_connectivity.Database()
        self.db.check_connection()
        pass
    def main(self):
        while True:
            print("EMPLOYEE")

            choice = input("""Enter 1 for Place order,
            2 for Print receipt,
            Any other number to Go back""")

            if choice.isnumeric():
                if int(choice) == 1:
                    pass
                elif int(choice) == 2:
                    pass
                else:
                    break
            else:
                print("Invalid choice")
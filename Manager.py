import data


class Manager:

    def __init__(self):
        pass


    def main(self):
        while True:
            print("MANAGER")

            choice=input("""Enter 1 for Login,
            2 for New Account,
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
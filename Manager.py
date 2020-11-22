import database_connectivity
# package to take masked input for passwords in terminal
import stdiomask


class Manager:

    def __init__(self):
        self.db = database_connectivity.Database()
        self.db.use_database("restaurant")
        self.id = 0

    def manager_login(self):
        id = int(input("Manager ID: "))
        passwd = stdiomask.getpass("Password: ", mask="*")
        if self.db.login_manager(id, passwd):
            self.id = id
            return True
        else:
            return False

    def manager_signup(self):
        id = self.db.vacancy_read("vacant_manager_id")
        print("Your Manager ID: " + str(id))
        name = input("Enter name: ")
        passwd = stdiomask.getpass("Password: ", mask="*")
        self.db.add_manager(id, name, passwd)
        print("Account created successfully")
        self.db.vacancy_update("vacant_manager_id")

    def menu_related(self):
        while True:
            choice = input("""Enter 1 to add an item to menu,
                        2 to remove an item from list,
                        3 to update an item from list,
                        4 to show menu,
                        5 to delete menu,
                        Any other number to Go back""")
            if choice.isnumeric():
                if int(choice) == 1:
                    number = self.db.vacancy_read("vacant_itemNo")
                    print("Item number: " + str(number))
                    name = input("Enter name of item: ")
                    price = float(input("Enter price of item: "))
                    self.db.add_item(number, name, price)
                    self.db.vacancy_update("vacant_itemNo")
                elif int(choice) == 2:
                    number = int(input("Enter item number of the item:"))
                    self.db.remove_item(number)
                elif int(choice) == 3:
                    number = int(input("Enter item number:"))
                    name = input("Enter name of item: ")
                    price = float(input("Enter price of item: "))
                    self.db.update_item(number, name, price)
                elif int(choice) == 4:
                    self.db.show_menu()
                elif int(choice) == 5:
                    self.db.delete_menu()
                    self.db.vacancy_reset("vacant_itemNo")
                    self.db.main()
                else:
                    break

    def orders_related(self):
        pass

    def tax_related(self):
        pass

    def account_related(self):
        while True:
            choice = input("""Enter 1 to see your account details,
            2 to delete your account,
            Any other number to Go back""")
            if choice.isnumeric():
                if int(choice) == 1:
                    self.db.show_manager(self.id)
                elif int(choice) == 2:
                    self.db.remove_manager(self.id)
                    print("Account deleted")
                    self.id = 0
                    return False
                else:
                    return True

    def main(self):
        while True:
            print("MANAGER")

            choice = input("""Enter 1 for Login,
            2 for New Account,
            Any other number to Go back""")

            if choice.isnumeric():
                if int(choice) == 1:
                    if self.manager_login():
                        print("LOGIN SUCCESSFUL")
                        while True:
                            options = input("""Enter 1 for menu-related functions,
                                        2 for orders-related functions,
                                        3 for tax-related functions,
                                        4 for account-related functions,
                                        Any other number to Log Out""")
                            if options.isnumeric():
                                if int(options) == 1:
                                    self.menu_related()
                                elif int(options) == 2:
                                    self.orders_related()
                                elif int(options) == 3:
                                    self.tax_related()
                                elif int(options) == 4:
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
                    self.manager_signup()
                else:
                    break
            else:
                print("Invalid choice")

# importing all the necessary python files
import database_connectivity
import data

# Library to take masked input for passwords in terminal
import stdiomask


class Manager:

    # init method or constructor to initialise the stuffs related to this class
    def __init__(self):
        self.db = database_connectivity.Database()
        self.db.use_database(data.restaurant)
        self.id = 0

    # Function called when a manager is to login to his/her account
    def manager_login(self):
        # Validating manager credentials from the database
        while True:
            id = input("Manager ID: ")
            if id.isnumeric():
                break
            else:
                print("ID can only be numeric")

        passwd = stdiomask.getpass("Password: ", mask="*")
        if self.db.login_manager(int(id), passwd):
            self.id = int(id)
            return True
        else:
            return False

    # Method called when a manager is to create a new account
    def manager_signup(self):
        id = self.db.vacancy_read("vacant_manager_id")
        print("Your Manager ID: " + str(id))
        name = input("Enter name: ")
        passwd = stdiomask.getpass("Password: ", mask="*")
        self.db.add_manager(id, name, passwd)
        print("Account created successfully")
        self.db.vacancy_update("vacant_manager_id")

    # Method which is called when a manager selects menu related functions
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
                    while True:
                        try:
                            price = float(input("Enter price of item: "))
                            break
                        except Exception:
                            print("Price can only be a floating point number")

                    self.db.add_item(number, name, price)
                    self.db.vacancy_update("vacant_itemNo")
                elif int(choice) == 2:
                    while True:
                        number = input("Enter item number of the item:")
                        if number.isnumeric():
                            number = int(number)
                            break
                        else:
                            print("Item number can only be an integer")
                    self.db.remove_item(number)
                elif int(choice) == 3:
                    while True:
                        number = input("Enter item number: ")
                        if number.isnumeric():
                            number = int(number)
                            break
                        else:
                            print("Item number can only be an integer")
                    name = input("Enter name of item: ")
                    while True:
                        try:
                            price = float(input("Enter price of item: "))
                            break
                        except Exception:
                            print("Price can only be a floating point number")
                    self.db.update_item(number, name, price)
                elif int(choice) == 4:
                    self.db.show_menu()
                elif int(choice) == 5:
                    self.db.delete_menu()
                    self.db.vacancy_reset("vacant_itemNo")
                    self.db.main()
                else:
                    break

    # Method which is called when a manager selects order related functions
    def orders_related(self):
        while True:
            choice = input("""Enter 1 to view list of orders,
            2 to print bill of previous orders,
            3 to delete records of any previous order,
            Any other number to Go back""")
            if choice.isnumeric():
                if int(choice) == 1:
                    while True:
                        choice1 = input("""Enter 1 to view list of orders by date of order,
                                    2 to view list of orders by exact name of customer,
                                    3 to view list of orders by part of the name of customer,
                                    4 to view list of orders by starting of the name of customer,
                                    5 to view order by order number,
                                    Any other number to Go back""")
                        if choice1.isnumeric():
                            if int(choice1) == 1:
                                date = ""
                                while True:
                                    yr = input("Enter year of order(0000-9999): ")
                                    if yr.isnumeric() and len(yr) == 4:
                                        date += yr
                                        break
                                    else:
                                        print("Invalid year")
                                        print("Enter the full year in four digit")
                                while True:
                                    mt = input("Enter month of order(01-12): ")
                                    if mt.isnumeric() and int(mt) in range(1, 13):
                                        date += "-" + mt
                                        break
                                    else:
                                        print("Invalid month\nEnter month in digits")
                                while True:
                                    dt = input("Enter date of order(1-31): ")
                                    if dt.isnumeric() and int(dt) in range(1, 32):
                                        date += "-" + dt
                                        break
                                    else:
                                        print("Invalid date")
                                self.db.view_orders_by_date(date)
                            elif int(choice1) == 2:
                                name = input("Enter name of the customer:")
                                self.db.view_orders_by_name_exact(name)
                            elif int(choice1) == 3:
                                pt = input("Enter part of the name of the customer:")
                                self.db.view_orders_by_name_part(pt)
                            elif int(choice1) == 4:
                                st = input("Enter start of the name of the customer:")
                                self.db.view_orders_by_name_start(st)
                            elif int(choice1) == 5:
                                while True:
                                    order_number = input("Enter order number: ")
                                    if order_number.isnumeric():
                                        self.db.view_orders_by_ordernum(int(order_number))
                                        break
                                    else:
                                        print("Invalid order number\nOrder number can be only integer")
                            else:
                                break

                elif int(choice) == 2:
                    while True:
                        order_number = input("Enter order number: ")
                        if order_number.isnumeric():
                            self.db.print_bill(int(order_number))
                            break
                        else:
                            print("Invalid order number\nOrder number can be only integer")

                elif int(choice) == 3:
                    while True:
                        order_number = input("Enter order number: ")
                        if order_number.isnumeric():
                            self.db.delete_order(int(order_number))
                            break
                        else:
                            print("Invalid order number\nOrder number can be only integer")

                else:
                    break

    # Method which is called when a manager selects tax related functions
    def tax_related(self):
        while True:
            choice = input("""Enter 1 to add new tax,
                        2 to remove a tax from list,
                        3 to update a tax from list,
                        4 to show all taxes,
                        5 to delete all taxes,
                        Any other number to Go back""")
            if choice.isnumeric():
                if int(choice) == 1:
                    number = self.db.vacancy_read("vacant_taxNo")
                    print("Tax number: " + str(number))
                    tax = input("Enter name of tax: ")
                    while True:
                        try:
                            percent = float(input("Enter tax percent: "))
                            break
                        except Exception:
                            print("Tax percent can only be a floating point number")

                    self.db.add_tax(number, tax, percent)
                    self.db.vacancy_update("vacant_taxNo")
                elif int(choice) == 2:
                    while True:
                        number = input("Enter tax number:")
                        if number.isnumeric():
                            number = int(number)
                            break
                        else:
                            print("Tax number can only be an integer")
                    self.db.remove_tax(number)
                elif int(choice) == 3:
                    while True:
                        number = input("Enter tax number:")
                        if number.isnumeric():
                            number = int(number)
                            break
                        else:
                            print("Tax number can only be an integer")
                    tax = input("Enter name of tax: ")
                    while True:
                        try:
                            percent = float(input("Enter tax percent: "))
                            break
                        except Exception:
                            print("Tax percent can only be a floating point number")

                    self.db.update_tax(number, tax, percent)
                elif int(choice) == 4:
                    self.db.show_tax()
                elif int(choice) == 5:
                    self.db.delete_tax()
                    self.db.vacancy_reset("vacant_taxNo")
                    self.db.main()
                else:
                    break

    # Method which is called when a manager selects account related functions
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

    # Main method
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

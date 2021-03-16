# Library imported that is used to make sql connection
import mysql.connector
# Importing data.py
import data
# Library used to take system date
import datetime as dt
# Library to print well designed tables
import tabulate


class Database:

    # init method or constructor to initialise the stuffs related to this class
    def __init__(self):
        # Creating python and mysql connectivity using mysql.connector library
        try:
            self.mydb = mysql.connector.connect(host="localhost", user=data.username, passwd=data.password)
            self.mycursor = self.mydb.cursor()
        except Exception as e:
            print("Username or password entered is incorrect")
            self.mydb=False

    # checks whether the python and mysql connection has been build properly
    def check_connection(self):
        if self.mydb:
            print("Connection successful")
        else:
            print("Connection unsuccessful")
            exit()

    # Method to create database
    def create_database(self, database_name, condition="if not exists "):
        self.mycursor.execute("create database " + condition + database_name)
        self.mydb.commit()

    # Method to show databases
    def show_databases(self):
        self.mycursor.execute("show databases")
        for db in self.mycursor:
            print(db)

    # Method to use database
    def use_database(self, name):
        self.mycursor.execute("use " + name)

    # Method to show tables in the database
    def show_tables(self):
        self.mycursor.execute("show tables")
        for i in self.mycursor:
            print(i)

    # Method to read values in table
    def read_table(self, tablename, fields="*"):
        self.mycursor.execute("select " + fields + " from " + tablename)
        myresult = self.mycursor.fetchall()
        for row in myresult:
            print(row)

    # Method to delete a table
    def delete_table(self, tablename):
        sql = "drop table " + tablename
        self.mycursor.execute(sql)
        self.mydb.commit()

    # Method to delete a database
    def delete_database(self, dbname):
        sql = "drop database " + dbname
        self.mycursor.execute(sql)
        self.mydb.commit()

    # Methods for manager

    # Method to add manager details while creating a new account
    def add_manager(self, id, name, password):
        query = "INSERT INTO managers VALUE ({},'{}','{}')".format(id, name, password)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Method to delete manager details while deleting the account
    def remove_manager(self, id):
        query = "DELETE FROM managers WHERE manager_ID= {}".format(id)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Method to check credentials of the manager while logging in
    def login_manager(self, id, password):
        query = "SELECT manager_ID,manager_password FROM managers"
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        for i in data:
            if (id, password) == i:
                return True
        return False

    # Method to display account details
    def show_manager(self, id):
        read_query = "SELECT * FROM managers WHERE manager_ID={}".format(id)
        self.mycursor.execute(read_query)
        data = self.mycursor.fetchall()
        print("Manager ID: " + str(data[0][0]))
        print("Manager name: " + data[0][1])
        print("Manager password: " + data[0][2])

    # Methods for employee

    # Method to add employee details while creating a new account
    def add_employee(self, id, name, password):
        query = "INSERT INTO employees VALUE ({},'{}','{}')".format(id, name, password)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Method to delete employee details while deleting the account
    def remove_employee(self, id):
        query = "DELETE FROM employees WHERE employee_ID= {}".format(id)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Method to check credentials of the employee while logging in
    def login_employee(self, id, password):
        query = "SELECT employee_ID,employee_password FROM employees"
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        for i in data:
            if (id, password) == i:
                return True
        return False

    # Method to display account details
    def show_employee(self, id):
        read_query = "SELECT * FROM employees WHERE employee_ID={}".format(id)
        self.mycursor.execute(read_query)
        data = self.mycursor.fetchall()
        print("Employee ID: " + str(data[0][0]))
        print("Employee name: " + data[0][1])
        print("Employee password: " + data[0][2])

    # Methods for menu

    # Method to add item to menu
    def add_item(self, num, name, price):
        add_query = "INSERT INTO menu VALUE ({},'{}',{})".format(num, name, price)
        self.mycursor.execute(add_query)
        self.mydb.commit()
        print("ITEM SUCCESSFULLY ADDED")

    # Method to remove item from menu
    def remove_item(self, num):
        self.mycursor.execute("""SELECT * FROM menu""")
        original_no_rows = len(self.mycursor.fetchall())
        rem_query = "DELETE FROM menu WHERE item_NO= {}".format(num)
        self.mycursor.execute(rem_query)
        self.mydb.commit()
        self.mycursor.execute("""SELECT * FROM menu""")
        final_no_rows = len(self.mycursor.fetchall())
        if original_no_rows != final_no_rows:
            print("ITEM SUCCESSFULLY REMOVED")
        else:
            print("ITEM NOT THERE IN MENU ALREADY")

    # Method to update item details
    def update_item(self, num, name, price):
        check_query = """SELECT item_NO FROM menu"""
        self.mycursor.execute(check_query)
        item_no_present = self.mycursor.fetchall()
        if (num,) in item_no_present:
            update_query = """UPDATE menu SET item='{}',price={} WHERE item_NO= {}""".format(name, price, num)
            self.mycursor.execute(update_query)
            self.mydb.commit()
            print("ITEM UPDATED SUCCESSFULLY")
        else:
            print("ITEM NUMBER INVALID! NO ITEM WITH THIS NUMBER PRESENT IN MENU")

    # Method to show menu
    def show_menu(self):
        read_query = """SELECT * FROM menu"""
        self.mycursor.execute(read_query)
        data = self.mycursor.fetchall()
        # print("{:<20} | {:^20} | {:>20}".format("item_NO", "item", "price"))
        # for i in data:
        #     print("{:<20} | {:^20} | {:>20}".format(i[0], i[1], i[2]))
        headers = ["item_NO", "item", "price"]
        print(tabulate.tabulate(data, headers, tablefmt="psql"))

    # Method to delete existing menu
    def delete_menu(self):
        self.delete_table("menu")
        print("Menu Deleted!")

    # Methods for tax

    # Method to add tax
    def add_tax(self, num, tax, percent):
        add_query = "INSERT INTO tax VALUE ({},'{}',{})".format(num, tax, percent)
        self.mycursor.execute(add_query)
        self.mydb.commit()
        print("TAX SUCCESSFULLY ADDED")

    # Method to remove tax
    def remove_tax(self, num):
        self.mycursor.execute("""SELECT * FROM tax""")
        original_no_rows = len(self.mycursor.fetchall())
        rem_query = "DELETE FROM tax WHERE tax_NO= {}".format(num)
        self.mycursor.execute(rem_query)
        self.mydb.commit()
        self.mycursor.execute("""SELECT * FROM tax""")
        final_no_rows = len(self.mycursor.fetchall())
        if original_no_rows != final_no_rows:
            print("TAX SUCCESSFULLY REMOVED")
        else:
            print("TAX NOT THERE ALREADY")

    # Method to update tax
    def update_tax(self, num, tax, percent):
        check_query = """SELECT tax_NO FROM tax"""
        self.mycursor.execute(check_query)
        tax_no_present = self.mycursor.fetchall()
        if (num,) in tax_no_present:
            update_query = """UPDATE tax SET tax='{}',percent={} WHERE tax_NO= {}""".format(tax, percent, num)
            self.mycursor.execute(update_query)
            self.mydb.commit()
            print("TAX UPDATED SUCCESSFULLY")
        else:
            print("TAX NUMBER INVALID! NO TAX WITH THIS NUMBER PRESENT")

    # Method to show all taxes
    def show_tax(self):
        read_query = """SELECT * FROM tax"""
        self.mycursor.execute(read_query)
        data = self.mycursor.fetchall()
        # print("{:<20} | {:^20} | {:>20}".format("tax_NO", "tax", "percent"))
        # for i in data:
        #     print("{:<20} | {:^20} | {:>20}".format(i[0], i[1], i[2]))
        headers = ["tax_NO", "tax", "percent"]
        print(tabulate.tabulate(data, headers, tablefmt="psql"))

    # Method to delete existing tax
    def delete_tax(self):
        self.delete_table("tax")
        print("All taxes deleted!")

    # Methods for orders

    # Method to take new order
    def take_order(self):
        # reading menu
        read_menu = """SELECT * FROM menu"""
        self.mycursor.execute(read_menu)
        menu_details = self.mycursor.fetchall()

        # creating a dictionary menu with item_NO as key and list of item name and price as value
        menu = {}
        for i in menu_details:
            menu[i[0]] = [i[1], i[2]]

        order_no = self.vacancy_read("vacant_orderNo")
        print("Order Number:" + str(order_no))
        date = str(dt.date.today())
        print("Date: " + date)
        name = input("Enter customer name:")

        print(
            """Enter item number of the item you want to order\nEnter menu to see menu while ordering \nEnter quit to stop ordering""")
        order = ""
        sl = 1
        while True:
            item_num = input("Enter item number: ")
            if item_num.isnumeric():
                if int(item_num) in menu.keys():
                    while True:
                        quantity = input("Enter quantity of " + menu[int(item_num)][0] + " you want to order: ")
                        if quantity.isnumeric():
                            if quantity > 0:
                                order += """({},'{}',{},{},{}),""".format(sl, menu[int(item_num)][0], menu[int(item_num)][1],
                                                                          quantity, menu[int(item_num)][1] * quantity)
                                sl += 1
                                break
                            else:
                                print("Invalid quantity \nQuantity of item cannot be zero or negative")
                                break
                        else:
                            print("Quantity can only be a whole number")
                else:
                    print("Item number does not exist in menu")
            elif item_num.lower() == "menu":
                self.show_menu()
            elif item_num.lower() == "quit":
                if len(order) == 0:
                    print("Nothing ordered \nDeleting order progress")
                    return False
                else:
                    # inserting order details in order_details table
                    insert_order_details = "INSERT INTO order_details VALUE ({},'{}','{}')".format(order_no, name, date)
                    self.mycursor.execute(insert_order_details)
                    self.mydb.commit()

                    # creating order table
                    order_table_create = """CREATE TABLE IF NOT EXISTS order{}(
                    Sl_no INTEGER NOT NULL PRIMARY KEY,
                    item TEXT,
                    price FLOAT,
                    quantity INTEGER,
                    amount FLOAT);""".format(order_no)
                    self.mycursor.execute(order_table_create)

                    # inserting order in order table
                    insert_order = """INSERT INTO order{} VALUES {};""".format(order_no, order[:-1])
                    self.mycursor.execute(insert_order)
                    self.mydb.commit()

                    self.vacancy_update("vacant_orderNo")
                    print("Order placed successfully!")
                    self.print_bill(order_no)
                    return True
            else:
                print("Invalid Entry")

    # Method to print bill of previous order
    def print_bill(self, orderno):
        try:
            order_details_query = """SELECT * FROM order_details WHERE order_NO={}""".format(orderno)
            self.mycursor.execute(order_details_query)
            order_details = self.mycursor.fetchall()
            print("\t\t\t***INVOICE***")
            print("Order Number: " + str(order_details[0][0]))
            print("Name of customer: " + order_details[0][1])
            print("Date: " + str(order_details[0][2]))
            order_query = """SELECT * FROM order{}""".format(orderno)
            self.mycursor.execute(order_query)
            order = self.mycursor.fetchall()
            subtotal_query = """SELECT SUM(amount) FROM order{}""".format(orderno)
            self.mycursor.execute(subtotal_query)
            subtotal = self.mycursor.fetchall()[0][0]
            order.append(["", "", "", "Subtotal: ", subtotal])
            tax_query = """SELECT * FROM tax"""
            self.mycursor.execute(tax_query)
            tax = self.mycursor.fetchall()
            total = subtotal
            for i in tax:
                order.append(["", "", "", i[1] + ": ", str(i[2]) + "%"])
                total -= (i[2] / 100.0) * total
            order.append(["", "", "", "Total: ", total])
            headers = ["Sl_no", "Item", "Price", "Quantity", "Amount"]
            print(tabulate.tabulate(order, headers, tablefmt="psql"))
            return True
        except Exception:
            print("Invalid order number")
        return False

    # Method to view previous orders filtered by date
    def view_orders_by_date(self, date):
        order_details_query = """SELECT * FROM order_details WHERE date='{}'""".format(date)
        self.mycursor.execute(order_details_query)
        order_details = self.mycursor.fetchall()
        if len(order_details) != 0:
            headers = ["Order Number", "Name of customer", "Date"]
            print(tabulate.tabulate(order_details, headers, tablefmt="psql"))
        else:
            print("No orders placed on " + date)

    # Method to view previous orders filtered by name
    def view_orders_by_name_exact(self, name):
        order_details_query = """SELECT * FROM order_details WHERE name='{}'""".format(name)
        self.mycursor.execute(order_details_query)
        order_details = self.mycursor.fetchall()
        if len(order_details) != 0:
            headers = ["Order Number", "Name of customer", "Date"]
            print(tabulate.tabulate(order_details, headers, tablefmt="psql"))
        else:
            print("No orders placed by the name " + name)

    # Method to view previous orders filtered by name
    def view_orders_by_name_part(self, part):
        order_details_query = """SELECT * FROM order_details WHERE name LIKE '%{}%'""".format(part)
        self.mycursor.execute(order_details_query)
        order_details = self.mycursor.fetchall()
        if len(order_details) != 0:
            headers = ["Order Number", "Name of customer", "Date"]
            print(tabulate.tabulate(order_details, headers, tablefmt="psql"))
        else:
            print("No orders found")

    # Method to view previous orders filtered by name
    def view_orders_by_name_start(self, start):
        order_details_query = """SELECT * FROM order_details WHERE name LIKE '{}%'""".format(start)
        self.mycursor.execute(order_details_query)
        order_details = self.mycursor.fetchall()
        if len(order_details) != 0:
            headers = ["Order Number", "Name of customer", "Date"]
            print(tabulate.tabulate(order_details, headers, tablefmt="psql"))
        else:
            print("No orders found")

    # Method to view previous orders by unique order number
    def view_orders_by_ordernum(self, orderno):
        order_details_query = """SELECT * FROM order_details WHERE order_NO={}""".format(orderno)
        self.mycursor.execute(order_details_query)
        order_details = self.mycursor.fetchall()
        if len(order_details) != 0:
            headers = ["Order Number", "Name of customer", "Date"]
            print(tabulate.tabulate(order_details, headers, tablefmt="psql"))
        else:
            print("No orders with the order number " + str(orderno))

    # Method to delete order details from database
    def delete_order(self, orderno):
        try:
            delete_order = """DROP TABLE order{}""".format(orderno)
            self.mycursor.execute(delete_order)
            self.mydb.commit()
            delete_order_details = """DELETE FROM order_details WHERE order_NO={}""".format(orderno)
            self.mycursor.execute(delete_order_details)
            self.mydb.commit()
            print("Records of order number " + str(orderno) + " deleted!")
        except Exception:
            print("Order number " + str(orderno) + " does not exist")

    # Methods for vacancy

    # Method to read vacant ids
    def vacancy_read(self, name):
        query = """SELECT ID FROM vacancy WHERE name = '{}'""".format(name)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data[0][0]

    # Method to increment vacant id by 1
    def vacancy_update(self, name):
        query = """UPDATE vacancy SET ID =ID + 1 WHERE name = '{}'""".format(name)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Method to reset vacant ids to 1
    def vacancy_reset(self, name):
        query = """UPDATE vacancy SET ID =1 WHERE name = '{}'""".format(name)
        self.mycursor.execute(query)
        self.mydb.commit()

    # Main method used to set up the entire database if not done before
    def main(self):
        # Creating database restaurant if it is not created already before
        self.mycursor.execute("create database if not exists " + data.restaurant)
        # Using database restaurant
        self.mycursor.execute("use " + data.restaurant + ";")

        # Creating table for manager details
        manager_query = """CREATE TABLE IF NOT EXISTS managers(
                                manager_ID INTEGER NOT NULL PRIMARY KEY,
                                manager_name TEXT,
                                manager_password TEXT)"""
        self.mycursor.execute(manager_query)

        # Creating table for employee details
        employee_query = """CREATE TABLE IF NOT EXISTS employees(
                                        employee_ID INTEGER NOT NULL PRIMARY KEY,
                                        employee_name TEXT,
                                        employee_password TEXT)"""
        self.mycursor.execute(employee_query)

        # Creating table for menu details
        menu_query = """CREATE TABLE IF NOT EXISTS menu(
                                        item_NO INTEGER NOT NULL PRIMARY KEY,
                                        item TEXT,
                                        price FLOAT)"""
        self.mycursor.execute(menu_query)

        # Creating table for tax details
        tax_query = """CREATE TABLE IF NOT EXISTS tax(
                                                tax_NO INTEGER NOT NULL PRIMARY KEY,
                                                tax TEXT,
                                                percent FLOAT)"""
        self.mycursor.execute(tax_query)

        # Creating table for order details
        order_query = """CREATE TABLE IF NOT EXISTS order_details(
                                                order_NO INTEGER NOT NULL PRIMARY KEY,
                                                name TEXT,
                                                date DATE)"""
        self.mycursor.execute(order_query)

        # Creating table for vacancy details
        vacancy_query = """CREATE TABLE IF NOT EXISTS vacancy(
                                                name TEXT,
                                                id INTEGER DEFAULT 1)"""
        self.mycursor.execute(vacancy_query)

        vacant_employee_id_query = """INSERT INTO vacancy (name)
                                SELECT("vacant_employee_id")
                                WHERE NOT EXISTS(SELECT * FROM vacancy WHERE name="vacant_employee_id")"""
        self.mycursor.execute(vacant_employee_id_query)
        self.mydb.commit()

        vacant_manager_id_query = """INSERT INTO vacancy (name)
                                SELECT("vacant_manager_id")
                                WHERE NOT EXISTS(SELECT * FROM vacancy WHERE name="vacant_manager_id")"""
        self.mycursor.execute(vacant_manager_id_query)
        self.mydb.commit()

        vacant_itemNo_query = """INSERT INTO vacancy (name)
                                SELECT("vacant_itemNo")
                                WHERE NOT EXISTS(SELECT * FROM vacancy WHERE name="vacant_itemNo")"""
        self.mycursor.execute(vacant_itemNo_query)
        self.mydb.commit()

        vacant_orderNo_query = """INSERT INTO vacancy (name)
                                SELECT("vacant_orderNo")
                                WHERE NOT EXISTS(SELECT * FROM vacancy WHERE name="vacant_orderNo")"""
        self.mycursor.execute(vacant_orderNo_query)
        self.mydb.commit()

        vacant_taxNo_query = """INSERT INTO vacancy (name)
                                SELECT("vacant_taxNo")
                                WHERE NOT EXISTS(SELECT * FROM vacancy WHERE name="vacant_taxNo")"""
        self.mycursor.execute(vacant_taxNo_query)
        self.mydb.commit()

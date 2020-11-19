import mysql.connector
import data


class Database:
    def __init__(self):
        # Creating python and mysql connectivity using mysql.connector library
        self.mydb = mysql.connector.connect(host="localhost", user=data.username, passwd=data.password)
        self.mycursor = self.mydb.cursor()

    # checks whether the python and mysql connection has been build properly
    def check_connection(self):
        if self.mydb:
            print("Connection successful")
        else:
            print("Connection unsuccessful")

    # function to create database
    def create_database(self, database_name, condition="if not exists "):
        self.mycursor.execute("create database " + condition + database_name)
        self.mydb.commit()

    # function to show databases
    def show_databases(self):
        self.mycursor.execute("show databases")
        for db in self.mycursor:
            print(db)

    # function to use database
    def use_database(self, name):
        self.mycursor.execute("use " + name)

    # function to create tables in the database
    def create_table(self):
        pass

    # function to show tables in the database
    def show_tables(self):
        self.mycursor.execute("show tables")
        for i in self.mycursor:
            print(i)

    # function to insert values in table
    def insert_values(self):
        pass

    # function to delete values in table
    def delete_values(self):
        pass

    # function to read values in table
    def read_table(self, tablename, fields="*"):
        self.mycursor.execute("select " + fields + " from " + tablename)
        myresult = self.mycursor.fetchall()
        for row in myresult:
            print(row)

    # function to update values in table
    def update(self):
        pass

    # function to delete a table
    def delete_table(self, tablename):
        sql = "drop table " + tablename
        self.mycursor.execute(sql)
        self.mydb.commit()

    # function to delete a database
    def delete_database(self, dbname):
        sql = "drop database " + dbname
        self.mycursor.execute(sql)
        self.mydb.commit()

    # functions for manager

    def add_manager(self, id, name, password):
        query = "INSERT INTO managers VALUE ({},'{}','{}')".format(id, name, password)
        self.mycursor.execute(query)
        self.mydb.commit()

    def remove_manager(self, id):
        query = "DELETE FROM managers WHERE manager_ID= {}".format(id)
        self.mycursor.execute(query)
        self.mydb.commit()

    def login_manager(self, id, password):
        query = "SELECT manager_ID,manager_password FROM managers"
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        for i in data:
            if (id, password) == i:
                return True
        return False

    # functions for employee

    def add_employee(self, id, name, password):
        query = "INSERT INTO employees VALUE ({},'{}','{}')".format(id, name, password)
        self.mycursor.execute(query)
        self.mydb.commit()

    def remove_employee(self, id):
        query = "DELETE FROM employees WHERE employee_ID= {}".format(id)
        self.mycursor.execute(query)
        self.mydb.commit()

    def login_employee(self, id, password):
        query = "SELECT employee_ID,employee_password FROM employees"
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        for i in data:
            if (id, password) == i:
                return True
        return False

    # functions for menu

    def add_item(self, num, name, price):
        add_query = "INSERT INTO menu VALUE ({},'{}',{})".format(num, name, price)
        self.mycursor.execute(add_query)
        self.mydb.commit()

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

    def show_menu(self):
        read_query = """SELECT * FROM menu"""
        self.mycursor.execute(read_query)
        data = self.mycursor.fetchall()
        print("item_NO  |  item  |  price")
        for i in data:
            print(str(i[0]) + "  |  " + i[1] + "  |  " + str(i[2]))

    # functions for vacancy
    def vacancy_read(self, name):
        query = """SELECT ID FROM vacancy WHERE name = '{}'""".format(name)
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data[0][0]

    def vacancy_update(self, name):
        query = """UPDATE vacancy SET ID =ID + 1 WHERE name = '{}'""".format(name)
        self.mycursor.execute(query)
        self.mydb.commit()

    def main(self):
        # creating database "restaurant" if it is not created already before
        self.mycursor.execute("create database if not exists restaurant")
        # using database restaurant
        self.mycursor.execute("use restaurant;")

        # creating table for manager details
        manager_query = """CREATE TABLE IF NOT EXISTS managers(
                                manager_ID INTEGER NOT NULL PRIMARY KEY,
                                manager_name TEXT,
                                manager_password TEXT)"""
        self.mycursor.execute(manager_query)

        # creating table for employee details
        employee_query = """CREATE TABLE IF NOT EXISTS employees(
                                        employee_ID INTEGER NOT NULL PRIMARY KEY,
                                        employee_name TEXT,
                                        employee_password TEXT)"""
        self.mycursor.execute(employee_query)

        # creating table for menu details
        menu_query = """CREATE TABLE IF NOT EXISTS menu(
                                        item_NO INTEGER NOT NULL PRIMARY KEY,
                                        item TEXT,
                                        price FLOAT)"""
        self.mycursor.execute(menu_query)

        # creating table for tax details
        tax_query = """CREATE TABLE IF NOT EXISTS tax(
                                                tax TEXT,
                                                percent FLOAT)"""
        self.mycursor.execute(tax_query)

        # creating table for vacancy details
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

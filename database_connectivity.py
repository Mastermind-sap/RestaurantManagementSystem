import mysql.connector
import data


class Database:
    def __init__(self):
        # Creating python and mysql connectivity using mysql.connector library
        self.mydb = mysql.connector.connect(host="localhost", user=data.username, passwd=data.password)
        self.mycursor = self.mydb.cursor()

    # checks whether the python and mysql connection has been build properly
    def check_connection(self):
        if self.mydb :
            print("Connection successful")
        else:
            print("Connection unsuccessful")

    # function to create database
    def create_database(self, database_name, condition="if not exists "):
        self.mycursor.execute("create database "+condition+database_name)
        self.mydb.commit()

    # function to show databases
    def show_databases(self):
        self.mycursor.execute("show databases")
        for db in self.mycursor:
            print(db)

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
        self.mycursor.execute("select "+fields+" from "+tablename)
        myresult = self.mycursor.fetchall()
        for row in myresult:
            print(row)

    # function to update values in table
    def update(self):
        pass

    # function to delete a table
    def delete_table(self, tablename):
        sql = "drop table "+tablename
        self.mycursor.execute(sql)
        self.mydb.commit()

    # function to delete a database
    def delete_database(self, dbname):
        sql = "drop database "+dbname
        self.mycursor.execute(sql)
        self.mydb.commit()

    def main(self):
        # creating database "restaurant" if it is not created already before
        self.mycursor.execute("create database if not exists restaurant")
        # using database restaurant
        self.mycursor.execute("use restaurant;")

        # creating table for manager details
        manager_query="""CREATE TABLE IF NOT EXISTS managers(
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
        menu_query="""CREATE TABLE IF NOT EXISTS menu(
                                        item_NO INTEGER NOT NULL PRIMARY KEY,
                                        item TEXT,
                                        price FLOAT)"""
        self.mycursor.execute(menu_query)

        # creating table for tax details
        tax_query = """CREATE TABLE IF NOT EXISTS tax(
                                                CGST FLOAT,
                                                SGST FLOAT)"""
        self.mycursor.execute(tax_query)

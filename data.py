# package to take masked input for passwords in terminal
import stdiomask


# data to be used to access local sql server
username = "root"
password = "mysql"
vacant_employee_id=1
vacant_manager_id=1

class Data:
    def __init__(self):
        # Taking user and password to be used to create python-sql connectivity
        print("DATABASE AUTHENTICATION")
        user = input("Username: ")
        if len(user) != 0:
            global username
            username = user
        else:
            print("Default user to be used")
        passwd = stdiomask.getpass("Password: ",mask="*")
        if len(passwd) != 0 :
            global password
            password = passwd
        else:
            print("Default password to be used")
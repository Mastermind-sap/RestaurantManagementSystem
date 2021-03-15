# package to take masked input for passwords in terminal
import stdiomask

# Library to display terminal images
# import timg

# Library to print a colourful header
import cfonts

# data to be used to access local sql server
# global variables
username = "root"
password = "mysql"
restaurant = "restaurant"


class Data:

    # init method or constructor to initialise the stuffs related to this class
    def __init__(self):
        # Starting of the output

        # optional ascii image (if wanted)
        # obj = timg.Renderer()
        # obj.load_image_from_file("icon1.ico")
        # obj.resize(100, 50)
        # obj.render(timg.ASCIIMethod)
        # print()

        # A header for the program created with the library cfonts
        cfonts.say("Restaurant", font='chrome', colors=['candy', 'candy', 'candy'], align='center', space=False)
        cfonts.say("Management", font='chrome', colors=['candy', 'candy', 'candy'], align='center', space=False)
        cfonts.say("System", font='chrome', colors=['candy', 'candy', 'candy'], align='center', space=False)
        print()

        # Taking username,password and restaurant name to be used to create python-sql connectivity
        print("DATABASE AUTHENTICATION")
        user = input("Username: ")
        if len(user) != 0:
            global username
            username = user
        else:
            print("Default user to be used")
        passwd = stdiomask.getpass("Password: ", mask="*")
        if len(passwd) != 0:
            global password
            password = passwd
        else:
            print("Default password to be used")
        res = input("Enter restaurant name to access its database: ")
        if len(res) != 0:
            global restaurant
            restaurant = res
        else:
            print("Default database (i.e. 'restaurant') to be used")

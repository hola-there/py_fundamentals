# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #3 from Week 3

from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register

# Declaring variables
database = {"admin": "password123", }
donations = []
authorized_user = ""
run_donations = True


# Determines if the login worked
def login_check():
    if authorized_user == "":
        print("You must be logged in to donate.\n")
    else:
        print("Logged in as:", authorized_user, "\n")


# Checks if the result of whether a user is registered already or not
def can_register(database_passed, username_passed, password_passed):
    if authorized_user != "":
        database_passed[str(username_passed)] = password_passed


# user is presented with options
def homepage_option_selection():
    login_check()
    global authorized_user
    choice = input("Choose and Option: ")
    if (choice.isnumeric() and int(choice) == 1) or choice.lower() == "login":
        username = input("\nPlease enter your account's username: ")
        password = input("Please enter your account's password: ")
        authorized_user = login(database, username, password)
    elif (choice.isnumeric() and int(choice) == 2) or choice.lower() == "register":
        username = input("\nPlease enter your account's username: ")
        password = input("Please enter your account's password: ")
        authorized_user = register(database, username)
        can_register(database, username, password)
    elif (choice.isnumeric() and int(choice) == 3) or choice.lower() == "donate":
        print("TODO: Write Donate Functionality")
    elif (choice.isnumeric() and int(choice) == 4) or choice.lower() == "show donations":
        print("TODO: Write Show Donations Functionality")
    elif (choice.isnumeric() and int(choice) == 5) or choice.lower() == "exit":
        print("Goodbye...exiting now")
        global run_donations
        run_donations = False


while run_donations:
    show_homepage()
    homepage_option_selection()

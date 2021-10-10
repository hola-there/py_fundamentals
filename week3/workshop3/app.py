# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #3 from Week 3

from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# Declaring variables
database = {"admin": "password123", }
donations = []
authorized_user = ""
run_donations = True


# Determines if the login worked
def login_check(donate_check):
    if authorized_user == "" and donate_check == False:
        print("You must be logged in to donate.\n")
    elif donate_check == True and authorized_user == "":
        print("You are not logged in.")
        return False
    elif donate_check == True:
        return True
    else:
        print("Logged in as:", authorized_user, "\n")


# Checks if the result of whether a user is registered already or not
def can_register(database_passed, username_passed, password_passed):
    if authorized_user != "":
        database_passed[str(username_passed)] = password_passed


# user is presented with options
def homepage_option_selection():
    login_check(False)
    global authorized_user
    global donations
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
        if login_check(True):
            donation = donate(authorized_user)
            donations.append(donation)
    elif (choice.isnumeric() and int(choice) == 4) or choice.lower() == "show donations":
        show_donations(donations)
    elif (choice.isnumeric() and int(choice) == 5) or choice.lower() == "exit":
        print("Goodbye...exiting now")
        global run_donations
        run_donations = False


while run_donations:
    show_homepage()
    homepage_option_selection()

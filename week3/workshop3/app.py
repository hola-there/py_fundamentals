# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #3 from Week 3

from donations_pkg.homepage import show_homepage


# Decalring variables
database = {"admin", "password123"}
donations = []
authorized_user = ""
run_donations = True


def login_check():
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)


def homepage_option_selection():
    login_check()
    choice = input("Choose and Option: ")
    if (choice.isnumeric() and int(choice) == 1) or choice.lower() == "login":
        print("TODO: Write Login Functionality")
    elif (choice.isnumeric() and int(choice) == 2) or choice.lower() == "register":
        print("TODO: Write Register Functionality")
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

# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #2 from Week 2

# Class for bank users created
class User:
    def __init__(name, pin, balance):
        self.name = name
        self.pin = pin
        self.balence = balance


# Creating starting values
new_user = User("empty", "empty", "empty")
registered_users = []
login_boolean = True
check_passed = False
current_user = ""
# Helper functions created


# I needed it often and this requires less typing
def print_empty_line():
    print("")


# I needed this often and this makes it easier to use and reduces lines of code
def automated_teller_machine_print():
    print_empty_line()
    print("          === Automated Teller Machine ===          ")


# Important functions created

# Handles the registration of new users
def register():
    automated_teller_machine_print()
    name = input("Enter name to register: ")
    pin = input("Enter PIN: ")
    balance = 0
    global new_user
    new_user = User(name, pin, balance)
    print(new_user.name +
          " has been registered with a starting balance of $" + str(new_user.balance))


# Handles the login for registered users
def login():
    print_empty_line()
    print("LOGIN")
    tmp_name = input("Enter name: ")
    tmp_pin = input("Enter PIN: ")
    global current_user
    current_user = check_login(tmp_name, tmp_pin)


# Checks if the user object with the name and pin provided exists or not
def check_login(tmp_name, tmp_pin):
    print_empty_line()
    for x in registered_users:
        if x.name.lower() == tmp_name.lower() and x.pin == tmp_pin:
            print("Login Successful!")
            global check_passed
            check_passed = True
            global login_boolean
            login_boolean = False
            return x
    if check_passed == False:
        print("Invalid Credentials")
        return tmp_name


def atm_menu(user_object):
    automated_teller_machine_print()
    print("User: " + user_object.name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    option = input("Choose an option: ")


# The program actually beings user interaction!
register()
while login_boolean:
    login()
while check_passed:
    atm_menu(current_user)

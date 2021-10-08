# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #2 from Week 2

from banking_pkg import account


# Class for bank users created
class User:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance


# Creating starting values
new_user = ""
registered_users = []
login_boolean = True
check_passed = False
current_user = ""
leave_menu = False
# Helper functions created


# I needed it often and this requires less typing
def print_empty_line():
    print("")


# I needed this often and this makes it easier to use and reduces lines of code
def automated_teller_machine_print():
    print_empty_line()
    print("          === Automated Teller Machine ===          ")


# Important functions created

# Checks the account pin to pass a required registration check
def pin_check():
    pin_check_passed = False
    while pin_check_passed == False:
        pin = input("Enter PIN: ")
        if ((len(pin)) > 4) and pin.isnumeric():
            print("PIN contains more than 4 numbers")
            print("PIN must contain 4 numbers")
        elif len(pin) < 4 and pin.isnumeric():
            print("PIN contains less than 4 numbers")
            print("PIN must contain 4 numbers")
        elif not pin.isnumeric():
            print("PIN must contain 4 numbers")
        else:
            pin_check_passed == True
            return pin
            # Checks name to pass certain requirements for registration


def name_check():
    name_check_passed = False
    while name_check_passed == False:
        name = input("Enter name to register: ")
        if len(name) < 10 and len(name) > 1:
            name_check_passed = True
            return name
        elif len(name) == 0:
            print("You must enter a name.")
        else:
            print("Valid names are between 1 to 10 Characters long")


# Handles the registration of new users
def register():
    automated_teller_machine_print()
    name = name_check()
    pin = pin_check()
    balance = 0
    global new_user
    new_user = User(name, pin, balance)
    registered_users.append(new_user)
    print(new_user.name + " has been registered with a starting balance of $" +
          str(new_user.balance))


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
    if int(option) == 1 or str(option.lower()) == "balance":
        print("Your current balance is: " +
              str(account.show_balance(user_object)))
    elif int(option) == 2 or str(option.lower()) == "deposit":
        tmp_account_change = account.deposit(user_object)
        user_object.balance = tmp_account_change
        print("Your current balance is now: " +
              str(account.show_balance(user_object)))
    elif int(option) == 3 or str(option.lower()) == "withdraw":
        tmp_account_change = account.withdraw(user_object)
        if "float" in str(type(tmp_account_change)):
            user_object.balance = tmp_account_change
            print("Your current balance is now: " +
                  str(account.show_balance(user_object)))
    elif int(option) == 4 or str(option.lower()) == "logout":
        account.logout(user_object)
        global leave_menu
        leave_menu = True
    else:
        print("Invaild option please try again")


# The program actually beings user interaction!
register()
while login_boolean:
    login()
while check_passed == True and leave_menu == False:
    atm_menu(current_user)

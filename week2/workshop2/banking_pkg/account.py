# Name: Ola B.
# Email: code@olab.dev
# Part of Workshop #2 from Week 2

# This function should display the account balance of the logged-in user
def show_balance(user):
    return float(user.balance)


# This function should allow the logged-in user to make a deposit
def deposit(user):
    modifier = float(input("Enter amount to deposit: "))
    return user.balance + modifier


# This function should allow the logged-in user to make a withdrawl if enough funds exist
def withdraw(user):
    modifier = float(input("Enter amount to withdraw: "))
    if float(user.balance) <= 0.0 or (float(user.balance) - modifier) < 0.0:
        print("Not enough funds to withdraw from...")
        return "no change"
    else:
        return float(user.balance - modifier)


# This function will log the user out of their account
def logout(user):
    print("Goodbye " + str(user.name) + "!")

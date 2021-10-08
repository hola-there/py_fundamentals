# Name: Ola B.
# Email: code@olab.dev
# Part of Workshop #2 from Week 2


def show_balance(user):
    return float(user.balance)


def deposit(user):
    modifier = float(input("Enter amount to deposit: "))
    return user.balance + modifier


def withdraw(user):
    modifier = float(input("Enter amount to withdraw: "))
    if user.balance <= 0 or (user.balance - modifier) < 0:
        print("Not enough funds to withdraw from...")
    else:
        return user.balance - modifier


def logout(user):
    print("Goodbye" + str(user.name) + "!")

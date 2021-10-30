# Name: Ola B.
# Email: code@olab.dev
# Exercise 3 of Week 4

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Instance method; only change the instance; not the class
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

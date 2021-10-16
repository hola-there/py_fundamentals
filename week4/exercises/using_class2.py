# Name: Ola B.
# Email: code@olab.dev
# Exercise 2 of Week 4

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Instance method; only change the instance; not the class
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
# using an instance method on a instance of a class
user1.change_password("bestpassword")

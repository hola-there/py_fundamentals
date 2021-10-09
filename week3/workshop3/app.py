# Name: Ola B.
# Email: code@olab.dev
# Main program for Workshop #3 from Week 3

from donations_pkg.homepage import show_homepage


# Decalring variables
database = {"admin", "password123"}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)

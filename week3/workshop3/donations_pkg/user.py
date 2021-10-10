# Name: Ola B.
# Email: code@olab.dev
# Part of Workshop #3 from Week 3


#
def login(database_passed, username_passed, password_passed):
    # isinstance source: https://docs.python.org/3/library/functions.html#isinstance
    if isinstance(database_passed, dict) and isinstance(username_passed, str) and isinstance(password_passed, str):
        for user_passed, passed_pass in database_passed.items():
            if user_passed == username_passed and passed_pass == password_passed:
                print("\n        === Welcome to DonateMe! ===          ")
                return username_passed
            elif user_passed == username_passed:
                print(
                    username_passed, "exists, but the password is incorrect. Please try again...")
                return ""
            else:
                print(
                    "Password & Username does not exist. If you'd like you should register an account")
                return ""

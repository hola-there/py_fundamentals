# Name: Ola B.
# Email: code@olab.dev
# Part of Workshop #3 from Week 3


# Ensures that the correct datatype is passed
def login(database_passed, username_passed, password_passed):
    # isinstance source: https://docs.python.org/3/library/functions.html#isinstance
    if isinstance(database_passed, dict) and isinstance(username_passed, str) and isinstance(password_passed, str):
        for user_passed, passed_pass in database_passed.items():
            if user_passed.lower() == username_passed.lower() and passed_pass == password_passed:
                print("\n        === Welcome to DonateMe! ===          ")
                return user_passed
            elif user_passed.lower() == username_passed.lower():
                print(
                    username_passed, "exists, but the password is incorrect. Please try again...")
                return ""
        print("Password & Username does not exist. Please register an account")
        return ""
    else:
        print("Incorrect data type passed; please try again")
        return ""


def register(database_passed, username_passed, password_passed):
    # isinstance source: https://docs.python.org/3/library/functions.html#isinstance
    if isinstance(database_passed, dict) and isinstance(username_passed, str):
        if username_passed[0].isnumeric():
            print(
                "The first character of the username must be a letter. Please try again...")
            return ""
        elif username_passed.isalnum() is not True:
            print(
                "The username must not contain special characters; only letters and numbers")
            return ""
        elif username_passed.lower() in database_passed.keys():
            print("Username already registered.")
            return ""
        else:
            if len(username_passed) > 10 and len(password_passed) < 5:
                print("Username must be less than 10 characters")
                print("Password must be more than 5 characters")
                print("Please try to register again")
            else:
                print("Successfully Registered:", username_passed)
                return username_passed
    else:
        print("Incorrect data type passed; please try again")
        return ""

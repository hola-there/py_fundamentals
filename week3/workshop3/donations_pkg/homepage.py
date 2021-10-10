# Name: Ola B.
# Email: code@olab.dev
# Part of Workshop #3 from Week 3

# I needed it often and this requires less typing
def print_empty_line():
    print("")


# I needed this often and this makes it easier to use and reduces lines of code
def donate_me_homepage_print():
    print_empty_line()
    print("          === DonateMe Homepage ===          ")


# Printing out the homepage
def show_homepage():
    donate_me_homepage_print()
    print("------------------------------------------")
    print("| 1.    Login      | 2.  Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate     | 4.  Show Donations  |")
    print("------------------------------------------")
    print("|                 5.  Exit               |")
    print("------------------------------------------")


def donate(authorized_user_passed):
    donation_amt = float(input("Enter amount to donate: "))
    donation = str(authorized_user_passed) + " donated $" + str(donation_amt)
    print("Thank you for your donation!")
    return donation


def show_donations(donations_passed):
    print("\n--- All Donations ---")
    if len(donations_passed) == 0:
        print("Currently, there are no donations.")
    else:
        for x in donations_passed:
            print(x)

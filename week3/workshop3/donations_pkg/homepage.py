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
    donation_amt = input("Enter amount to donate: ")
    if donation_amt.isnumeric():
        if float(donation_amt) <= 0:
            return "Please enter a donation amount greater than 0"
        else:
            donation = str(authorized_user_passed) + \
                " donated $" + str(donation_amt)
            print("Thank you for your donation!")
            return donation
    else:
        return "Please enter a valid donation amount"


def show_donations(donations_passed):
    print("\n--- All Donations ---")
    if len(donations_passed) == 0:
        print("Currently, there are no donations.")
    else:
        total_donation = 0.0
        for x in donations_passed:
            print(x)
            location_of_money_sign = x.find('$')
            float_from_donation = x[(location_of_money_sign + 1):]
            total_donation += float(float_from_donation)
        print("Donation Total: $", total_donation)

# Name: Ola B.
# Email: code@olab.dev
# Challenge 3 of Week 3

# Declarations
continue_collecting_snowfall_records = True
inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


# Going to print out total snowfall from a passed dictionary
def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)


# Will determine if a day passed is a valid day or not
def check_days_in_a_week(day_passed):
    days_in_a_week = ("monday", "tuesday", "wednesday", "thursday", "friday")
    return day_passed.lower() in days_in_a_week


# Will attempt to record the inches of snow if proper input is passed
def record_inches(day_passed, dict_passed, update):
    try_to_get_record = True
    while try_to_get_record:
        if update:
            num_of_inches = input(
                "Update " + str(day_passed) + " to how many inches?: ")
        else:
            num_of_inches = input(
                "How many inches fell on " + str(day_passed) + "?: ")
        if num_of_inches.isnumeric():
            dict_passed[str(day_passed)] = int(num_of_inches)
            try_to_get_record = False
        else:
            print(
                "Invalid option for inches that fell has been passed. Please pass a number")

# Maybe a cool thing to finish another day: sort by day of week or by record snowfall num
# def sort_records(dict_passed):


# Iterate through the dictionary in order to list all entries
def print_current_records(dict_passed):
    for day, record in dict_passed.items():
        print(record, " inches on ", day)


# Updates a preexisting key-value pair
def update_record(day_passed, dict_passed):
    record_inches(day_passed, dict_passed, True)
    print(str(day_passed) + " has been updated to " +
          str(dict_passed[str(day_passed)]) + " inches")


# Going to list all key-value pairs or append or modify a key-value pair in a passed dictionary
def new_snowfall_record(dict_to_pass):
    day_isnt_valid = True
    while day_isnt_valid:
        day = input("Which day was the snowfall recorded?: ")
        if day.lower() not in dict_to_pass.keys() and check_days_in_a_week(day):
            record_inches(day, dict_to_pass, False)
            day_isnt_valid = False
        elif day.lower == "q" or day.lower() == "quit":
            print("Exiting now...")
            day_isnt_valid = False
            global continue_collecting_snowfall_records
            continue_collecting_snowfall_records = False
        elif day.lower == "l" or day.lower() == "list":
            print("Current Records are: ")
            print_current_records(dict_to_pass)
        elif day.lower == "u" or day.lower() == "update":
            update_day = input(
                "Which day do you want to update recorded snowfall?: ")
            if check_days_in_a_week(update_day):
                print("You may now update the record for: " + str(update_day))
                update_record(update_day, dict_to_pass)
        elif check_days_in_a_week(day) == False:
            print("Please enter a valid day or enter 'q' to quit.")
        else:
            print("The day: " + str(day) +
                  ". Has been recored already. Please try again or enter 'list' to view current records or enter 'update' to update current records")


while continue_collecting_snowfall_records:
    print_total_snowfall(inches_snow)
    choice = input(
        "Would you like to add a new snowfall record?\n  1) Yes\n  2) Quit\n Your Choice: ")
    if (choice.lower() == "yes" or choice.lower() == "y") or (choice.isnumeric() and int(choice) == 1):
        new_snowfall_record(inches_snow)
    elif (choice.lower() == "quit" or choice.lower() == "q") or (choice.isnumeric() and int(choice) == 2):
        print("Exiting now...")
        continue_collecting_snowfall_records = False
    else:
        print("Your choice is not valid; please try again...")

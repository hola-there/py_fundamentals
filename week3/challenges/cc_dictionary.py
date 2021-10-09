# Name: Ola B.
# Email: code@olab.dev
# Challenge 2 of Week 3

# Declarations
inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)


def new_snowfall_record(dict_to_pass):
    new_thursday_record = input("How many inches of snow fell on Thursday?: ")
    if new_thursday_record.isnumeric():
        dict_to_pass["Thursday"] = int(new_thursday_record)
        #day = input("Which day was the snowfall recorded?: ")
        #num_of_inches = input("How many inches fell?: ")
        #inches_snow[str(day)] = int(num_of_inches)
        print_total_snowfall(dict_to_pass)


print_total_snowfall(inches_snow)
new_snowfall_record(inches_snow)

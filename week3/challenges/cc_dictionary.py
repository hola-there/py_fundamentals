# Name: Ola B.
# Email: code@olab.dev
# Challenge 2 of Week 3

inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def total_snowfall(dict_to_pass):
    num = 0
    for snow in dict_to_pass.values():
        num += snow
    print("Total snowfall inches:", num)


def new_snowfall_record(dict_to_pass):
    day = input("Which day was the snowfall recorded?: ")
    num_of_inches = input("How many inches fell?: ")
    inches_snow[str(day)] = int(num_of_inches)
    total_snowfall(dict_to_pass)


total_snowfall(inches_snow)
new_snowfall_record(inches_snow)

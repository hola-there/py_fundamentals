start = 0
step = 5
stop = 100 + step
for amount_loaded in range(start, stop, step):
    if amount_loaded == 25:
        print("1/4 of the way there")
    elif amount_loaded == 50:
        print("1/2 of the way there")
    elif amount_loaded == 75:
        print("3/4 of the way there")
    elif amount_loaded == 100:
        print("Loading complete!")
    else:
        print(amount_loaded)

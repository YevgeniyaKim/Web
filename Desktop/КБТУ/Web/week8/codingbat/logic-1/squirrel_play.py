def squirrel_play(temp, is_summer):
    upper = 90
    if is_summer:
        upper = 100
    return 60 <= temp <= upper

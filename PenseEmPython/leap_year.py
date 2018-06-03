# the year can be evenly divided by 4, is a leap year, unless:
# the year can be evenly divided by 100, is NOT a leap year, unless:
# the year can be evenly divided by 400. Then it is a leap year:

# test leap: 2000, 2400
# test not leap: 1800, 1900, 2100, 2200, 2300
# trial 1990 not leap


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


is_leap(1800)

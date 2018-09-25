#Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.

year = int(input("year=?"))

if year % 4 == 0 and year % 100 != 0:
    print("It is a leap year!")
elif year % 400 == 0:
    print("it is a leap year!")
else:
    print("It is not a leap year")

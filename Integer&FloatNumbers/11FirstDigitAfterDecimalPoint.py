#Given a positive real number, print its first digit to the right of the decimal point.

from math import floor

x = float(input("x= ?"))

y = round((x-floor(x)), 6)
print("number after decimal point is ", y)

print( "The first digit to the right of the decimal point is " , int((y*100) // 10))
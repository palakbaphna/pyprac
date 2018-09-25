#Given a positive real number, print its fractional part.


from math import floor

x = float(input("x = "))
y = floor(x)
print(round((x-y), 3))


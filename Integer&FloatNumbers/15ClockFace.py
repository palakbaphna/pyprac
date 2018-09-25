#Hour hand turned by α degrees since the midnight.
# Determine the angle by which minute hand turned since the start of the current hour.
#  Input and output in this problems are floating-point numbers.

from math import floor

alpha = float(input("angle by which hour hand moved since mid night = ?" ))

#beta = Angle by which minute hand moves since the start of the current hour

CurrentHour = round( (alpha/ 30), 3)

print(CurrentHour)

x = floor(CurrentHour)

print(x)

y = round((CurrentHour - x), 3)

print(y)

CurrentMinute = round( ( y * 60 ), 3 )

print(CurrentMinute )


Beta = round((CurrentMinute * 6), 2)

print("Angle by which minute hand moves since the start of the current hour, Beta = ", Beta)

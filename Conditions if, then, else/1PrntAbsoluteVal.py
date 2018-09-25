#for the given integer X determine its absolute value. If X>0 then the program should print the value X,
# otherwise it should print -X.
# This behavior can't be reached using the sequential program.
# The program should conditionally select the next step.

x = int(input())

if x > 0:
    print(x)
else:
    print(-x)

#Absolute value describes the distance of a number
# on the number line from 0 without considering which direction from zero the number lies.
# The absolute value of a number is never negative.

X = int(input("X = ?"))

if X > 0 :
    print("absolute value of %d is " %X , X)

else:
    print("absolute value of %d is " %X, -X)

exit()

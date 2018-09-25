#A cupcake costs A dollars and B cents.
# Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

from math import floor, ceil
A = int(input("A = ?"))
B = int(input(" B = ?"))

print("Cost of one cupcake is %d $ and %d cents" %(A, B))

totValForOne = round((A + (B/100)), 2)
print("Cost of one cupcake is ", totValForOne)

N = int(input("No of cupcakes,N = ?"))


x = round((N * (totValForOne)), 3)
print("Total cost of M number of cupcakes = ", x)

Dollars = floor(x)
cents = ceil((x- floor(x))*100)
#print(Dollars)
#print(cents)

print("Total cost of %d number of cupcakes = %d $ and %d cents" %(N, Dollars, cents))
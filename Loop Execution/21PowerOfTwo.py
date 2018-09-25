#The power of two. For a given integer N,
#find the greatest integer x where 2 power x is less than or equal to N. Print the exponent value and the result of the expression 2powerx.

N = int(input())

x = 0
while ((2**x) <= N ):
    x += 1

print("exponent value is:", (x-1), " and value of 2 power x is:", (2**(x-1)) )


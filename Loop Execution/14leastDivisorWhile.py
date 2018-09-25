#Given an integer not less than 2. Print its smallest integer divisor greater than 1.

N = int(input())
div = 2
while N%div != 0:
      div+= 1

print("least divisor for the given numner is:", div)


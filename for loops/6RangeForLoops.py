#Way 1 : find the arithmetic sum

n = 100
sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print("Sum of all the numbers from 1 to %d: %d" % (n,sum))


#Way 2 : we take input from user, all the sum lines get printed

print("Give a number, n to find the arithmatic sum of all the numbers from 1 to n, n = ")
n = int(input())
sum = 0
for n in range(1, n+1):
    sum = sum + n
    print("%d" %sum)

#Way 3 : We take input from user for number n, to add all the nos and all the sum lines get printed

print("Give a number, n to find the arithmatic sum of all the numbers from 1 to n, n = ")
n = int(input())
sum = 0
for number in range(1, n+1):
    sum = sum + number
    print("Sum of all the numbers from 1 to %d: %d" %(number, sum))


#Way 4
print("Give a number n to find the sum of all the numbers from 0 to n, printing all the statements one by one. n = ")
n = int(input())
sum = 0

for n in range(0, n+1):
    sum = n + sum
    print("The sum of numbers from 0 to %d = %d" %(n, sum))

#Way 5 Find the arithmetic sum of all the numbers from 3 to a given number

print("Hello, World")
print("Give a number n, to find the arithmatic sum of all the numbers from 3 to n. n = ")
n = int(input())
sum = 0

for n in  range(3, n+1):
    sum = n + sum

print("The sum of all the numbers from 3 to %d = %d " %(n, sum))

#Way 4 : List the numbers backwards in the range(30, 1)

print("List of all numbers backwards from 30 to 1 : " , list(range(30,0, -1)))

p = list(range(30, 0, -1))
print("List of all numbers backwards from 30 to 1: %s" %p)

#Way 5 Getting pythagorean triplets using for, if and range functions
from math import sqrt

n = int(input("maximal number?"))
for a in range(1, n+1):             #a!=0, b!= 0 , c != 0, a<b<c
    for b in range(a, n):
        cSquare = (a*a + b*b)
        c = int(sqrt(cSquare))
        if ((cSquare) - c*c) == 0:
            print("%d, %d, %d" %(a,b,c))

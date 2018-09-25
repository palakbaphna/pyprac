#use of the while loop to determine the number of digits of an integer n:


n = int(input())
length = 0
while n > 0:
    n =  n//10
    length = length + 1
print("number of digits in the given number n =" , length)

#On each iteration we cut the last digit of the number using
# integer division by 10 (n //= 10). In the variable length we count how many times we did that.
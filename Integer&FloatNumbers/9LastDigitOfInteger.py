#Given an integer number, print its last digit.

x  =  int(input("x =" ))

if x/10 == 0:
    print("last digit = 0")
elif x/10!= 0:
    print("Last digit of the given number = %d" %(x%10))
exit()

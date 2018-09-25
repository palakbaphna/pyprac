#For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

#WRONG CODING
#N = int(input("N =?"))
#i = 0
#while i <= N:
#    i += 1
#   if (i ** 2) <= N:
#        print(i ** 2)
#else:
#        print(" Square of %d is greater than %d" %(i, N))


N = int(input())
i = 1
while i*i <= N:
    print(i ** 2)
    i += 1
else:
    print("square of %d is greater than %d" %(i, N))


#N= 30
#i = 1
# 1*1= 1< 30, print 1, i =2
#2*2= 4< 30, print 4, i =3
#3*3= 9< 30, print 9, i =4
#4*4= 16< 30, print 16, i =5
#5*5= 25< 30, print 25, i =6
#6*6= 36> 30 FALSE While condition expression
#exits while loop
#executes else statement
#Square of 6 is greater than 30
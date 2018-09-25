#If during the execution of the loop Python interpreter encounters break, it immediately stops the loop execution and exits out of it.
# In this case, the else: branch is not executed. So, break is used to abort the loop execution during the middle of any iteration.

#a program that reads numbers and sums it until the total gets greater or equal to 21.
# The input sequence ends with 0 for the program to be able to stop even if the total sum of all numbers is less than 21.

tot_sum = 0
a = int(input())

while a != 0:
    tot_sum += a
    #print(tot_sum)

    if tot_sum >= 21:
        print("tot_sum is" , tot_sum)
        break
    a =int(input())

else:
    print("tot_sum is less than 21 and is equal to", tot_sum)
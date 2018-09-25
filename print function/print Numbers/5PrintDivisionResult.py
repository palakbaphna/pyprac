#N students take K apples and distribute them among each other evenly. The remaining (the undivisible)
# part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above.


n = int(input(" number of student, n = "))
k = int(input("number of apples, k = "))

print("Numbers of apple evenly distributed among n number of students = ", k//n) #example of integer division

print("Number of undivisible apples = ", k % n)  #example of getting remainder


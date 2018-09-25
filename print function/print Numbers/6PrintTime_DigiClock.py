#Given the integer N - the number of minutes that is passed since midnight -
# how many hours and minutes are displayed on the 24h digital clock?
#The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 59).

n = int(input("Number of minutes that have passed since midnight?"))

h = n//60
m = n%60
#print("hours dispalyed on the digital Clock = ", n//60)

#print("minutes displayed on the digital clock = ", n % 60)
print ("Digital clock reads %d:%d " %(h, m))
print("Digital clock reads %d:%d " %(n//60, n%60))




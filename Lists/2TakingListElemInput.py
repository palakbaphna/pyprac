

a = [0]*int(input("enter the number of elements:"))
# a is defined as an empty list and multiplying it with a number, taking input, we redefine its length at the same time
for i in range(len(a)): # if len is 3, i gets in range 0,1,2
    a[i] = int(input())# as len of list is already defined, it will take only those many inputs
print(a * 3) # all the elements gets repeated 3 times

print(a[1] * 3)

print(a[1] - 2)


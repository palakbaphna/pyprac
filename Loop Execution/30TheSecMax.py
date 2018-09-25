#Statement: The sequence consists of distinct positive integer numbers and ends with the number 0.
# Determine the value of the second largest element in this sequence.
#  It is guaranteed that the sequence has at least two elements.

a = []
n = int(input("Enter number of elements:"))

for n in range(1, n+1):
    num = int(input("Enter the numbers:"))
    a.append(num)
a.sort()

print("Second largest number is:", a[n-2])
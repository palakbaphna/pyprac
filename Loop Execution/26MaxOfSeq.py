#Statement: A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.

#######USING max() and min() functions
lst = []
num = int(input("How many numbers: "))

for n in range(num):
    numbers = int(input("Enter number: "))
    lst.append(numbers)

print("Maximum element in the list is: ", max(lst), "\nMinimum element in the list is:",  min(lst))


######################USING FOR LOOP
a = [3, 2, 1, 0]
max = 0
for i in a:
    if i > max:
        max = i
print(max)


##############USING WHILE LOOP
max = 0
while True:
    seq = int(input("Enter number: "))
    if seq > max:
        max = seq  #if we use max==seq, it will assign last value of seq regardless of anything else
    if seq == 0:
        break
print(max)

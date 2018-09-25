#STATEMENT: A sequence consists of integer numbers and ends with the number 0.
# Determine the index of the largest element of the sequence. If the highest
# element is not unique, print the index of the first of them.

max = 0
counter = 0

while True:
    seq = int(input("Enter number: "))
    if seq > max:
        max = seq
        counter+= 1
    if seq == 0:
        break
print(max, counter)

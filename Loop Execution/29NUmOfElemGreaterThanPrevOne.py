#STATEMENT: A sequence consists of integer numbers and ends with the number 0.
#Determine how many elements of this sequence are greater than their neighbours above.

seq = [1, 5, 2, 4, 3, 0]

counter = 0
a = 0
b = 1
while b < len(seq):
    if(seq[a] < seq[b]):
        counter+= 1
    a += 1
    b += 1

print(seq)
print(counter)
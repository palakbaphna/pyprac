#Statement: Determine the average of all elements of the sequence ending with the number 0.

seq = int(input("enter number: "))

sum = seq
counter = 1
avg_seq = (sum/counter)
while True:
    seq = int(input("enter number: "))
    if seq == 0:
        break
    #print(seq)
    counter+= 1
    #print(counter)
    sum = sum + seq
    #print(sum)
    avg_seq = sum/counter
    #print(avg_seq)

print(sum/counter)
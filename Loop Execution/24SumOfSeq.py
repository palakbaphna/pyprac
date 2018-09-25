#Statement:Determine the sum of all elements in the sequence, ending with the number 0.



seq = int(input("enter numbers: "))
sum = seq
while seq > 0:
    seq = int(input("enter number: "))
    sum+= seq
    if seq == 0:
        break
print(sum)
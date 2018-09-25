#Given a sequence of non-negative integers, where each number is written in a separate line.
#Determine the length of the sequence, where the sequence ends when the integer is equal to 0.
#Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted.


seq =  (2, 3, 5, 8, 9, 0, 4, 7)
#print(seq)
print(" 2 \n 3 \n 5 \n 8 \n 9 \n 0 \n 4 \n 7")
len = 0
for i in seq:
    if i > 0:
        len+= 1
    else:
        break
print("len = ",len)
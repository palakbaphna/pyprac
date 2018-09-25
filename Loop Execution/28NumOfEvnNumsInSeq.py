#STATEMENT: Determine the number of even elements in the sequence ending with the number 0.


counter = 0
while True:
    seq = int(input("enter number: "))
    if seq % 2 == 0 and seq!= 0:
        counter+= 1
    if seq == 0:
        break
print("There are", counter, " even numbers in the given sequence")


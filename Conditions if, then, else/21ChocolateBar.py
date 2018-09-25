#Chocolate bar has the form of a rectangle divided into n×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern.
# Determine whether it is possible to split it so that one of the parts will have exactly k squares.

n = int(input("n =?"))

m = int(input("m =?"))

k = int(input("k =?"))

if n > m :
    if k == n*(m-1):
        print("yes")
    else:
        print("No")
elif n < m: 
    if k == m*(n-1):
        print("yes")
else:
    print("No")
exit()

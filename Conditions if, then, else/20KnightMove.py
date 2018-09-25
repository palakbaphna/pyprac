#Chess knight moves like the letter L.
# It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally.
# Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

r = int(input("r =?"))
if r <1 or r >8 :
    print("Invalid")
    exit()
c = int(input("c = ?"))
if c <1 or c >8 :
    print("Invalid")
    exit()

R = int(input("R = ?"))
if R <1 or R >8 :
    print("Invalid")
    exit()
C = int(input("C = ?"))
if C <1 or C >8 :
    print("Invalid")
    exit()

if (R == r-2) and ((C==c-1) or (C== c+1)):
    print("Yes")

elif(R == r-1) and ((C==c-2) or (C== c+2)):
    print("YEs")

elif(R == r+2) and ((C==c-1) or (C== c+1)):
    print("YES")

elif(R == r+1) and ((C==c-2) or (C== c+2)):
    print("YES")

else:
    print("No")
exit()

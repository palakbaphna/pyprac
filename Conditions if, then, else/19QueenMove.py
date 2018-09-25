#Chess queen moves horizontally, vertically or diagonally to any number of cells.
# Given two different cells of the chessboard, determine whether a queen can go
# from the first cell to the second in one move.

r = int(input("r =?"))
if r<1 or r >8:
    print("invalid")
    exit()

c = int(input("c =?"))
if c<1 or c >8:
    print("invalid")
    exit()

R = int(input("R =?"))
if R <1 or R>8:
    print("Invalid")
    exit()

C = int(input("C =?"))
if C<1 or C>8:
    print("Invalid")
    exit()



if R==r and ( C<=8 or C>=1):
    print("YES")
elif C==c and (R <=8 or R >=1):
    print("YES")
elif (R>r and C> c):
    if (R-r ==C-c):
        print("YES")
    else:
        print("NO")
elif(R>r and C<c):
    if(R-r == c-C):
        print("YES")
    else:
        print("NO")
elif(R<r and C>c):
    if(r-R == C-c):
        print("YES")
    else:
        print("NO")
elif(R<r and C<c):
    if(r-R == c-C):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
exit()
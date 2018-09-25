#In chess, the bishop moves diagonally, any number of squares.
# Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

r = int(input())
if r >8 or r < 1 :
    print("Invalid")
    exit()

c = int(input())
if c >8 or c < 1 :
    print("Invalid")
    exit()

R = int(input())
if R >8 or R < 1 :
    print("Invalid")
    exit()

C = int(input())
if C >8 or C < 1 :
    print("Invalid")
    exit()


if (R >r and C >c):
    if (R-r) == (C -c):
        print("Yes")
    else:
        print("No")
elif (R>r and C<c):
    if (R-r) == (c -C):
        print("Yes")
    else:
        print("No")
elif(R<r and C <c):
    if (r-R == c-C):
        print("Yes")
    else:
        print("No")
elif (R <r and C >c):
    if (r -R == C-c):
        print("Yes")
    else:
        print("No")
else:
    print("No")
exit()

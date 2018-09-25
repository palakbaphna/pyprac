#Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard,
# determine whether a king can go from the first cell to the second in one move.

r = int(input("Row, r =?"))
if ( (r > 8) or (r <1)):
    print("Invalid entry!!")

c = int(input("Column, c = ?"))
if ( (c > 8) or (c <1)):
    print("Invalid entry!!")

R = int(input("row, R =?"))
if ( (R > 8) or (R <1)):
    print("Invalid entry!!")

C = int(input("Column, C = ?"))
if ( (C > 8) or (C <1)):
    print("Invalid entry!!")

if R == r or R == (r+1) or R == (r-1):
    if C == (c+1) or C == (c-1) or C == c :
        print("Yes")
    else:
        print("NO")
else:
    print("NO")

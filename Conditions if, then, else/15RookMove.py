#Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
r = int(input("Row no.1 = ?"))
c = int(input("Column no.1 = ?"))

R = int(input("Row no.2 = ?"))
C = int(input("Column no.2 = ?"))

if (R == r and (C >=1 or C <=8)) or (C==c and (R >= 1 or R <= 8) ):
    print("Yes, its a valid move for Rook")
else:
    print("No, its not a valid move")
exit()



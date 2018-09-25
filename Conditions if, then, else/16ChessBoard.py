#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.

r = int(input("Row number of the first cell on Chessboard, r = ?"))
if ((r > 8) or (r < 1)):
    print("Invalid row number for a Chessboard!")
    exit()

c = int(input("The column number for the first cell on Chessboard, c = ?"))
if((c > 8) or (c <1)):
    print("Invalid column number for a Chessboard!")
    exit()

R = int(input("THe row number for the second cell on Chessboard, R = ?"))
if ((R > 8) or (R < 1)):
    print("Invalid row number for a Chessboard!")
    exit()

C = int(input("The column for the second cell on Chessboard, C = ?"))
if ((C > 8) or (C <1 )):
    print("Invalid column number for a Chessboard!")
    exit()

if ( ( r % 2 == 0) and ( (c % 2 == 0)) )or ( (r % 2 != 0) and (c % 2 != 0)):
    if ( ((R %2 == 0)and(C% 2 ==0)) or  (( R % 2 != 0)and(C %2 != 0)) ):
        print("YES, The two given cells has the SAME color.")
    else:
        print("NO, The two given cells are NOT the same color")

elif ( ((r % 2 == 0) and(c %2 != 0)) or ((r % 2 != 0) and (c% 2 ==0)) ):
    if ( ((R %2 == 0)and(C% 2 !=0)) or  (( R % 2 != 0)and(C %2 == 0)) ):
        print("YES, The two given cells has the SAME color.")
    else:
        print("NO, The two given cells are NOT the same color")
exit()


#One can write an else: statement after a loop body which is executed once after the end of the loop:

i = 0
while i <= 10:
    print( i )
    i += 1
else:
    print("loop ended, i = ",  i )
exit()
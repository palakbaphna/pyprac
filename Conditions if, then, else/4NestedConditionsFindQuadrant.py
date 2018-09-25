#Given the coordinates of the point on the plane, print its quadrant.


x = int(input("x = ?"))
y = int(input("y = ?"))

if x > 0:
    if y > 0:
        print("Co-ordinates belong to I quadrant")
    elif y < 0:
        print("Co-ordinates belong to IV quadrant")
    else: #y =0
        print("co-ordiantes lie on +x axis")
elif x < 0:
    if y > 0:
        print("Co-ordinates belong to II quadrant")
    elif y < 0:
        print("Co-ordinates belong to III quadrant")
    else: #y =0
        print("Co ordinates lie on -x axis")
else : # elif x==0:
    if y > 0:
        print("Co-ordinates lie on +y axis")
    elif y < 0:
        print("Co-ordinates lie on -y axis")
    else: #y =0
        print("Co ordinates lie at Origin")


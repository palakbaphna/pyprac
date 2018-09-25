
#Use of Slice function with for loop

colors = ["red"]
print(colors)
for i in colors:
    if i == "red":
        colors += ["black"]
        print(colors)
    if i == "black":
        colors += ["white"]
        print(colors)
print(colors)


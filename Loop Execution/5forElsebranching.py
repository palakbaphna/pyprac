#program reads 5 integers but stops right when the first negative integer is met.

#using for else loop

for i in range(5):
    i = int(input())
    if i < 0:
        print("Negative value of i met")
        break
else:
    print("No negative value of i were met")

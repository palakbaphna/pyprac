#Given the two integers, print the least of them.

a = int(input("a = ?"))
b = int(input("b = ?"))

if a < b:
    print("least of them is a = %s" %a)
elif b < a:
    print("least of them is b = %s" %b)

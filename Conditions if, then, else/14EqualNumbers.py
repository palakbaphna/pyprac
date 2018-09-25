#Given three integers, determine how many of them are equal to each other.
# The program must print one of these numbers: 3 (if all are the same),
# 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

a = int(input("a=?"))
b = int(input("b=?"))
c = int(input("c=?"))

if a == b == c:
    print(3)
elif (a == b != c) or (a != b == c) or (a == c != b):
    print(2)
elif a != b != c:
    print(0)

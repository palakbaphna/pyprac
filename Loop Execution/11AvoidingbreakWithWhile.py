#counting digits of a given number

n = int(input())
len = 0
while n != 0:
    len += 1
    n//= 10
print("length of the given digit", len)

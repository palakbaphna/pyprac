#counting the digits of a given integer

n = int(input())
len = 0

while True:
    len += 1
    n//=10
    if n==0:
        break
print("length of the given number", len)

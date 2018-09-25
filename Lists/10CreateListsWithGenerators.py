a = [0 for i in range(5)]

print(a)

#Create a list filled with the squares of the integers

n = int(input())

b = [i**2 for i in range(1, n+1)]
print(b)


# the list will consist of lines read from standard input
# first, you need to enter the number of elements of the list
# (this value will be used as an argument of the function range), second — that number of strings:

c = [int(input()) for i in range(int(input()))]
print(c)

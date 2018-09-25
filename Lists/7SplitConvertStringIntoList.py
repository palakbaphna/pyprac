string = "hello world how are you"
list = string.split(' ')
print(list)

#resulting list will always contain the list of strings and not the numbers

s = '1 2 3 4 5 6 7 8 9 0'
b = s.split()
print(b) #returns the list of the strings not integers


#to get the list of numbers, you have to convert the list items one by one to integers:

str = '2 3 4 5 6 8 9'
split_str = str.split()
for i in range(len(split_str)):
    split_str[i] = int(split_str[i])
print(split_str)

x = '192.168.0.1'.split('.')
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])


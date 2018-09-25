Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

print("the first element of the list Rainbow is:",Rainbow[0])

print("The true colors of a rainbow are:")
for i in range(len(Rainbow)):
    print(Rainbow[i])

#print all the elements in one line or one item per line. Here are two examples of that, using other forms of loop:

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] #1

print(a)

for i in range(len(a)):
    print(a[i])#2

for elem in a:
    print(elem, end = ' ') #3

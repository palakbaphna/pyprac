#the third parameter of the slice is similar to the third parameter of the function range():


s = 'abcdefghijklm'

print(s[0:11:2])

for i in range(0, 11, 2):
    print(i, s[i])



str = input("Enter the string:")

#str = "abcbabcbabcbabcabcabcbacbacbacbabacbacbbb"
ca = 0
cb = 0
cc = 0

for i in (str):
        if i == 'a':
            ca += 1
        elif i == 'b':
            cb += 1
        elif i == 'c':
            cc += 1
        else:
            exit

print(ca, cb, cc)

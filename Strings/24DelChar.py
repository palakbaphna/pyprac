#Given a string. Delete from it all the characters whose indices are divisible by 3.

s = input()
a = ""
for i in range(0, len(s)):
    if i % 3 != 0:
        #print('index =', i)
        a+=s[i]
        print('letter at index %d = %s' %(i,s[i]))
        #print(s[i])
        # s_new = s.replace("s[i]", "")
print(a)

        #print('new modified string is:', s_new)


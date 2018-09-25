#Given a string that may or may not contain the letter of interest.
# Print the index location of the second occurrence of the letter f.
# If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2.

s = input()

if s.count('f') == 1: #count() returns 1 if subsrting occurs once
    print("String contains the letter f only once, so the desired output is:", -1)

elif s.count('f') == 0: #returns 0 if substring not found
    print("String does not contain the letter f, so the desired output is:", -2)
elif s.count('f') > 1:
    i1 = s.find('f')
    #print("index of first occurrence of letter f:", i1)
    s2 = s[(i1+1):]
    #print(s2)
    #i2 = s2.find('f', i1 +1) <<<<< s2 = ortf o =0, r = 1, t = 2, f = 3, so slicing from 3+1, excludes the whole s2 substring and when it does not find f returns -1
    i2 = s.find('f', i1 + 1)
    print("the index location of the second occurrence of the letter f:", i2)


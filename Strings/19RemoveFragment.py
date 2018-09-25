#Given a string in which the letter h occurs at least twice.
# Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.

s = input()
i1 = s.find('h')
i2 = s.rfind('h')
print("index of first occurrence of letter h:",s.find('h'))
print("index of last occurrence of letter h:", s.rfind('h'))

#print(s[:i1])
#print(s[(i2+1):])
s_cancatenated = s[:i1] + s[(i2+1):]
print("required cancatenated string :", s_cancatenated)
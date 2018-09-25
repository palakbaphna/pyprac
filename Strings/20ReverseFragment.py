#Given a string in which the letter h occurs at least two times,
# reverse the sequence of characters enclosed between the first and last appearances.


s = input()
i1 = s.find('h')
print(s.find('h'))

i2 = s.rfind('h')
print(s.rfind('h'))

sh = s[i1:(i2+1)]
new_s = s[:i1] + sh[::-1] + s[(i2+1):]
print(new_s)
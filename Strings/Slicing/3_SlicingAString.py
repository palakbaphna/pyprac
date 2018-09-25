#A substring of a string is called a slice. Selecting a slice is similar to selecting a character:


singers = "Peter, Paul, and Mary" #A string named singers created

print(singers[0:5]) #0:5 returns p is the zeroth character, e =1, t=2, e=3, r=4..and none from 5th character

print(singers[5:8]) #space between comma and P (for Paul here) is also considered as a character of this string

print(singers[3:10])

print(singers[8:12]) #space in a string is counted

print(singers[7:11]) #it will give name Paul only, as P is the 7th character and l is the 11 the character

print(singers[10:14])

#to get the name Mary
print(singers[17:21])

#to get the whole string
print(singers[:])
print(singers[0:21])

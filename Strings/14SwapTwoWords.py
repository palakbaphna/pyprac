#Given a string consisting of exactly two words separated by a space.
# Print a new string with the first and second word positions swapped (the second word is printed first).
#This task should not use loops and if.

s = str(input())

New_s = s.split( ' ')
print(New_s)

New_s1 = New_s[0]
print(New_s1)

New_s2 = New_s[1]
print(New_s2)

swapped_s = New_s2 + ' ' + New_s1
print(swapped_s)


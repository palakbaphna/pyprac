#Check if the given string is a Palindrome

s = input()

s_modified  = s.replace(' ', '').lower()

print(s_modified)

s_rev = s_modified[ : : -1]

if s_modified == s_rev :
    print("given string is a palindrome")
else:
    print("given string is NOT a palindrome")

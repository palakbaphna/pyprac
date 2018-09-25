#Any slice of a string creates a new string and never modifies the original one. In Python strings are
# immutable, i.e they can not be changed as the objects.
# You can only assign the variable to the new string, but the old one stays in memory.

#In fact in Python there is no variables. There are only the names that are associated with any objects.
#You can first associate a name with one object, and then — with another. Can several names be associated
#with one and the same object.

s = "Hello"
t = s  # s and t point to the same string
print(s, t)

t = s[1:3] # now t points to the new string 'el'
print(s) # prints 'Hello' as s is not changed
print(t)
#the method join is used; this method has one parameter: a list of strings.
# It returns the string obtained by concatenation of the elements given,
# and the separator is inserted between the elements of the list;
# this separator is equal to the string on which is the method applied

a = ['red', 'green', 'blue']

print(' '.join(a))

print(''.join(a))

print('***'.join(a))

#b = [1, 2, 3, 4, 5, 6]

#print(''.join(b)) # gives type error, because join can cancatenate only strings

#so to join list with numbers or integers, we need to USE THE GENERATORS

b = [1, 2, 3]

print('.'.join([str(i) for i in b]))



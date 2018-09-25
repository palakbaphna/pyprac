#Given a string that may or may not contain a letter of interest.
# Print the index location of the first and last appearance of f.
# If the letter f occurs only once, then output its index.
# If the letter f does not occur, then do not print anything.
#Don't use loops in this task.

string = 'find me the flower catalog'
#CASE 1
print("index location of the first appearance of f: ", string.find('f'))
#returns 0.. because it returns only the index of the FIRST occurrence of the letter f
print("index location of the last appearance of f: ", string.rfind('f'))

#CASE 2
s = input() #input a string
#print("Given string is:", s)
if s.count('f') == 0:
    print()
elif s.count('f') == 1:
    print("index location of the first appearance of f: ", s.find('f'))
elif s.count('f') > 1:
    print("index location of the first appearance of f: ", s.find('f'))
    print("index location of the last appearance of f: ", s.rfind('f'))



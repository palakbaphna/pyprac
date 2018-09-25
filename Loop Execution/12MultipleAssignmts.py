#In Python it is possible for a single assignment statement to change the value of several variables.
# multiple assignment changes the values of two variables simultaneously.

a, b = 0, 1

#exchange the values of two variables

#In older programming languages without the support of multiple assignment this can be done using the auxiliary variable:
a = 1
b = 2
tmp = a
a = b
b = tmp
print(a, b)

#In Python, the same swap can be written in one line:
#The left-hand side of "=" should have a comma-separated list of variable names. The right-hand side can be any expressions,
# separated by commas. The left-hand side and the right-hand side lists should be of equal length.
p, q = 5, 6
p, q = q, p
print(p, q)
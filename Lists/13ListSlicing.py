A = [1, 2, 3, 4, 5, 6, 7]

print(len(A))
A[ : : -2] = [10, 20, 30, 40] #0 for the beginning of the parent list, next zero signifies till the end of the parent list and -,minus signifies replacment shall start from the back of the parent list and 2 signifies the step


print(A)

print(len(A))

# The reason is, A[::-2] is a list of elements A[-1], A[-3], A[-5], A[-7], and that elements are assigned to 10, 20, 30, 40, respectively.
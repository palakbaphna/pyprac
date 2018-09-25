#unlike strings, are mutable objects: you can assign a list item to a new value. Moreover, it is possible to change entire slices

A =[1, 2, 3, 4, 5]

A[2:4] = [7, 8, 9]

print(A)

#Here we received a list [1, 2, 3, 4, 5], and then try to replace the two
#elements of the slice A[2:4] with a new list of three elements. The resulting list is as follows: [1, 2, 7, 8, 9, 5]
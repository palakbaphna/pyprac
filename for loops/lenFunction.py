#Example to find index of an element and element itself using range function with the length function, len()

print("Find the indices of all the elements and elements with in a given fibonacci series")

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

for i in range(len(fibonacci)):
     print(i, fibonacci[i])

totNumOfElements = len(fibonacci)
print("Number of elements in the given series = %s" %totNumOfElements)




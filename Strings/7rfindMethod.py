#the method rfind() returns the index of the last occurrence of the substring.


s = 'abracadabra'

print(s.find('b'))

print(s.rfind('b'))


#If you call find() with three arguments s.find(substring, left, right), the search is performed inside
#the slice s[left:right]. If you specify only two arguments, like s.find(substring, left), the search is
#performed in the slice s[left:], that is, starting with the character at index left to the end of
#the string. Method s.find(substring, left, right) returns the absolute index, relatively to the whole string s, and not to the slice.


m = 'my name is bond, james bond.'

print(m.find('bond'))

print(m.find('bond', 12)) #starts finding it only afer the character 12
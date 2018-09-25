#Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

s = input()

i1 = s.find('h')
i_last = s.rfind('h')

s_middle = s[(i1+1):i_last]
print(s_middle)

s_mid_replaced = s_middle.replace('h', 'H')
print(s_mid_replaced)

s_required = s[:(i1 +1)] + s_mid_replaced[:] + s[i_last:]
print("required string is:", s_required)




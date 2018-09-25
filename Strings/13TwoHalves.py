import math

s = input()

tot_letters = len(s)
if tot_letters % 2 == 0 and tot_letters >= 2 :

    print("given string s has even number of letters")
    print("no. of letters in given string s are %d" %tot_letters)

    N_s1 = N_s2 = int(tot_letters / 2)
    s1 = s[0:N_s1]

    print("substring1:", s1)

    s2 = s[N_s2:]
    print( "substring2", s2)

    cancatenated_str = s2 + s1
    print("CAncatenated String:",cancatenated_str)
elif tot_letters % 2 != 0 and tot_letters >= 2:
    print("given string s has odd number of letters")
    print("no. of letters in given string s are %d" % tot_letters)

    N_s1 = math.ceil(tot_letters / 2)
    print(N_s1)
    s1 = s[0:N_s1]

    print("substring1:", s1)

    N_s2 = int(tot_letters - N_s1)
    print(N_s2)
    s2 = s[-N_s2:]
    print("substring2", s2)

    cancatenated_str = s2 + s1
    print("CAncatenated String:",cancatenated_str)

elif tot_letters % 2 != 0 and tot_letters < 2:
    N_s1 = math.ceil(tot_letters / 2)
    print(N_s1)
    s1 = s[0:N_s1]

    print("substring1:", s1)

    N_s2 = int(tot_letters - N_s1)
    print(N_s2)
    s2 = s[1:]
    print("substring2: null")

    cancatenated_str = s2 + s1
    print("CAncatenated String:", cancatenated_str)
exit()

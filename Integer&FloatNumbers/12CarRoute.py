#A car can cover distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M.

N = int (input("N = ?"))

M = int(input("M = ?"))

from math import ceil


print("No. of days will it take to cover a route of length M kilometers is", ceil(M/N))

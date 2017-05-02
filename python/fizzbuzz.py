# author : kip-s
# 2017-05-02

import sys

for n in range(1, 32+1):
    if n % 3 == 0:
        print ("fizz", end="")
    if n % 5 == 0:
        print ("buzz", end="")
    elif n % 3 != 0:
        print (n, end="")
    print ()

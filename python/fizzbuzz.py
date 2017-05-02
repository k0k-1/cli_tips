# author : kip-s
# 2017-05-02

import sys

for n in range(1, 32+1):
    print (n)
    if n % 3 == 0:
        sys.stdout.write ("fizz")
    if n % 5 == 0:
        sys.stdout.write ("buzz")

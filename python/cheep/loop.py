import time

start = time.time()
L = 200000
total = 0
for i in range(L):
    for j in range(L):
        total += i*j
print (total)
t_time = time.time() - start
print (time, "[sec]")

import time
start = time.time()
loop = 10000
total = 0
for i in range(loop):
    for j in range(loop):
        total += i*j
print (total)
t_time = time.time() - start
print (t_time, "[sec]")

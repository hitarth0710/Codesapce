import time
import random

arr = [random.randint(0,10000) for i in range(10000000000)]
start = time.time()
arr.sort()
end = time.time()
print('Time taken to sort 100 elements: ', end-start)

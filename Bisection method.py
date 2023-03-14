import math
import timeit

def f(x):
    return x**3 - 2*x - 5

a = 2
b = 3
tolerance = 1e-6
max_iteration = 100

start_time = timeit.default_timer()

for i in range(max_iteration):
    c = (a + b) / 2
    if abs(f(c)) < tolerance:
        print(f'Root found at x={c:.6f}')
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c

elapsed_time = timeit.default_timer() - start_time

print(f"Time taken to execute the code: {elapsed_time:.6f} seconds")

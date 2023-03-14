import math
import matplotlib.pyplot as plt
import timeit

def f(x):
    return x**3 - 2*3 - 5

def df(x):
    return 3*x**2 - 2

x1 = 1
tolerance = 1e-6
max_iterations = 100

start_time = timeit.default_timer()

for i in range(max_iterations):
    fx = f(x1)
    dfx = df(x1)
    x2 = x1 - fx / dfx
    if abs(x2 - x1) < tolerance:
        print(f"Root found at x = {x2:.6f}")
        break
    else:
        x1 = x2

elapsed_time = timeit.default_timer() - start_time

print(f"Time taken to execute the code: {elapsed_time:.6f} seconds")

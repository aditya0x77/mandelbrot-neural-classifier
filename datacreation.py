import numpy as np
import pandas as pd


def escape_mandelbrot(x, y, max_itr):
    z = 0 + 0j
    c = complex(x,y)
    for i in range(max_itr):
        z = z**2 + c
        if abs(z) > 2:
            return i

    return max_itr

x_val = np.linspace(-2.5, 1, 1000)
y_val = np.linspace(-1.5, 1.5, 1000)
dataset = []
escape_time = 0
max_iterations = 1000
for x in x_val:
    for y in y_val:
        escape_time = escape_mandelbrot(x,y,max_iterations)
        dataset.append([x, y, escape_time])

dataset = np.array(dataset)
df = pd.DataFrame(dataset, columns=["x", "y", "esc"])
df.to_csv("dataset.csv", index = False)


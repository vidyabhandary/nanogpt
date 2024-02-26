# -*- coding: utf-8 -*-
"""AK1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oK11jab8rAsL2mH0SP3_txRtVHzB_ySa
"""

# Commented out IPython magic to ensure Python compatibility.
import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def f(x):
  return 3*x**2 - 4*x + 5

f(3.0)

xs = np.arange(-5, 5, 0.25)
xs

ys = f(xs)
ys

plt.plot(xs, ys)

h = 0.00000001
x = 2/3
(f(x + h) - f(x))/h

h = 0.000001
x = 2/3
(f(x + h) - f(x))/h

# les get more complex
a = 2.0
b = -3.0
c = 10.0
d = a*b + c
print(d)

h = 0.0001

# inputs
a = 2.0
b = -3.0
c = 10.0

# This is the expression that indicate the equation we are solving
d1 = a*b + c
c += h

# After adding h to c
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)























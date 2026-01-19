import math
import numpy as np

an = float(eval(input("Enter your angle multiple of radians: ")))
x1 = float(input("x1: "))
x2  = float(input("x1: "))

co = math.cos(an * math.pi)
si = math.sin(an * math.pi)

A = np.array([[co,-si],[si,co]])
x = np.array([[x1],[x2]])

y = A.dot(x);

print(y)

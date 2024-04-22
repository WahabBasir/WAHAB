import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 10)

y1 = x**2 - 10
y2 = x**3 + x - 100
y3 = x**10 - x**8 + x**2 - 8
y4 = x**4 + x**3 + x**2 + 1
y5 = x**2 + x + 10 / 2*x
y6 = np.sin(x) / 3*x
y7 = x**3 + 2*x**2 - 10*x + 3
y8 = np.cos(x) / 5*x
y9 = x**3 / 2*x - 10*x
y10 = x+2 * x+3 * x-4

plt.figure(figsize=(100, 100))

plt.plot(x, y1, label=r"f(x) = x**4 + 8", color='b')
plt.plot(x, y2, label=r"g(x) = x**3 + x - 100", color='g')
plt.plot(x, y3, label=r"h(x) = x**10 - x**8 + x**2 - 8", color='y')
plt.plot(x, y4, label=r"b(x) = x**4 + x**3 + x**2 + 1", color='m')
plt.plot(x, y5, label=r"c(x) = x**2 + x + 10 / 2*x", color='c')
plt.plot(x, y6, label=r"k(x) = np.sin(x) / 3*x", color='g')
plt.plot(x, y7, label=r"l(x) = x**3 + 2*x**2 - 10*x + 3", color='y')
plt.plot(x, y8, label=r"m(x) = np.cos(x) / 5*x", color='b')
plt.plot(x, y9, label=r"n(x) = x**3 / 2*x - 10*x", color='c')
plt.plot(x, y10, label=r"p(x) = x+2 * x+3 * x-4", color='m')

plt.axhline(y=0, color='r', linestyle='-', linewidth=2)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2)

plt.title("GRAPHS OF THE FOLLOWING EQUATIONS")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
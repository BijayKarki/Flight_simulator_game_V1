import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = (x - 2) * (x - 8)
y2 = (x - 2) * (x - 5) * (x - 8)

# graphical part

plt.grid(True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Polynomial functions")

plt.plot(x, y1, label = "y1", color ="red")
plt.plot(x, y2, label = "y2", color = 'blue')
plt.legend()
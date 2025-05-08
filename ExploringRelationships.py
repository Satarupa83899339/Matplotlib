# scatter_plot.py
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(6, 6))
plt.scatter(x, y)
plt.title('Random Scatter')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.tight_layout()
plt.show()

# line_plot.py
import numpy as np
import matplotlib.pyplot as plt

# Data: a sine wave
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o', linestyle='-')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.tight_layout()
plt.show()

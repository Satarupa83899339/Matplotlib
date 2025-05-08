# histogram.py
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 samples from a normal distribution
data = np.random.randn(1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30)
plt.title('Normal Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# bar_chart.py
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values     = [23,    17,    35,    29,    12]

plt.figure(figsize=(6, 4))
plt.bar(categories, values)
plt.title('Category Value Comparison')
plt.xlabel('Category')
plt.ylabel('Value')
plt.tight_layout()
plt.show()

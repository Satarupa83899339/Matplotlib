# pie_chart.py
import matplotlib.pyplot as plt

segments = [40, 25, 20, 15]
labels   = ['Segment A', 'Segment B', 'Segment C', 'Segment D']

plt.figure(figsize=(6, 6))
plt.pie(segments, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Segment Proportions')
plt.tight_layout()
plt.show()

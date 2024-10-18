import matplotlib.pyplot as plt

# Bar positions for the first set
x1 = [1, 2, 3, 4]
y1 = [2, 4, 5, 6]

# Bar positions for the second set (shifted slightly to the right)
x2 = [1, 2, 3,4]
y2 = [4, 6,4,11]

# Width of the bars
bar_width = 0.4

# First set of bars
plt.bar(x1, y1, width=bar_width, label='Set 1')

# Adjusting the second set's position by adding the width to avoid overlap
plt.bar([i + 0.4 for i in x2], y2, width=bar_width, label='Set 2')

# Adding labels and legend
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

# Show the plot
plt.show()

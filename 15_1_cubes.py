import matplotlib.pyplot as plt

# 15.1: Plot the first 5 cubic numbers;
# Then plot the first 5000 cubic numbers.

# Simple list of first 5 cube numbers
# x = [1, 2, 3, 4, 5]
# y = [1, 8, 27, 64, 125]
# plt.plot(x, y, linewidth=3)

# First 5000 cubes
x_val = list(range(1, 5001))
y_val = [x**3 for x in x_val]

plt.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Reds, edgecolor='none', s=20)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set sie of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
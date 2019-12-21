import matplotlib.pyplot as plt

# Demonstrating the plotting of points, with looping calculations to
# help with efficiently working on large sets of data.
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Colormap Gradient
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set title and label axes - adding style!
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
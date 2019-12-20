import matplotlib.pyplot as plt

# Adding labels and stuff to matplotlib
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set sie of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()

# A representation of the simplest sort of plot you can make using Matplotlib
# Plot a set of values and show it
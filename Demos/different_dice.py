import pygal

from die import Die
from hist_label_loop import labels_list

# What happens when we roll two different dice 50,000 times?
# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Rolling a D6 and D10 50,000 times."
hist.x_labels = labels_list(max_result - 1, 2)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D10', frequencies)
hist.render_to_file('d6_d10.svg')
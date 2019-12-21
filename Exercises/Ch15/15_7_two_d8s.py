import pygal

from die import Die
from hist_label_loop import labels_list

# 15.7 : Create a simulation showing what happens if you roll
# two D8s 1000 times. Increase number gradually as your computer can handle.

die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in list.
results = []
for roll_num in range(10000):
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

hist.title = "Rolling two D8s 10000 times."
hist.x_labels = labels_list(max_result - 1, 2)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D8 + D8', frequencies)
hist.render_to_file('d8_d8.svg')
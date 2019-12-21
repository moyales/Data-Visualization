import pygal

from die import Die
from hist_label_loop import labels_list

# 15.8 : Create a visualization for rolling three D6 dice.

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in list.
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Rolling three D6s 10000 times."
hist.x_labels = labels_list(max_result - 2, 3)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('Three D6s', frequencies)
hist.render_to_file('three_dice.svg')
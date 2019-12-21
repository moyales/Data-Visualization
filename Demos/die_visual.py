import pygal
from die import Die
from hist_label_loop import labels_list

# Create a D6. (6 is default value)
die = Die()

# Make some rolls, and store them in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
num_sides = die.num_sides
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 1000 times."
hist.x_labels = labels_list(num_sides, 1)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


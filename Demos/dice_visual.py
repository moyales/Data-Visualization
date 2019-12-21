import pygal
from die import Die
from hist_label_loop import labels_list

# Create two D6s
die_1 = Die()
die_2 = Die()

# Make some rolls, and store them in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6s 1000 times."
hist.x_labels = labels_list(max_result - 1, 2)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')


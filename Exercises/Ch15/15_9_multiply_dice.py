import pygal

from die import Die
from hist_label_loop import labels_list

# 15.9 : Simulate rolling two dice and show the distribution
# when the two dice rolls are multiplied together.

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(10000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for val in range(1, max_result + 1):
    freq = results.count(val)
    frequencies.append(freq)

hist = pygal.Bar()

hist.title = "Rolling two D6s and Multiplying the Results - 10000 Rolls"
hist.x_labels = labels_list(max_result, 1)
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 * D6', frequencies)
hist.render_to_file('d6_mult.svg')
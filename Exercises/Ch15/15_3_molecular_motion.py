import matplotlib.pyplot as plt

from random_walk import RandomWalk
# 15.3 : Modify rw_visual such that the scatter plot becomes a line instead
# Use 5000 points (default) instead of 50000 (for the love of god, please do.)

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))

    pt_numbers = list(range(rw.num_points))
    plt.plot(rw.x_val, rw.y_val, linewidth=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=50)

    # Remove the axes, so they don't distract us from the walk path.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
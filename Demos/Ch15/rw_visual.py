import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Let's have it such that a new random walk is continuously generated
# without the need to run the program again and again.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10,6))

    pt_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_val, rw.y_val, c=pt_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=10)

    # Remove the axes, so they don't distract us from the walk path.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
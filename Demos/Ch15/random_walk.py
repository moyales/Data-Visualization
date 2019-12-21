from random import choice

class RandomWalk():
    '''A class to generate random walks.'''

    def __init__(self, num_points=5000):
        '''Initialise attributes of a walk.'''
        self.num_points = num_points

        # All walks start at the origin (0,0).
        self.x_val = [0]
        self.y_val = [0]

    def get_step(self):
        '''
        Determine which direction and distance for each step, 
        then calculate the step.
        '''
        # Refactored method to de-clutter fill_walk
        direction = choice([1, -1])
        dist = choice([0, 1, 2, 3, 4])
        step = direction * dist

        return step

    def fill_walk(self):
        '''Calculate all the points in the walk.'''

        # Continue taking steps until the walk reaches the desired length.
        while len(self.x_val) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            # Do this for both x and y direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            # Once values are obtained, we append them to x_val and y_val.
            self.x_val.append(next_x)
            self.y_val.append(next_y)
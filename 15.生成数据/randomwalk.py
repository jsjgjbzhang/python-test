from random import choice


class RandomWalk():
    """docstring for RandomWalk"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        self.x_values = self.get_step()
        self.y_values = self.get_step()

    def get_step(self):
        tempValues = [0]
        while len(tempValues) < self.num_points:
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction * distance
            next_step = tempValues[-1] + step
            tempValues.append(next_step)
        return tempValues

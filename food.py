import random


class Food:
    """
    class used to define food position
    """
    def __init__(self, width, height, snake_block):
        self.x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    def position_x(self):
        """
        get position x
        :return: self.x
        """
        return self.x

    def position_y(self):
        """
        get position y
        :return: self.y
        """
        return self.y

    def is_ate(self, snake_x, snake_y):
        """
        method used to make snake eat food
        :param snake_x: int
        :param snake_y: int
        :return: bool
        """
        if snake_x == self.x and snake_y == self.y:
            return True

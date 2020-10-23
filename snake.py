class Snake:
    """
    Class used to snake move
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_new = 0
        self.y_new = 0
        self.snake_list = []
        self.snake_length = 1

    def move_to(self, direction):
        """
        Method used for move
        :param direction: str (left, right, up, down)
        """
        if direction == 'left':
            self.x_new = -10
            self.y_new = 0
        elif direction == 'right':
            self.x_new = 10
            self.y_new = 0
        elif direction == 'up':
            self.x_new = 0
            self.y_new = -10
        elif direction == 'down':
            self.x_new = 0
            self.y_new = 10

    def update_position(self):
        """
        method used to update snake position after a move
        """
        self.x += self.x_new
        self.y += self.y_new

    def is_out_of_window(self, width, height):
        """
        method used to make game over is snake is out of the window limit
        :param width: int
        :param height: int
        :return: bool
        """
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            return True

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

    def list(self):
        """
        get snake list
        :return: self.snake_list
        """
        return self.snake_list

    def eat_himself(self):
        """
        method used to make game over if snake is eating himself
        :return: bool
        """
        snake_head = list()
        snake_head.append(self.x)
        snake_head.append(self.y)
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
        for x in self.snake_list[:-1]:
            if x == snake_head:
                return True

    def grow_up(self):
        """
        method used to add 1 to snake length
        """
        self.snake_length += 1

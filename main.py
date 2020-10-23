import json

import pygame
from pygame.locals import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, QUIT

from food import Food
from snake import Snake


class Main:
    """
    class used for main game progression
    """

    def __init__(self):
        self.constant = dict()
        self.load_constant()
        self.window = pygame.display.set_mode((self.constant['win_width'],
                                               self.constant['win_height']))
        self.play()

    def load_constant(self):
        """
        method used to load constant and put data on self.constant
        """
        with open('constant.json') as file:
            self.constant = json.load(file)

    @staticmethod
    def color_tuple(color_list):
        """
        method used for format list color to tuple
        in order to use it in pygame.draw.rect
        :param color_list: list
        :return: tuple
        """
        r, g, b = color_list[0], color_list[1], color_list[2]
        return r, g, b

    def play(self):
        """
        method for main game progression
        """
        pygame.init()  # initialize pygame

        # instantiate snake object
        snake = Snake(self.constant['win_width'] / 2,
                      self.constant['win_height'] / 2)

        # instantiate food object
        food = Food(self.constant['win_width'],
                    self.constant['win_height'],
                    self.constant['snake_block'])
        clock = pygame.time.Clock()
        game_over = False

        # loop game
        while not game_over:

            # all event used for the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_over = True
                    elif event.key == K_LEFT:
                        snake.move_to('left')
                    elif event.key == K_RIGHT:
                        snake.move_to('right')
                    elif event.key == K_UP:
                        snake.move_to('up')
                    elif event.key == K_DOWN:
                        snake.move_to('down')

            # update snake position
            snake.update_position()

            # set blue background
            self.window.fill(self.color_tuple(self.constant['blue']))

            # display food element
            pygame.draw.rect(self.window,
                             self.color_tuple(self.constant['green']),
                             [food.position_x(),
                              food.position_y(),
                              self.constant['snake_block'],
                              self.constant['snake_block']])

            # game over is the snake is out of the window limit
            if snake.is_out_of_window(self.constant['win_width'],
                                      self.constant['win_height']):
                game_over = True

            # game over if the snake eat himself
            elif snake.eat_himself():
                game_over = True

            # snake grow up when eating food
            elif food.is_ate(snake.position_x(), snake.position_y()):
                food = Food(self.constant['win_width'],
                            self.constant['win_height'],
                            self.constant['snake_block'])
                snake.grow_up()

            # update snake displaying
            for x in snake.list():
                pygame.draw.rect(self.window,
                                 self.constant['black'],
                                 [x[0],
                                  x[1],
                                  self.constant['snake_block'],
                                  self.constant['snake_block']])

            # game updated
            pygame.display.update()

            # game speed
            clock.tick(self.constant['snake_speed'])

        pygame.quit()
        quit()

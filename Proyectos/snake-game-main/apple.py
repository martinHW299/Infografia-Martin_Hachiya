import arcade
import random


class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("./img/apple.png", center_x=random.randint(10, game.width-10), center_y=random.randint(10, game.height-10), scale=0.02)
        self.score = 1
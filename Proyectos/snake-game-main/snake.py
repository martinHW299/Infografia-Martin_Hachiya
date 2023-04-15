import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__("./images/snakehead.png", center_x=game.width//2, center_y=game.height//2, scale=0.05)
        self.width = 20
        self.height = 20
        self.center_x = game.width / 2
        self.center_y = game.height / 2
        self.color = arcade.color.WHITE
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0
        self.body = arcade.SpriteList()
        self.speed_counter = 0

    def move(self):
        new_body_part = arcade.Sprite(center_x=self.center_x, center_y=self.center_y)
        new_body_part.width = self.width
        new_body_part.height = self.height
        self.body.append(new_body_part)
        self.speed_counter += 1
        if self.speed_counter == 100:
            self.speed += 0.2
            self.speed_counter = 0
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        self.score += food.score
        food.kill()

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.width/2, self.color)
        self.body.reverse()
        for index, part in enumerate(self.body):
            arcade.draw_circle_filled(part.center_x, part.center_y, part.width/2, self.color if index%2!=0 else self.color)
        self.body.reverse()

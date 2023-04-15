import arcade
from snake import Snake
from apple import Apple

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="活力(La viborita)")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.apple = Apple(self)
        self.snake = Snake(self)
        self.is_game_ended = False
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()
        arcade.draw_text(f"Score: {self.snake.score}", 10, 20, arcade.color.WHITE, 14)
        if self.is_game_ended == True:
            arcade.pause(0.5)
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("GAME OVER", 250, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
            arcade.finish_render()

    def on_update(self, delta_time: float):
        if not self.is_game_ended:
            self.snake.move()
            if arcade.check_for_collision(self.snake, self.apple):
                self.snake.eat(self.apple)
                self.apple = Apple(self)
            if self.snake.center_x < 10 or self.snake.center_x > self.width-10 or self.snake.center_y < 10 or self.snake.center_y > self.height-10:
                self.is_game_ended = True
            for i in range(len(self.snake.body)-14, 0, -1):
                if arcade.check_for_collision(self.snake, self.snake.body[i]):
                    self.is_game_ended = True
    

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            if not self.snake.change_y:
                self.snake.change_x = 0
                self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            if not self.snake.change_y:
                self.snake.change_x = 0
                self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            if not self.snake.change_x:
                self.snake.change_x = 1
                self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            if not self.snake.change_x:
                self.snake.change_x = -1
                self.snake.change_y = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()
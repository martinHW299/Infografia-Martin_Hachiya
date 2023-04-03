import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Flor")

BACKGROUND_COLOR = arcade.color.BLACK
PETAL_COLOR = arcade.color.RED
CENTER_COLOR = arcade.color.YELLOW

petal_width = 200
petal_height = 300
petal_gap = 50

for i in range(4):
    angle = i * 90
    arcade.draw_ellipse_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, petal_width, petal_height,
                               PETAL_COLOR, angle, 128)

center_radius = 50
arcade.draw_circle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, center_radius, CENTER_COLOR)

arcade.finish_render()
arcade.run()




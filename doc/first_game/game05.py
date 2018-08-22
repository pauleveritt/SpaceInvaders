import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 50


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)
        self.ball_x = 300

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, 300, CIRCLE_RADIUS, arcade.color.BLACK)

    def update(self, delta_time):
        self.ball_x += 1


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

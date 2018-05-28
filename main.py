import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceInvaders(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def update(self, delta_time):
        pass


def main():
    game = SpaceInvaders(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

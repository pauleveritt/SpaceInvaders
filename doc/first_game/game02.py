import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Ball")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()

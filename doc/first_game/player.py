import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 50
MOVEMENT_SPEED = 3
PLAYER_COLOR = arcade.color.BUBBLES


class Player:
    def __init__(self, x, y, velocity, radius, color):
        self.x = x
        self.y = y
        self.delta_x = velocity
        self.delta_y = 0

        # Size and rotation
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def move(self):
        self.x += self.delta_x


class MyGame(arcade.Window):
    player: Player

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Start in the center
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2
        self.player = Player(x, y, MOVEMENT_SPEED, CIRCLE_RADIUS, PLAYER_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def update(self, delta_time):
        self.player.move()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

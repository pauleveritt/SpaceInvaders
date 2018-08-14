import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SHIP_SCALE = .5
ENEMY_SCALE = .2
VELOCITIES = [-2, -1, 1, 2]
EXPLOSION_TEXTURE_COUNT = 271


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("images/ship.png", SHIP_SCALE)
        self.center_x = 50
        self.center_y = 50


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("images/mystery.png", ENEMY_SCALE)
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGHT)
        self.velocity = [random.choice(VELOCITIES), random.choice(VELOCITIES)]

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self):
        super().__init__("images/explosion/explosion0000.png")

        # Start at the first frame
        self.current_texture = 0
        self.texture = self.textures[self.current_texture]

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(Explosion.explosion_textures):
            self.texture = Explosion.explosion_textures[self.current_texture]
        else:
            self.kill()


for i in range(EXPLOSION_TEXTURE_COUNT):
    texture = arcade.load_texture(f"images/explosion/explosion{i:04d}.png")
    Explosion.explosion_textures.append(texture)


class MyGame(arcade.Window):
    enemies = []
    ship = None
    score = 0
    explosions = []

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BEAVER)
        self.set_mouse_visible(False)
        self.background = arcade.load_texture("images/background.jpg")

    def setup(self):
        self.score = 0
        self.enemies = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        self.ship = Ship()
        for i in range(50):
            enemy = Enemy()
            self.enemies.append(enemy)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ship.draw()
        self.enemies.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.ELECTRIC_VIOLET)
        self.explosions.draw()

    def update(self, delta_time: float):
        self.enemies.update()
        self.explosions.update()
        hits = arcade.check_for_collision_with_list(self.ship, self.enemies)
        for hit in hits:
            explosion = Explosion()
            explosion.center_x = hit.center_x
            explosion.center_y = hit.center_y
            self.explosions.append(explosion)
            hit.kill()
            self.score += 1

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.ship.center_x = x
        self.ship.center_y = y


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()

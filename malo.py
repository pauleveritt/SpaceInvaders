import random
import arcade

SCREEN_HEIGHT = 476
SCREEN_WIDTH = 640
SHIP_SCALE = .5
ENEMY_SCALE = .2
VELOCITIES = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EXPLOSION_TEXTURE_COUNT = 271


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__("images/ship.png", SHIP_SCALE)
        self.center_x = 50
        self.center_y = 50


class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("images/enemy1_1.png", ENEMY_SCALE)
        self.center_x = x
        self.center_y = y
        self.velocity = [random.choice(VELOCITIES), random.choice(VELOCITIES)]

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Explosion(arcade.Sprite):
    explosion_textures = []

    def __init__(self):
        super().__init__("images/explosion/explosion0000.png")

        self.current_texture = 0
        self.texture = self.textures[self.current_texture]

    def update(self):

        self.current_texture += 1
        if self.current_texture < len(Explosion.explosion_textures):
            self.texture = Explosion.explosion_textures[self.current_texture]
        else:
            self.kill()


for i in range(EXPLOSION_TEXTURE_COUNT):
    texture = arcade.load_texture(f"images/explosion/explosion{i:04d}.png")
    Explosion.explosion_textures.append(texture)


class MyGame(arcade.Window):
    ship = None
    enemies = []
    score = 0
    explosions = []

    def __init__(self, width, height):
        super().__init__(width, height, title="Get the parasites off Jar Jar")
        self.set_mouse_visible(False)
        self.background = arcade.load_texture("images/jarjarbinks.jpg")

    def setup(self):
        self.score = 0
        self.enemies = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        self.ship = Ship()
        for i in range(500):
            x = random.randint(100, SCREEN_WIDTH - 100)
            y = random.randint(100, SCREEN_HEIGHT - 100)
            enemy = Enemy(x, y)
            self.enemies.append(enemy)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ship.draw()
        self.enemies.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 20, arcade.color.ORANGE, 40)
        self.explosions.draw()

    def update(self, delta_time):
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

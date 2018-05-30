import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ENEMY_SCALE = 0.25
ENEMY_WIDTH = 40
COLUMN_WIDTH = 60
ROW_HEIGHT = 60


class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__()
        self.textures = [
            arcade.load_texture('images/enemy1_1.png', scale=ENEMY_SCALE),
            arcade.load_texture('images/enemy1_2.png', scale=ENEMY_SCALE),
        ]
        self.texture_change_frames = 60

    @property
    def at_edge(self):
        return self.left < (self.width + 10) or \
               self.right > (SCREEN_WIDTH - self.width - 10)


class SpaceInvaders(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.enemy_sprite_list = arcade.SpriteList()
        self.enemy_position = SCREEN_HEIGHT - 200
        self.frames = 0
        self.enemy_velocity = COLUMN_WIDTH * 1  # Later this will be -1
        self.dropped_row = False

        # Load the movement sounds
        self.movement_sounds = {}
        for r in range(4):
            self.movement_sounds[r] = arcade.load_sound(f'sounds/{r}.wav'),
        self.current_sound = 0

    def setup(self):

        for row in range(3):
            for column in range(8):
                enemy = Enemy()
                enemy.center_x = 157 + (column * COLUMN_WIDTH)
                enemy.center_y = self.enemy_position + (row * ROW_HEIGHT)
                self.enemy_sprite_list.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.enemy_sprite_list.draw()

    @property
    def enemies_at_edge(self):
        # Return true if any enemies are at either edge
        for enemy in self.enemy_sprite_list:
            if enemy.at_edge:
                return True

        return False

    def drop_and_reverse(self):
        # If we are at the edge *and* didn't just drop a row...
        if self.enemies_at_edge and not self.dropped_row:
            # Drop a row and set the flag
            for enemy in self.enemy_sprite_list:
                enemy.center_y -= 50
            self.dropped_row = True
        else:
            # Did we just drop a row?
            if self.dropped_row:
                # Reverse direction and clear the flag
                self.enemy_velocity *= -1
                self.dropped_row = False

            # Move the enemy one column
            for enemy in self.enemy_sprite_list:
                enemy.center_x += self.enemy_velocity

    def play_movement_sound(self):
        # On each movement, play sound 0, then 1, through 4,
        # back to 0

        arcade.play_sound(self.movement_sounds[0])

    def update(self, delta_time):
        self.frames += 1

        if not self.frames % 60:
            # See if any of the enemies hit the edge
            self.drop_and_reverse()
            self.play_movement_sound()

        self.enemy_sprite_list.update()
        self.enemy_sprite_list.update_animation()


def main():
    game = SpaceInvaders(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

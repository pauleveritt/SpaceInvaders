Sounds for Explosions
=====================

.. code-block:: python

    # in __init__.py
    self.explosion_sound = arcade.sound.load_sound("sounds/shipexplosion.wav")

    # when exploding
    arcade.sound.play_sound(self.explosion_sound)


Ship Moves/Rotates With Keys
============================

.. code-block:: python

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.ship.change_angle = 3
        elif symbol == arcade.key.RIGHT:
            self.ship.change_angle = -3

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0


Kill Enemies With Missile
=========================


Re-appear On Other Side
=======================


Multi-Player
============



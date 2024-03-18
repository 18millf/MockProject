import pygame
from pygame import Color, Vector2, Rect

from drawable_object import DrawableObject
from game.blue_pedal import BluePedal
from game.pedal import Pedal
from game.red_pedal import RedPedal
from game_objects import GameObjects


class PedalOverlap(DrawableObject):
    def start(self):
        self.color: Color = Color(238, 238, 238)

        self.red_pedal: RedPedal = GameObjects.get(RedPedal)
        self.blue_pedal: BluePedal = GameObjects.get(BluePedal)

        print("aaaaaa")
        print(self.red_pedal)

    def update(self, delta: float):
        red_pos = self.red_pedal.position
        blue_pos = self.blue_pedal.position

        pedal_length = Pedal.PEDAL_LENGTH

        red_min = red_pos.x
        red_max = red_min + pedal_length
        blue_min = blue_pos.x
        blue_max = blue_min + pedal_length

        overlap_length = max(0, min(red_max, blue_max) - max(red_min, blue_min))

        pedal_radius = Pedal.PEDAL_RADIUS

        red_mid = red_pos + (pedal_radius, 0)
        blue_mid = blue_pos + (pedal_radius, 0)

        overlap_mid = (red_mid + blue_mid) / 2
        overlap_pos = overlap_mid - (overlap_length / 2, 0)

        pygame.draw.rect(self.screen, self.color, Rect(overlap_pos, Vector2(overlap_length, 5)))

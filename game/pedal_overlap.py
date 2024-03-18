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
        self.pedal_length = Pedal.PEDAL_LENGTH
        self.pedal_radius = Pedal.PEDAL_RADIUS

        print("aaaaaa")
        print(self.red_pedal)

    def update(self, delta: float):
        red_pos: Vector2 = self.red_pedal.position
        blue_pos: Vector2 = self.blue_pedal.position

        red_mid: Vector2 = red_pos + Vector2(self.pedal_radius, 0)
        blue_mid: Vector2 = blue_pos + Vector2(self.pedal_radius, 0)

        blue_end_x = blue_pos.x + self.pedal_length
        red_end_x = red_pos.x + self.pedal_length

        overlap_length: float = max(0, min(blue_end_x, red_end_x) - max(blue_pos.x, red_pos.x))
        overlap_radius: float = overlap_length / 2

        mid_point: Vector2 = ((red_mid + blue_mid) - Vector2(overlap_radius, 0)) / 2

        pygame.draw.rect(self.screen, self.color, Rect(mid_point.x, mid_point.y, overlap_length, 5))

from pygame import Rect, Vector2
from drawable_object import DrawableObject
from game.boundary_box import BoundaryBox
from game_objects import GameObjects

from pygame.color import Color
from pygame.key import get_pressed
from pygame.math import clamp
import pygame

class Pedal(DrawableObject):
    PEDAL_LENGTH: int = 115
    PEDAL_RADIUS: int = 115 // 2

    SENSITIVITY: int = 180

    def start(self):
        self.color: Color = Color(255, 255, 255)

        self.boundary_box: BoundaryBox = GameObjects.get(BoundaryBox)

        self.left_boundary: int = self.boundary_box.position.x + BoundaryBox.BOX_THICKNESS
        self.right_boundary: int = self.boundary_box.position.x + BoundaryBox.BOX_WIDTH - Pedal.PEDAL_LENGTH - BoundaryBox.BOX_THICKNESS

        self.forward_key: int
        self.backward_key: int
        self.left_key: int
        self.right_key: int

        self.position: Vector2 = Vector2

        print(self)

    def update(self, delta: float):
        keys = get_pressed()

        x_position: int = self.position.x

        if keys[self.left_key]:
            x_position -= Pedal.SENSITIVITY * delta
        if keys[self.right_key]:
            x_position += Pedal.SENSITIVITY * delta

        self.position.x = clamp(x_position, self.left_boundary, self.right_boundary)

        pygame.draw.rect(self.screen, self.color, Rect(self.position.x, self.position.y, Pedal.PEDAL_LENGTH, 5))
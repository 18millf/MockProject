from drawable_object import DrawableObject
from pygame.math import Vector2
from display import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
from pygame import Rect

class BoundaryBox(DrawableObject):
    BOX_WIDTH: int = 550
    BOX_HEIGHT: int = 730
    BOX_THICKNESS: int = 5
    
    def start(self):
        self.position: Vector2 = Vector2(
            (SCREEN_WIDTH // 2) - (BoundaryBox.BOX_WIDTH // 2),
            (SCREEN_HEIGHT // 2) - (BoundaryBox.BOX_HEIGHT // 2)
            )

    def update(self, _: float):
        pygame.draw.rect(
            self.screen, 
            (255, 255, 255), 
            Rect(self.position.x, self.position.y,
                 BoundaryBox.BOX_WIDTH, BoundaryBox.BOX_HEIGHT
                 ),
            5
            )
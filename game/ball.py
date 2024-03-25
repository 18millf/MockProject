import pygame
from pygame import Vector2, Rect
from physics_object import PhysicsObject

from game.boundary_box import BoundaryBox
from game_objects import GameObjects

DEBUG_LINES: bool = True

class Ball(PhysicsObject):
    def start(self):
        self.position: Vector2 = Vector2(200, 200)
        self.radius: int = 10
        self.velocity: Vector2 = Vector2(0, 0)
        self.gravity: Vector2 = Vector2(-150, 0)

        self.boundary_box: BoundaryBox = GameObjects.get(BoundaryBox)
        self.boundary_box_rect: Rect = self.boundary_box.rect
        self.boundary_box_thickness: float = BoundaryBox.BOX_THICKNESS

        self.boundary_left: Rect = Rect(self.boundary_box_rect.left, self.boundary_box_rect.top,
                                        self.boundary_box_thickness, self.boundary_box_rect.height)
        self.boundary_top: Rect = Rect(self.boundary_box_rect.left, self.boundary_box_rect.top,
                                       self.boundary_box_rect.width, self.boundary_box_thickness)
        self.boundary_bottom: Rect = Rect(self.boundary_box_rect.left,
                                          self.boundary_box_rect.top + self.boundary_box_rect.height - self.boundary_box_thickness,
                                          self.boundary_box_rect.width, self.boundary_box_thickness
                                          )
        self.boundary_right: Rect = Rect(self.boundary_box_rect.left + self.boundary_box_rect.width - self.boundary_box_thickness,
                                         self.boundary_box_rect.top, self.boundary_box_thickness,
                                         self.boundary_box_rect.height)
        
        self.vertical_boundaries: list[Rect] = [self.boundary_top, self.boundary_bottom]
        self.horizontal_boundaries: list[Rect] = [self.boundary_left, self.boundary_right]

        self.closest_collide: Vector2 = Vector2(0, 0)

    def physics_process(self):
        y_dist: list[float] = [abs(self.boundary_top.y - self.position.y), abs(self.boundary_bottom.y - self.position.y)]
        x_dist: list[float] = [abs(self.boundary_left.x - self.position.x), abs(self.boundary_right.x - self.position.x)]

        closest_vertical = min([0, 1], key=y_dist.__getitem__)
        closest_horizontal = min([0, 1], key=x_dist.__getitem__)

        



    def update(self, delta: float):
        super().update(delta)

        pygame.draw.circle(self.screen, (255, 255, 255), self.position, self.radius)

        if DEBUG_LINES:
            pygame.draw.rect(self.screen, (255, 0, 0), self.boundary_left, 1)
            pygame.draw.rect(self.screen, (255, 0, 0), self.boundary_top, 1)
            pygame.draw.rect(self.screen, (255, 0, 0), self.boundary_bottom, 1)
            pygame.draw.rect(self.screen, (255, 0, 0), self.boundary_right, 1)

            pygame.draw.line(self.screen, (0, 0, 255), self.position, self.closest_collide, 1)
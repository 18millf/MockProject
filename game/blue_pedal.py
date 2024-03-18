from game.boundary_box import BoundaryBox
from game.pedal import Pedal
from pygame.locals import K_UP, K_LEFT, K_DOWN, K_RIGHT
from pygame.math import Vector2

class BluePedal(Pedal):
    def start(self):
        super().start()

        self.color = "#2ea4d9"

        self.forward_key = K_UP
        self.left_key = K_LEFT
        self.backward_key = K_DOWN
        self.right_key = K_RIGHT

        self.position = self.boundary_box.position + Vector2(BoundaryBox.BOX_WIDTH - 125, 600)
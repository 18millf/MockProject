from game.pedal import Pedal
from pygame.locals import K_w, K_a, K_s, K_d
from pygame.math import Vector2

class RedPedal(Pedal):
    def start(self):
        super().start()

        self.color = "#2ea4d9"

        self.forward_key = K_w
        self.left_key = K_a
        self.backward_key = K_s
        self.right_key = K_d

        self.position = self.boundary_box.position + Vector2(10, 600)
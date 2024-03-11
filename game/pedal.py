from drawable_object import DrawableObject

from pygame.color import Color

class Pedal(DrawableObject):
    def start(self):
        self.color: Color = Color(255, 255, 255)

        self.forward_key: int
        self.backward_key: int
        self.left_key: int
        self.right_key: int

    def update(self):
        
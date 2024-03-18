from pygame import Vector2
from physics_object import PhysicsObject

class Ball(PhysicsObject):
    def start(self):
        self.position: Vector2
        self.radius: int = 10
        self.velocity: Vector2
        self.gravity: Vector2 = Vector2(-150, 0)

    def physics_process():
        
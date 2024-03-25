from drawable_object import DrawableObject

class PhysicsObject(DrawableObject):
    fixed_delta: float = 1.0 / 50.0

    def physics_process(self):
        pass
from drawable_object import DrawableObject
from physics_object import PhysicsObject
from typing import TypeVar, Type

T = TypeVar("T")

class GameObjects:
    game_objects: list[DrawableObject] = list()
    physics_objects: list[PhysicsObject] = list()

    @staticmethod
    def get(obj_type: Type[T]) -> T:
        for obj in GameObjects.game_objects:
            if isinstance(obj, obj_type):
                return obj
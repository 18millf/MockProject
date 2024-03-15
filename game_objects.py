from drawable_object import DrawableObject
from typing import TypeVar, Type

T = TypeVar("T")

class GameObjects:
    game_objects: list[DrawableObject] = list()

    def get(type: Type[T]) -> T:
        for obj in GameObjects.game_objects:
            print(f"Type name: {type.__name__}    Class name: {type(obj).__class__.__name__}")
            if type.__name__ == type(obj).__class__.__name__:
                return obj
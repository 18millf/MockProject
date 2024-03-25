import pygame
from pygame.time import Clock
from pygame import Surface, Rect, Vector2

from display import SCREEN_WIDTH, SCREEN_HEIGHT
from game.blue_pedal import BluePedal
from game.pedal_overlap import PedalOverlap
from game.red_pedal import RedPedal
from game.ball import Ball
from game_objects import GameObjects

from game.boundary_box import BoundaryBox
from physics_object import PhysicsObject

BOX_WIDTH: int = 550
BOX_HEIGHT: int = 730

MAX_FRAME_RATE: int = 120

def main():
    pygame.init()
    pygame.font.init()

    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    running: bool = True

    GameObjects.game_objects = [
        BoundaryBox(screen),
        RedPedal(screen),
        BluePedal(screen),
        PedalOverlap(screen),
        Ball(screen),
    ]

    for object in GameObjects.game_objects:
            if isinstance(object, PhysicsObject):
                GameObjects.physics_objects.append(object)

            object.start()

    phys_timer: float = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#222222")

        delta: float = clock.tick_busy_loop(MAX_FRAME_RATE) / 1000

        phys_timer += delta

        if (phys_timer >= PhysicsObject.fixed_delta):
            for phys_object in GameObjects.physics_objects:
                phys_object.physics_process()

            phys_timer = 0

        for object in GameObjects.game_objects:
            object.update(delta)

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()
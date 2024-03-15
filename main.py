import pygame
from pygame.time import Clock
from pygame import Surface, Rect
from math import sin, cos

from display import SCREEN_WIDTH, SCREEN_HEIGHT
from game.red_pedal import RedPedal
from game_objects import GameObjects

from game.boundary_box import BoundaryBox

BOX_WIDTH: int = 550
BOX_HEIGHT: int = 730

BOX_POS_X: int = (SCREEN_WIDTH // 2) - (BOX_WIDTH // 2)
BOX_POS_Y: int = (SCREEN_HEIGHT // 2) - (BOX_HEIGHT // 2)

MAX_FRAME_RATE: int = 60

def main():
    pygame.init()
    pygame.font.init()

    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    running: bool = True

    GameObjects.game_objects = [
        BoundaryBox(screen),
        RedPedal(screen)
    ]

    for object in GameObjects.game_objects:
            object.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#222222")

        delta: float = clock.tick(MAX_FRAME_RATE) / 1000

        for object in GameObjects.game_objects:
            object.update(delta)

        # Pedal 2
        pygame.draw.rect(screen, "#d13f41", Rect(BOX_POS_X + BOX_WIDTH - 125, BOX_POS_Y + 600, 115, 5))

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()
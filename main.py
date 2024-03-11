import pygame
from pygame.time import Clock
from pygame import Surface, Rect
from math import sin, cos

from display import SCREEN_WIDTH, SCREEN_HEIGHT
from game_objects import GameObjects

from game.boundary_box import BoundaryBox

BOX_WIDTH: int = 550
BOX_HEIGHT: int = 730

BOX_POS_X: int = (SCREEN_WIDTH // 2) - (BOX_WIDTH // 2)
BOX_POS_Y: int = (SCREEN_HEIGHT // 2) - (BOX_HEIGHT // 2)

def main():
    pygame.init()
    pygame.font.init()

    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    running: bool = True

    GameObjects.game_objects = [
        BoundaryBox(screen)
    ]

    for object in GameObjects.game_objects:
            object.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#222222")

        for object in GameObjects.game_objects:
            object.update()

        # Pedal 1
        pygame.draw.rect(screen, "#2ea4d9", Rect(BOX_POS_X + 10, BOX_POS_Y + 600, 115, 5))

        # Pedal 2
        pygame.draw.rect(screen, "#d13f41", Rect(BOX_POS_X + BOX_WIDTH - 125, BOX_POS_Y + 600, 115, 5))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
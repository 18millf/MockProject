import pygame
from pygame.time import Clock
from pygame import Surface
from math import sin, cos

def main():
    pygame.init()
    pygame.font.init()

    screen: Surface = pygame.display.set_mode((1280, 720))
    clock: Clock = pygame.time.Clock()
    running: bool = True

    text_font = pygame.font.SysFont("LiberationSerif", 45)

    circle_rect = pygame.rect.Rect(0, 0, 0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#222222")

        text_surface = text_font.render("Hello World!", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(640, 360))

        circle_rect = pygame.draw.circle(screen, (255, 255, 255), circle_rect.center, 50)
        (pos_x, pos_y) = circle_rect.center
        pos_x -= 640
        pos_y -= 360
        pos_x = int(pos_x * cos(0.1) - pos_y * sin(0.1))
        pos_y = int(pos_x * sin(0.1) + pos_y * sin(0.1))
        pos_x += 640
        pos_y += 360

        circle_rect.center = (pos_x, pos_y)

        screen.blit(text_surface, text_rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
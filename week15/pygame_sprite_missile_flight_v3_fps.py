import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 30


class Missile(pygame.sprite.Sprite):

    surface = pygame.image.load('assets/sprites/missile.png')

    def __init__(self):
        super().__init__()
        self.rect = self.surface.get_rect()
        self.rect.left = SCREEN_WIDTH
        self.rect.top = random.randrange(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randrange(1, 10)

    def update(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.image.load('assets/backdrops/space.png')
    missile = Missile()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, background.get_rect())

        missile.update()
        screen.blit(missile.surface, missile.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()

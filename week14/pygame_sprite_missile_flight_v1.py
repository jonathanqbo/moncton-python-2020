import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


class Missile(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/missile.png')

    def __init__(self):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_WIDTH
        self.rect.top = random.randrange(0, SCREEN_HEIGHT - self.rect.height)

    def update(self):
        self.rect.right -= 10
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load('../week15/assets/backdrops/space.png')
    screen.blit(background, background.get_rect())

    # create and show sprite missile
    missile = Missile()
    # screen.blit(missile.surface, missile.rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        missile.update()
        screen.blit(missile.image, missile.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()

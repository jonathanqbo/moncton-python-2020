import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


class Missile(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/missile.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        self.rect.center = 100, 100


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load('assets/backdrops/space.png')
    screen.blit(background, (0, 0))

    # create and show sprite missile
    missile = Missile()
    screen.blit(missile.image, missile.rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()

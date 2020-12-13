import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 30


class Missile(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/missile.png')

    def __init__(self, *groups):
        super().__init__(groups)
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_WIDTH
        self.rect.top = random.randrange(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randrange(1, 10)

    def update(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            # remove this missile if it's out of screen
            self.kill()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.image.load('assets/backdrops/space.png')
    missiles = pygame.sprite.Group()
    for _ in range(10):
        missiles.add(Missile())
        # Missile(missiles)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, background.get_rect())

        missiles.update()
        missiles.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()

import pygame
import random
import itertools

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 30
LAUNCH_MISSILE = pygame.USEREVENT + 1


class SpaceBackground(pygame.sprite.Sprite):

    image = pygame.image.load('assets/backdrops/space.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        pygame.mixer.Sound('assets/sounds/back_ground.wav').play()


class Jet(pygame.sprite.Sprite):

    ANIMATION_SPEED = 200
    images = [pygame.image.load(f'assets/sprites/jet{i}.png') for i in range(2)]

    def __init__(self):
        super().__init__()
        self.images_iter = itertools.cycle(self.images)
        self.image = next(self.images_iter)
        self.rect = self.image.get_rect()
        self.rect.centery = SCREEN_HEIGHT // 2
        # variable for animate costume
        self.costume_start_time = pygame.time.get_ticks()
        # variables for movement
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.__change_costume()
        self.__move()

    def __move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -10
        elif keys[pygame.K_RIGHT]:
            self.speed_x = 10
        else:
            self.speed_x = 0
        if keys[pygame.K_DOWN]:
            self.speed_y = 10
        elif keys[pygame.K_UP]:
            self.speed_y = -10
        else:
            self.speed_y = 0
        self.rect.move_ip(self.speed_x, self.speed_y)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def __change_costume(self):
        now = pygame.time.get_ticks()
        if (now - self.costume_start_time) > self.ANIMATION_SPEED:
            self.image = next(self.images_iter)
            self.costume_start_time = now


class Missile(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/missile.png')

    def __init__(self):
        super().__init__()
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

    pygame.time.set_timer(LAUNCH_MISSILE, 1000)

    background = SpaceBackground()
    missiles = pygame.sprite.Group()
    jet = Jet()

    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == LAUNCH_MISSILE:
                missiles.add(Missile())

        screen.blit(background.image, background.rect)

        missiles.update()
        missiles.draw(screen)

        jet.update()
        screen.blit(jet.image, jet.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()

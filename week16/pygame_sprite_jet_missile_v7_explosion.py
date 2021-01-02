import pygame
import random
import itertools

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 30
LAUNCH_MISSILE = pygame.USEREVENT + 1


class GameOver(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/game_over.png')

    def __init__(self, *groups):
        super().__init__(groups)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2


class SpaceBackground(pygame.sprite.Sprite):

    image = pygame.image.load('assets/backdrops/space.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        pygame.mixer.Sound('assets/sounds/back_ground.wav').play(loops=-1)


class Jet(pygame.sprite.Sprite):

    ANIMATION_SPEED = 200
    images = [pygame.image.load(f'assets/sprites/jet{i}.png') for i in range(2)]

    def __init__(self, game, *groups):
        super().__init__(groups)
        self.game = game
        self.images_iter = itertools.cycle(self.images)
        self.image = next(self.images_iter)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = SCREEN_HEIGHT // 2
        # variable for animate costume
        self.costume_start_time = pygame.time.get_ticks()
        # variables for movement
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.__change_costume()
        self.__move()
        self.__hit_missile()

    def fire(self):
        Missile(self.game, self.rect.right, self.rect.centery, self.game.missiles, self.game.all_sprites)

    def __hit_missile(self):
        the_missile = pygame.sprite.spritecollideany(self, self.game.asteroids)
        if the_missile:
            the_missile.kill()
            self.game.game_over()

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
    image = pygame.transform.flip(image, True, True)

    def __init__(self, game, x, y, *groups):
        super().__init__(groups)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speed = 15

    def update(self):
        self.__move()
        self.__hit()

    def __hit(self):
        the_asteroid = pygame.sprite.spritecollideany(self, self.game.asteroids)
        if the_asteroid:
            Explosion(self.rect.right, self.rect.centery, self.game.all_sprites)
            pygame.mixer.Sound('assets/sounds/explosion.wav').play()
            self.kill()
            the_asteroid.kill()

    def __move(self):
        self.rect.right += self.speed
        if self.rect.right > SCREEN_WIDTH:
            # remove this missile if it's out of screen
            self.kill()


class Asteroid(pygame.sprite.Sprite):

    images = [pygame.image.load(f'assets/sprites/asteroid{i}.png') for i in range(2)]

    def __init__(self, game, *groups):
        super().__init__(groups)
        self.game = game
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_WIDTH
        self.rect.top = random.randrange(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randrange(1, 10)

    def update(self):
        self.__move()

    def __move(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            # remove this missile if it's out of screen
            self.kill()


class Explosion(pygame.sprite.Sprite):

    images = [pygame.image.load(f'assets/sprites/explosion_alpha_{i}.png') for i in range(16)]
    ANIMATE_SPPED = 10

    def __init__(self, x, y, *groups):
        super().__init__(groups)
        # images_converted = [img.convert_alpha() for img in self.images]
        # images_converted = self.images
        # self.images_iter = iter(images_converted)
        self.images_iter = iter(self.images)
        self.image = next(self.images_iter)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.costume_start_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.costume_start_time > self.ANIMATE_SPPED:
            try:
                self.image = next(self.images_iter)
            except StopIteration:
                self.kill()
        self.costume_start_time = now


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.time.set_timer(LAUNCH_MISSILE, 1000)

        self.background = SpaceBackground()
        self.asteroids = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.jet = Jet(self, self.all_sprites)

    def run(self):
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == LAUNCH_MISSILE:
                    Asteroid(self, self.asteroids, self.all_sprites)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jet.fire()

            self.screen.blit(self.background.image, self.background.rect)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

    def game_over(self):
        gameover_sprite = GameOver()
        # self.screen.blit(self.jet.image, self.jet.rect)
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == LAUNCH_MISSILE:
                    self.asteroids.add(Asteroid(self))

            self.screen.blit(self.background.image, self.background.rect)

            self.asteroids.update()
            self.asteroids.draw(self.screen)

            self.screen.blit(gameover_sprite.image, gameover_sprite.rect)

            pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()

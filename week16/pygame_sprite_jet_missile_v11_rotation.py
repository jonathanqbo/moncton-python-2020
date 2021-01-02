import pygame
import random
import itertools
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 30

LAUNCH_MISSILE = pygame.USEREVENT + 1


class GameOver(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/game_over.png')

    def __init__(self, *groups):
        super().__init__(groups)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2


class Score(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(groups)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.score = 0

    def update(self):
        self.image = self.font.render(f'Score: {self.score}', True, (0, 0, 0), (255, 255, 255))
        self.rect = self.image.get_rect()


class SpaceBackground(pygame.sprite.Sprite):

    image = pygame.image.load('assets/backdrops/space.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        pygame.mixer.Sound('assets/sounds/back_ground.wav').play(loops=-1)


class Jet(pygame.sprite.Sprite):

    ANIMATION_SPEED = 100
    images = [pygame.image.load(f'assets/sprites/jet{i}.png') for i in range(2)]
    shoot_images = [pygame.image.load(f'assets/sprites/jet_shoot_{i}.png') for i in range(5)]

    def __init__(self, game, *groups):
        super().__init__(groups)
        self.game = game
        self.images_iter = itertools.cycle(self.images)
        self.image = next(self.images_iter)
        # self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = SCREEN_HEIGHT // 2
        # variable for animate costume
        self.last_costume_change_time = pygame.time.get_ticks()
        # variables for movement
        self.speed_x = 0
        self.speed_y = 0
        # variable to control shoot speed
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_cool_down = 500
        # variable for shooting
        self.shooting = False
        # variable for rotation
        self.rotating = False
        self.angle = 0
        self.rotating_speed = 100
        self.last_rotating = pygame.time.get_ticks()

    def update(self):
        self.__change_costume()
        self.__move()
        self.__hit_missile()

    def rotate(self):
        if self.rotating:
            return

        self.rotating = True
        self.angle = 0
        self.last_rotating = pygame.time.get_ticks()

    def __rotating(self):
        if self.rotating:
            # now = pygame.time.get_ticks()
            # if (now - self.last_rotating) > self.ANIMATION_SPEED:
            self.angle += 10
            center = self.rect.center
            print(center)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            # self.rect.center = center
            if self.angle >= 360:
                self.rotating = False
                self.angle = 0

                # self.last_rotating = now

    def fire(self):
        now = pygame.time.get_ticks()
        if (now - self.last_shoot) > self.shoot_cool_down:
            Missile(self.game, self.rect.centerx, self.rect.centery, self.angle, self.game.missiles, self.game.all_sprites)
            self.last_shoot = now

            pygame.mixer.Sound('assets/sounds/shooting.wav').play()
            self.shooting = True
            self.shooting_images_iter = iter(self.shoot_images)

    def __hit_missile(self):
        the_asteroid = pygame.sprite.spritecollideany(self, self.game.asteroids)
        if the_asteroid:
            the_asteroid.kill()
            self.kill()
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
        if (now - self.last_costume_change_time) < self.ANIMATION_SPEED:
            return

        if self.shooting:
            try:
                self.image = next(self.shooting_images_iter)
                self.__rotating()
            except StopIteration:
                self.shooting = False
        else:
            self.image = next(self.images_iter)
            self.__rotating()

        self.last_costume_change_time = now



class Missile(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/missile.png')
    image = pygame.transform.flip(image, True, True)

    def __init__(self, game, x, y, angle, *groups):
        super().__init__(groups)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speed = 15
        self.angle = angle
        self.speed_y = -math.sin(math.radians(self.angle)) * self.speed
        self.speed_x = math.cos(math.radians(self.angle)) * self.speed
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.move_ip(self.speed_x, self.speed_y)

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
            self.game.score.score += 1

    def __move(self):
        # self.rect.right += self.speed
        self.rect.move_ip(self.speed_x, self.speed_y)

        if not self.game.screen.get_rect().colliderect(self.rect):
        # if self.rect.right < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0:
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
        images_converted = [img.convert_alpha() for img in self.images]
        self.images_iter = iter(images_converted)
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
        self.score = Score(self.all_sprites)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == LAUNCH_MISSILE:
                    Asteroid(self, self.asteroids, self.all_sprites)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.jet.fire()
                    if event.key == pygame.K_r:
                        self.jet.rotate()

            self.screen.blit(self.background.image, self.background.rect)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

    def game_over(self):
        gameover_sprite = GameOver()
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == LAUNCH_MISSILE:
                    self.asteroids.add(Asteroid(self))

            self.screen.blit(self.background.image, self.background.rect)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            self.screen.blit(gameover_sprite.image, gameover_sprite.rect)

            pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()

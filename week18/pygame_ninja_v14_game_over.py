import pygame
import itertools
import random

FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 750


class Background(pygame.sprite.Sprite):

    origin_image = pygame.image.load(f'assets/grass/BG/BG.png')

    def __init__(self):
        super().__init__()

        self.image = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image.blit(self.origin_image, (0, 0))
        self.image.blit(self.origin_image, (self.origin_image.get_rect().width, 0))
        self.rect = self.image.get_rect()

        pygame.mixer.stop()
        pygame.mixer.Sound('assets/sounds/bg_music_ninjia.wav').play(loops=-1)


class GameOver(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/game_over.png')

    def __init__(self, game):
        super().__init__()
        self.__game = game
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

        self.__show_failed_screen()

    def __show_failed_screen(self):
        running = True
        clock = pygame.time.Clock()
        self.__game.all_sprites.remove(self.__game.ninja)
        self.__game.all_sprites.add(self)
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.__game._draw()
            pygame.display.flip()


class FlyEnemy(pygame.sprite.Sprite):

    def __init__(self, left, bottom, *groups):
        super().__init__(groups)
        self.__image_iter = itertools.cycle([self.image_normal, self.image_fly])
        self.image = next(self.__image_iter)
        self.rect = self.image.get_rect()
        #
        self.rect.left = left
        self.rect.bottom = bottom
        #
        self._last_animation_time = pygame.time.get_ticks()
        # self.__moved_distance = 0
        self.__speed = -5

    def update(self):
        now = pygame.time.get_ticks()
        if now - self._last_animation_time > 200:
            self.image = next(self.__image_iter)
            self._last_animation_time = now

        self.rect.x += self.__speed


class Bat(FlyEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/bat.png')
    image_fly = pygame.image.load('assets/sprites/Enemy/bat_fly.png')


class Bee(FlyEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/bee.png')
    image_fly = pygame.image.load('assets/sprites/Enemy/bee_fly.png')


class CrawlEnemy(pygame.sprite.Sprite):

    def __init__(self, left, bottom, *groups):
        super().__init__(groups)
        self.__image_iter = itertools.cycle([self.image_normal, self.image_walk])
        self.image = next(self.__image_iter)
        self.rect = self.image.get_rect()
        #
        self.rect.left = left
        self.rect.bottom = bottom
        #
        self._last_animation_time = pygame.time.get_ticks()
        self.__moved_distance = 0
        self.__speed = -1
        self.__flip = False

    def update(self):
        now = pygame.time.get_ticks()
        if now - self._last_animation_time > 200:
            self.image = next(self.__image_iter)
            self._last_animation_time = now
            if self.__flip:
                self.image = pygame.transform.flip(self.image, True, False)

        self.rect.x += self.__speed
        self.__moved_distance += abs(self.__speed)
        if self.__moved_distance > 100:
            self.__speed = -self.__speed
            self.__moved_distance = 0
            self.__flip = not self.__flip


class Snail(CrawlEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/snail.png')
    image_walk = pygame.image.load('assets/sprites/Enemy/snail_walk.png')


class Snake(CrawlEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/snake.png')
    image_walk = pygame.image.load('assets/sprites/Enemy/snake_walk.png')


class Spider(CrawlEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/spider.png')
    image_walk = pygame.image.load('assets/sprites/Enemy/spider_walk1.png')


class Ladybug(CrawlEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/ladyBug.png')
    image_walk = pygame.image.load('assets/sprites/Enemy/ladyBug_walk.png')


class Mouse(CrawlEnemy):
    image_normal = pygame.image.load('assets/sprites/Enemy/mouse.png')
    image_walk = pygame.image.load('assets/sprites/Enemy/mouse_walk.png')


class GrassPlatformDecoration(pygame.sprite.Sprite):
    images_decor = [
        pygame.image.load('assets/grass/grass_ground_Deco/Bush (1).png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Bush (2).png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Bush (3).png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Bush (4).png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Mushroom_1.png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Mushroom_2.png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Tree_1.png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Tree_2.png'),
        pygame.image.load('assets/grass/grass_ground_Deco/Tree_3.png')
    ]

    def __init__(self, left, bottom, *groups):
        super().__init__(groups)
        self.image = random.choice(self.images_decor)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom


class Decorator:

    def __init__(self, decorator):
        self.decorator = decorator

    def decor(self, platform):
        for i in range(platform.rect.width // 100):
            if random.randrange(0, 100) < 20:
                continue

            decor = self.decorator(random.randint(platform.rect.left, platform.rect.right), platform.rect.top,
                                             platform.game.decorators)
            if decor.rect.right > platform.rect.right:
                decor.rect.right = platform.rect.right
            if decor.rect.left < platform.rect.left:
                decor.rect.left = platform.rect.left


class FloatTile(pygame.sprite.Sprite):

    def __init__(self, game, left, bottom, width, *groups):
        if width < 2:
            raise ValueError('The length of float platform need be >= 2')

        super().__init__(groups)
        self.game = game
        self.image = self.__build(width)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def __build(self, length):
        width = self.image_left.get_rect().width * length
        height = self.image_left.get_rect().height

        surface = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        surface.blit(self.image_left, (0, 0))
        x = self.image_left.get_rect().width
        if length > 2:
            for i in range(1, length - 1):
                surface.blit(self.image_middle, (x, 0))
                x += self.image_middle.get_rect().width
        surface.blit(self.image_right, (x, 0))

        return surface


class GrassFloatPlatform(FloatTile):
    image_left = pygame.image.load('assets/grass/grass_ground_Tiles/13.png')
    image_middle = pygame.image.load('assets/grass/grass_ground_Tiles/14.png')
    image_right = pygame.image.load('assets/grass/grass_ground_Tiles/15.png')
    decorator = GrassPlatformDecoration


class GroundTile(pygame.sprite.Sprite):

    def __init__(self, game, bottom, width, height, *groups):
        super().__init__(groups)
        self.game = game
        self.image = self.__build(width, height)
        self.rect = self.image.get_rect()
        self.rect.left = self.game.scene_width
        self.rect.bottom = bottom
        # update game scene width
        self.game.scene_width += self.rect.width - 8

    def __build(self, width, height):
        if width < 3 or height < 1:
            raise ValueError('Minimal width is 3, minimal height is 1')

        image_rect = self.image_top_left.get_rect()

        surface = pygame.surface.Surface((width * image_rect.width, height * image_rect.height), pygame.SRCALPHA)

        # top
        surface.blit(self.image_top_left, (0, 0))
        surface.blit(self.image_top_right, ((width - 1) * image_rect.width, 0))
        for i in range(1, width - 1):
            surface.blit(self.image_top_middle, (i * image_rect.width, 0))

        # bottom
        for i in range(1, height):
            surface.blit(self.image_bottom_left, (0, i * image_rect.height))
            surface.blit(self.image_bottom_right, ((width - 1) * image_rect.width, i * image_rect.height))
            for j in range(1, width - 1):
                surface.blit(self.image_bottom_middle, (j * image_rect.width, i * image_rect.height))

        return surface


class GrassPlatform(GroundTile):
    image_top_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/1.png')
    image_top_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/2.png')
    image_top_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/3.png')
    image_bottom_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/4.png')
    image_bottom_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/5.png')
    image_bottom_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/6.png')


class Water(GroundTile):
    image_top_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_bottom_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')


class Ninja(pygame.sprite.Sprite):

    ANIMATION_SPEED = 50
    ANIMATION_SLOW_SPEED = 100

    walk_images = [pygame.image.load(f'assets/sprites/ninjia/Run__00{i}.png') for i in range(10)]
    walk_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in walk_images]
    walk_image_iter = itertools.cycle(walk_images)

    fight_images = [pygame.image.load(f'assets/sprites/ninjia/Attack__00{i}.png') for i in range(10)]
    fight_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in fight_images]

    jump_images = [pygame.image.load(f'assets/sprites/ninjia/Jump__00{i}.png') for i in range(10)]
    jump_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in jump_images]

    jump_attack_images = [pygame.image.load(f'assets/sprites/ninjia/Jump_Attack__00{i}.png') for i in range(10)]
    jump_attack_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in jump_attack_images]

    throw_images = [pygame.image.load(f'assets/sprites/ninjia/Throw__00{i}.png') for i in range(10)]
    throw_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in throw_images]

    jump_throw_images = [pygame.image.load(f'assets/sprites/ninjia/Jump_Throw__00{i}.png') for i in range(10)]
    jump_throw_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in jump_throw_images]

    dead_images = [pygame.image.load(f'assets/sprites/ninjia/Dead__00{i}.png') for i in range(10)]
    dead_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in dead_images]

    idle_images = [pygame.image.load(f'assets/sprites/ninjia/Idle__00{i}.png') for i in range(10)]
    idle_images = [pygame.transform.rotozoom(img, 0, 0.3) for img in idle_images]
    idle_images_iter = itertools.cycle(idle_images)

    def __init__(self, game, left, bottom, *groups):
        super().__init__(groups)
        self.__game = game
        self.image = next(self.walk_image_iter)
        self.fight_images_iter = iter(self.fight_images)
        self.jump_images_iter = itertools.cycle(self.jump_images)
        self.jump_attack_images_iter = iter(self.jump_attack_images)
        self.throw_images_iter = itertools.cycle(self.throw_images)
        self.jump_throw_images_iter = iter(self.jump_throw_images)
        self.dead_image_iter = iter(self.dead_images)
        self.rect = self.image.get_rect()
        # initial position
        self.rect.left = left
        self.rect.bottom = bottom
        # for animation
        self.__last_animation_time = pygame.time.get_ticks()
        self.__last_slow_animation_time = pygame.time.get_ticks()
        # for image transform
        self.__origin_img = self.image
        # for moving
        self.__vel = pygame.math.Vector2(0, 0)
        self.__acc = pygame.math.Vector2(0, 0)
        self.__gra = 0.8
        # for moving
        self.__speed = 10
        self.__facing = 0
        # for state: fight throw jump dead
        self.__in_fighting = False
        self.__in_throwing = False
        self.__in_jumping = False
        self.__in_dead = False
        # sound
        self.__running_sound = pygame.mixer.Sound('assets/sounds/running.wav')

    def update(self):
        self.__moving()
        self.__animate()
        # self.image.fill((100, 100, 0), self.image.get_rect())

    def __animate(self):
        now = pygame.time.get_ticks()
        if self.__is_jumping() and self.__in_fighting:
            if now - self.__last_animation_time > self.ANIMATION_SPEED:
                try:
                    self.image = next(self.jump_attack_images_iter)
                    self.__last_animation_time = now
                    self.__origin_img = self.image
                    print('jump + fight')
                except StopIteration:
                    print('stop jump + fight')
                    self.__in_fighting = False
        elif self.__is_jumping() and self.__in_throwing:
            if now - self.__last_animation_time > self.ANIMATION_SPEED:
                try:
                    self.image = next(self.jump_throw_images_iter)
                    self.__last_animation_time = now
                    self.__origin_img = self.image
                    print('jump + throw')
                except StopIteration:
                    self.__in_throwing = False
        elif self.__in_throwing:
            if now - self.__last_animation_time > self.ANIMATION_SPEED:
                try:
                    self.image = next(self.throw_images_iter)
                    self.__last_animation_time = now
                    self.__origin_img = self.image
                    print(('throw'))
                except StopIteration:
                    self.__in_throwing = False
        elif self.__in_fighting:
            if now - self.__last_slow_animation_time > self.ANIMATION_SLOW_SPEED:
                try:
                    self.image = next(self.fight_images_iter)
                    self.__last_slow_animation_time = now
                    self.__origin_img = self.image
                    print('fight')
                except StopIteration:
                    self.__in_fighting = False
        elif self.__is_jumping():
            if now - self.__last_slow_animation_time > self.ANIMATION_SLOW_SPEED:
                try:
                    self.image = next(self.jump_images_iter)
                    self.__last_slow_animation_time = now
                    self.__origin_img = self.image
                    print('jump')
                except StopIteration:
                    pass
        elif self.__is_running():
            if now - self.__last_animation_time > self.ANIMATION_SPEED:
                self.image = next(self.walk_image_iter)
                self.__last_animation_time = now
                self.__origin_img = self.image
                self.__running_sound.play(maxtime=self.ANIMATION_SPEED)
                print('run')
        else:
            if now - self.__last_animation_time > self.ANIMATION_SPEED:
                self.image = next(self.idle_images_iter)
                self.__last_animation_time = now
                self.__origin_img = self.image
                print('idle')

        if self.__is_flip():
            self.image = pygame.transform.flip(self.__origin_img, True, False)

    def __moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.__vel.x = -self.__speed
            self.__acc.x = -0.1
            self.__facing = 180
        elif keys[pygame.K_RIGHT]:
            self.__vel.x = self.__speed
            self.__acc.x = 0.1
            self.__facing = 0
        else:
            self.__acc.x = 0
            self.__vel.x = 0

        self.__vel.y += self.__acc.y
        self.rect.move_ip(self.__vel.x, self.__vel.y)

        # kill enemy
        the_enemy = pygame.sprite.spritecollideany(self, self.__game.enemies)
        if self.__in_fighting and the_enemy:
            pygame.mixer.Sound('assets/sounds/hyuaa.wav').play()
            the_enemy.kill()
        elif the_enemy:
            self.__game.game_over()

        self.rect.bottom += 1  # two sprite touch don't consider as collide
        the_platform = pygame.sprite.spritecollideany(self, self.__game.platforms)
        self.rect.bottom -= 1
        # touch platform from top
        if the_platform:
            self.__acc.y = 0
            self.__vel.y = 0
            self.rect.bottom = the_platform.rect.top
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.__game.game_over()
        else:
            self.__acc.y = self.__gra

        # scroll screen
        if self.__is_moving_toward_right() and self.rect.left >= SCREEN_WIDTH // 2:
            self.__game.scroll(self.__vel.x)
            self.rect.left -= self.__vel.x

        # out of screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.__vel.x = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.__vel.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.__vel.y = 0

    def __is_moving_toward_right(self):
        return self.__vel.x > 0

    def __is_jumping(self):
        return self.__acc.y != 0

    def __is_running(self):
        return self.__vel.x != 0 or self.__acc.x != 0

    def __is_idle(self):
        return self.__vel.x == 0 and self.__vel.y == 0 and self.__acc.x == 0 and self.__acc.y == 0

    def __is_flip(self):
        return self.__facing == 180

    def throw(self):
        if self.__in_throwing:
            return

        self.__in_throwing = True
        self.throw_images_iter = iter(self.throw_images)
        if self.__is_jumping():
            self.jump_throw_images_iter = iter(self.jump_throw_images)

        if self.__is_flip():
            Kunai(self.__game, self.rect.left, self.rect.centery, False)
        else:
            Kunai(self.__game, self.rect.right, self.rect.centery, True)
        pygame.mixer.Sound('assets/sounds/throw.wav').play()

    def jump(self):
        if self.__is_jumping():
            return

        self.__vel.y = -20
        self.__acc.y = self.__gra

        self.jump_images_iter = iter(self.jump_images)
        if self.__in_fighting:
            self.jump_attack_images_iter = iter(self.jump_attack_images)
        pygame.mixer.Sound('assets/sounds/jump.wav').play()

    def fight(self):
        if self.__in_fighting:
            return

        self.__in_fighting = True
        self.fight_images_iter = iter(self.fight_images)
        if self.__is_jumping():
            self.jump_attack_images_iter = iter(self.jump_attack_images)
        pygame.mixer.Sound('assets/sounds/fight.wav').play()


class Kunai(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/ninjia/Kunai.png')

    def __init__(self, game, x, centery, facing_right, *groups):
        super().__init__(groups)
        self.game = game
        self.game.all_sprites.add(self)
        if facing_right:
            self.image = pygame.transform.rotozoom(self.image, -90, 0.5)
            self.rect = self.image.get_rect()
            self.rect.left = x
            self.speed = 15
        else:
            self.image = pygame.transform.rotozoom(self.image, 90, 0.5)
            self.rect = self.image.get_rect()
            self.rect.right = x
            self.speed = -15
        self.rect.centery = centery

    def update(self):
        self.rect.centerx += self.speed

        the_enemy = pygame.sprite.spritecollideany(self, self.game.enemies)
        if the_enemy:
            pygame.mixer.Sound('assets/sounds/hyuaa.wav').play()
            the_enemy.kill()

        if self.rect.left > SCREEN_WIDTH or self.rect.right < 0:
            self.kill()


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.scene_width = 0

        self.background = Background()
        self.ninja = Ninja(self, 0, 0)

        self.platforms = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.all_sprites.add(self.ninja, layer=1000)

        self.build_game()
        self.scroll(10)

    def start(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.ninja.throw()
                    elif event.key == pygame.K_UP:
                        self.ninja.jump()
                    elif event.key == pygame.K_a:
                        self.ninja.fight()

            self._draw()
            pygame.display.flip()

    def _draw(self):
        self.screen.blit(self.background.image, self.background.rect)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

    def game_over(self):
        GameOver(self)

    def game_win(self):
        pass

    def scroll(self, distance):
        for platform in self.platforms:
            platform.rect.x -= distance

            if platform.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(platform, layer=10)
            if platform.rect.right < 0:
                platform.kill()

        for decor in self.decorators:
            decor.rect.x -= distance

            if decor.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(decor, layer=1)
            if decor.rect.right < 0:
                decor.kill()

        for enemy in self.enemies:
            enemy.rect.x -= distance

            if enemy.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(enemy)
            if enemy.rect.right < 0:
                enemy.kill()

    def build_game(self):
        first_ground_tile = GrassPlatform(self, SCREEN_HEIGHT, 12, 1)
        Decorator(GrassPlatformDecoration).decor(first_ground_tile)
        self.all_sprites.add(first_ground_tile, layer=10)
        self.platforms.add(first_ground_tile)

        for i in range(5):
            Water(self, SCREEN_HEIGHT, 3, 1, self.decorators)
            grass_platform = GrassPlatform(self, SCREEN_HEIGHT, 3, 1, self.platforms)
            Decorator(GrassPlatformDecoration).decor(grass_platform)
            Bat(grass_platform.rect.centerx, grass_platform.rect.top - 200, self.enemies)

        water = Water(self, SCREEN_HEIGHT, 20, 1, self.decorators)
        for i in range(7):
            platform = GrassFloatPlatform(self, water.rect.left + i * 450, 600 - i * 50, 2, self.platforms)
            Decorator(GrassPlatformDecoration).decor(platform)
            Snake(platform.rect.centerx, platform.rect.top, self.enemies)


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()

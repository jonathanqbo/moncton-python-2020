import pygame
import itertools
from pygame_ninjia_settings import *


class Kunai(pygame.sprite.Sprite):

    image = pygame.image.load('assets/sprites/ninjia/Kunai.png')

    def __init__(self, game, x, y, direct_to_right, *groups):
        super().__init__(groups)
        self.game = game
        self.game.kunais.add(self)
        self.game.all_sprites.add(self)
        self.direct_to_right = direct_to_right
        if direct_to_right:
            self.image = pygame.transform.rotozoom(self.image, -90, 0.5)
            self.rect = self.image.get_rect()
            self.rect.left = x
        else:
            self.image = pygame.transform.rotozoom(self.image, 90, 0.5)
            self.rect = self.image.get_rect()
            self.rect.right = x
        self.rect.centery = y

    def update(self):
        the_enemy = pygame.sprite.spritecollideany(self, self.game.enemies)
        if the_enemy:
            pygame.mixer.Sound('assets/sounds/hyuaa.wav').play()
            the_enemy.kill()

        if self.direct_to_right:
            self.rect.left += 10
            if self.rect.left > SCREEN_WIDTH:
                self.kill()
        else:
            self.rect.right -= 10
            if self.rect.right < 0:
                self.kill()


class Ninjia(pygame.sprite.Sprite):

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
        self.__flip = False
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
                    self.__in_jumping = False
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
        if self.__is_jumping():
            self.jump_attack_images_iter = iter(self.jump_attack_images)
        else:
            self.fight_images_iter = iter(self.fight_images)

        pygame.mixer.Sound('assets/sounds/fight.wav').play()

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

        rect_origin = self.rect.copy()

        self.__vel.y += self.__acc.y
        # self.__vel += self.__acc
        self.rect.move_ip(self.__vel.x, self.__vel.y)

        the_enemy = pygame.sprite.spritecollideany(self, self.__game.enemies)
        if self.__in_fighting and the_enemy:
            pygame.mixer.Sound('assets/sounds/hyuaa.wav').play()
            the_enemy.kill()
        elif the_enemy:
            self.__game.game_over()

        self.rect.bottom += 1 # two sprite touch don't consider as collide
        the_platform = pygame.sprite.spritecollideany(self, self.__game.platforms)
        self.rect.bottom -= 1
        # touch platform from top
        if the_platform and self.__vel.y >= 0 and rect_origin.bottom <= the_platform.rect.top:
            self.__acc.y = 0
            self.__vel.y = 0
            self.rect.bottom = the_platform.rect.top
        # touch platform from bottom
        elif the_platform and self.__vel.y < 0 and rect_origin.top >= the_platform.rect.bottom:
            self.__acc.y = self.__gra
            self.__vel.y = 0
            self.rect.top = the_platform.rect.bottom
            self.rect.left -= self.__vel.x
        # touch platform from left/right
        elif the_platform:
            self.rect.left -= self.__vel.x
            self.__vel.x = 0
            # if self.rect.bottom < self.__game.ground.rect.top:
            #     self.__acc.y = self.__gra
        elif self.rect.bottom >= SCREEN_HEIGHT:
            # self.__acc.y = 0
            # self.__vel.y = 0
            # self.rect.bottom = self.__game.ground.rect.top
            self.__game.game_over()
        else:
            self.__acc.y = self.__gra

        if self.__is_moving_toward_right() and self.rect.left >= SCREEN_WIDTH // 2:
            self.__game.scroll(self.__vel.x)
            self.rect.left -= self.__vel.x

        if self.rect.left < 0:
            self.rect.left = 0
            self.__vel.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.__vel.y = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.__vel.y = 0
            # self.__game.game_over()

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
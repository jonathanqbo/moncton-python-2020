import pygame
import itertools


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

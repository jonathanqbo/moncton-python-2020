import pygame
import random
from pygame_ninjia_settings import *


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


class DesertPlatformDecoration(pygame.sprite.Sprite):
    images_decor = [
        pygame.image.load('assets/desert/Objects/Bush (1).png'),
        pygame.image.load('assets/desert/Objects/Bush (2).png'),
        # pygame.image.load('assets/desert/Objects/Crate.png'),
        pygame.image.load('assets/desert/Objects/Stone.png'),
        # pygame.image.load('assets/desert/Objects/Sign.png'),
        # pygame.image.load('assets/desert/Objects/SignArrow.png'),
        pygame.image.load('assets/desert/Objects/Skeleton.png'),
        # pygame.image.load('assets/desert/Objects/StoneBlock.png'),
        pygame.image.load('assets/desert/Objects/Tree.png'),
        pygame.image.load('assets/desert/Objects/Cactus (1).png'),
        pygame.image.load('assets/desert/Objects/Cactus (2).png'),
        pygame.image.load('assets/desert/Objects/Cactus (3).png'),
        pygame.image.load('assets/desert/Objects/Grass (1).png'),
        pygame.image.load('assets/desert/Objects/Grass (2).png'),
    ]

    def __init__(self, left, bottom, *groups):
        super().__init__(groups)
        self.image = random.choice(self.images_decor)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom


class SnowPlatformDecoration(pygame.sprite.Sprite):
    igloo = pygame.image.load('assets/wintersnow/Object/Igloo.png')
    snowman = pygame.image.load('assets/wintersnow/Object/SnowMan.png')
    direction_sigh = pygame.image.load('assets/wintersnow/Object/Sign_2.png')
    images_decor = [
        pygame.image.load('assets/wintersnow/Object/Stone.png'),
        # pygame.image.load('assets/wintersnow/Object/Crate.png'),
        # pygame.image.load('assets/wintersnow/Object/IceBox.png'),
        pygame.image.load('assets/wintersnow/Object/Tree_1.png'),
        pygame.image.load('assets/wintersnow/Object/Crystal.png'),
        pygame.image.load('assets/wintersnow/Object/Tree_2.png')
    ]

    def __init__(self, left, bottom, *groups):
        super().__init__(groups)
        self.image = self.__random_image()
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def __random_image(self):
        percent = random.randrange(0, 100)
        if percent < 5:
            return self.igloo
        elif percent < 10:
            return self.snowman
        elif percent < 15:
            return self.direction_sigh
        else:
            return random.choice(self.images_decor)


class GroundTile(pygame.sprite.Sprite):
    def __init__(self, game, width, height, *groups):
        super().__init__(groups)
        self.game = game
        self.image = self.__create_platform(width, height)
        self.rect = self.image.get_rect()
        self.rect.left = self.game.scene_width
        self.rect.bottom = SCREEN_HEIGHT
        self.game.scene_width += self.rect.width - 15  # there is a gap in each image

    def update(self):
        if self.rect.right < 0:
            self.kill()

    def __create_platform(self, width, height):
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

    def __init__(self, game, width, height, *groups):
        super().__init__(game, width, height, *groups)

        for i in range(width):
            if random.randrange(0, 100) < 20:
                continue

            decor = GrassPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                            self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.lfet


class DesertPlatform(GroundTile):
    image_top_left = pygame.image.load(f'assets/desert/Tile/1.png')
    image_top_middle = pygame.image.load(f'assets/desert/Tile/2.png')
    image_top_right = pygame.image.load(f'assets/desert/Tile/3.png')
    image_bottom_left = pygame.image.load(f'assets/desert/Tile/4.png')
    image_bottom_middle = pygame.image.load(f'assets/desert/Tile/5.png')
    image_bottom_right = pygame.image.load(f'assets/desert/Tile/6.png')

    def __init__(self, game, width, height, *groups):
        super().__init__(game, width, height, *groups)

        for i in range(width):
            if random.randrange(0, 100) < 20:
                continue

            decor = DesertPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                            self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.lfet


class SnowPlatform(GroundTile):
    image_top_left = pygame.image.load(f'assets/wintersnow/Tiles/1.png')
    image_top_middle = pygame.image.load(f'assets/wintersnow/Tiles/2.png')
    image_top_right = pygame.image.load(f'assets/wintersnow/Tiles/3.png')
    image_bottom_left = pygame.image.load(f'assets/wintersnow/Tiles/4.png')
    image_bottom_middle = pygame.image.load(f'assets/wintersnow/Tiles/5.png')
    image_bottom_right = pygame.image.load(f'assets/wintersnow/Tiles/6.png')

    def __init__(self, game, width, height, *groups):
        super().__init__(game, width, height, *groups)

        for i in range(width):
            if random.randrange(0, 100) < 20:
                continue

            decor = SnowPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                            self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.lfet


class Water(GroundTile):
    image_top_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_bottom_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')


# class Sand(GroundTile):
#     image_top_left = pygame.image.load(f'assets/desert/Tile/')
#     image_top_middle = pygame.image.load(f'assets/desert/Tile/')
#     image_top_right = pygame.image.load(f'assets/desert/Tile/')
#     image_bottom_left = pygame.image.load(f'assets/desert/Tile/')
#     image_bottom_middle = pygame.image.load(f'assets/desert/Tile/')
#     image_bottom_right = pygame.image.load(f'assets/desert/Tile/')


class Lava(GroundTile):
    image_top_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_top_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/17.png')
    image_bottom_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')
    image_bottom_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/18.png')


class FloatTile(pygame.sprite.Sprite):

    def __init__(self, game, left, bottom, length, *groups):
        if length < 2:
            raise ValueError('The length of float platform need be >= 2')

        super().__init__(groups)
        self.game = game
        width = self.image_left.get_rect().width * length
        height = self.image_left.get_rect().height
        self.image = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        self.image.blit(self.image_left, (0, 0))
        x = self.image_left.get_rect().width
        if length > 2:
            for i in range(1, length - 1):
                self.image.blit(self.image_middle, (x, 0))
                x += self.image_middle.get_rect().width
        self.image.blit(self.image_right, (x, 0))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def update(self):
        if self.rect.right < 0:
            self.kill()


class GrassFloatPlatform(FloatTile):
    image_left = pygame.image.load('assets/grass/grass_ground_Tiles/13.png')
    image_middle = pygame.image.load('assets/grass/grass_ground_Tiles/14.png')
    image_right = pygame.image.load('assets/grass/grass_ground_Tiles/15.png')

    def __init__(self, game, left, bottom, length, *groups):
        super().__init__(game, left, bottom, length, *groups)

        for i in range(length):
            if random.randrange(0, 100) < 20:
                continue

            decor = GrassPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                   self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.left


class SandFloatPlatform(FloatTile):
    image_left = pygame.image.load('assets/desert/Tile/14.png')
    image_middle = pygame.image.load('assets/desert/Tile/15.png')
    image_right = pygame.image.load('assets/desert/Tile/16.png')

    def __init__(self, game, left, bottom, length, *groups):
        super().__init__(game, left, bottom, length, *groups)

        for i in range(length):
            if random.randrange(0, 100) < 20:
                continue

            decor = DesertPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                            self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.left


class SnowFloatPlatform(FloatTile):
    image_left = pygame.image.load('assets/wintersnow/Tiles/14.png')
    image_middle = pygame.image.load('assets/wintersnow/Tiles/15.png')
    image_right = pygame.image.load('assets/wintersnow/Tiles/16.png')

    def __init__(self, game, left, bottom, length, *groups):
        super().__init__(game, left, bottom, length, *groups)

        for i in range(length):
            if random.randrange(0, 100) < 20:
                continue

            decor = SnowPlatformDecoration(random.randint(self.rect.left, self.rect.right), self.rect.top,
                                            self.game.decorators)
            if decor.rect.right > self.rect.right:
                decor.rect.right = self.rect.right
            if decor.rect.left < self.rect.left:
                decor.rect.left = self.rect.left

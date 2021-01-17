import pygame

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


class GroundTile(pygame.sprite.Sprite):
    image_top_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/1.png')
    image_top_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/2.png')
    image_top_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/3.png')
    image_bottom_left = pygame.image.load(f'assets/grass/grass_ground_Tiles/4.png')
    image_bottom_middle = pygame.image.load(f'assets/grass/grass_ground_Tiles/5.png')
    image_bottom_right = pygame.image.load(f'assets/grass/grass_ground_Tiles/6.png')

    def __init__(self, game, left, bottom, width, height, *groups):
        super().__init__(groups)
        self.game = game
        self.image = self.__create_platform(width, height)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def update(self):
        pass

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


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.background = Background()
        self.ground = GroundTile(self, 0, SCREEN_HEIGHT, 12, 2);

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.all_sprites.add(self.ground)

    def start(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background.image, self.background.rect)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

    def game_over(self):
        pass

    def game_win(self):
        pass


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()

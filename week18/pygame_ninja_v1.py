from week19.pygame_ninjia_level import *

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


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.background = GrassBackground()
        self.all_sprites = pygame.sprite.LayeredUpdates()

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

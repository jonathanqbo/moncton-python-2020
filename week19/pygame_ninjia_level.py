from week19.pygame_ninjia_tiles import *
from week19.pygame_ninjia_enemies import *
from week19.pygame_ninjia_ninjia import *


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
        self.__game.all_sprites.remove(self.__game.ninjia)
        self.__game.all_sprites.add(self)
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.__game._draw()
            pygame.display.flip()


class GameWin(pygame.sprite.Sprite):

    origin_image = pygame.image.load('assets/sprites/ninjia/Idle__000.png')

    def __init__(self, game):
        super().__init__()
        self.__game = game
        self.image = pygame.transform.rotozoom(self.origin_image, 0, 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.__zoom = 0.5
        self.__last_animation_time = pygame.time.get_ticks()

        pygame.time.wait(1000)
        self.__show_win_screen()

    def update(self):
        if self.__zoom < 0.8:
            now = pygame.time.get_ticks()
            if now - self.__last_animation_time > 500:
                self.__zoom += 0.1
                self.image = pygame.transform.rotozoom(self.origin_image, 0, self.__zoom)
                self.rect = self.image.get_rect()
                self.rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                self.__last_animation_time = now

    def __show_win_screen(self):
        running = True
        clock = pygame.time.Clock()
        self.__game.all_sprites.empty()
        self.__game.all_sprites.add(self)
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__game._draw()
            pygame.display.flip()


class GameWinSign(pygame.sprite.Sprite):

    image1 = pygame.image.load('assets/tiles/tochLit.png')
    image2 = pygame.image.load('assets/tiles/tochLit2.png')

    def __init__(self, game, left, bottom, *groups):
        super().__init__(groups)
        self.__game = game
        self.images_iter = itertools.cycle([self.image1, self.image2])
        self.image = next(self.images_iter)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.__last_animation_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_animation_time > 200:
            self.image = next(self.images_iter)
            self.__last_animation_time = now

        if self.rect.colliderect(self.__game.ninjia.rect):
            GameWin(self.__game)

    def __show_win_screen(self):
        running = True
        origin_ninjia_image = self.__game.ninjia.image
        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__game.ninjia.image = pygame.transform.rotozoom(origin_ninjia_image, 0, 1.1)
            self.__game._draw()
            pygame.display.flip()


class NextLevelSign(pygame.sprite.Sprite):

    image = pygame.image.load('assets/tiles/signExit.png')

    def __init__(self, game, left, bottom, *groups):
        super().__init__(groups)
        self.__game = game
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def update(self):
        if self.rect.colliderect(self.__game.ninjia.rect):
            self.__game.next_level()


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image.blit(self.origin_image, (0, 0))
        self.image.blit(self.origin_image, (self.origin_image.get_rect().width, 0))

        self.rect = self.image.get_rect()
        self.rect2 = self.rect.copy()
        self.__scroll_distance = 0
        pygame.mixer.stop()
        pygame.mixer.Sound('assets/sounds/bg_music_ninjia.wav').play(loops=-1)

    def scroll(self, distance):
        self.rect.move_ip(distance, 0)
        if self.rect.left >= SCREEN_WIDTH:
            self.rect = self.rect2.copy()
            self.rect

    def draw(self, screen):
        if self.__scroll_distance >= 0:
            screen.blit(self.image, (self.__scroll_distance, 0))
            screen.blit(self.image, (SCREEN_WIDTH-self.__scroll_distance, 0))


class SnowBackground(Background):
    origin_image = pygame.image.load(f'assets/wintersnow/BG/BG.png')


class DesertBackground(Background):
    origin_image = pygame.image.load(f'assets/desert/BG.png')


class GrassBackground(Background):
    origin_image = pygame.image.load(f'assets/grass/BG/BG.png')


class Level:

    def __init__(self, game):
        self._game = game

        self.scene_width = 0
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.kunais = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()

        self.background = None
        self.ninjia = None

    def start(self):
        self._build()
        self.scroll(20)
        self.__run()

    def next_level(self):
        self._game.next_level()

    def game_over(self):
        GameOver(self)

    def scroll(self, distance):
        for platform in self.platforms:
            platform.rect.x -= distance

            if platform.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(platform)
            if platform.rect.right < 0:
                platform.kill()

        for decor in self.decorators:
            decor.rect.x -= distance

            if decor.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(decor)
            if decor.rect.right < 0:
                decor.kill()

        for enemy in self.enemies:
            enemy.rect.x -= distance

            if enemy.rect.left <= SCREEN_WIDTH + 100:
                self.all_sprites.add(enemy)
            if enemy.rect.right < 0:
                enemy.kill()

    def _build(self):
        pass

    def __run(self):
        running = True
        while running:
            self._game.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.ninjia.fight()
                    elif event.key == pygame.K_s:
                        self.ninjia.throw()
                    elif event.key == pygame.K_UP:
                        self.ninjia.jump()

            self._draw()
            pygame.display.flip()

    def _draw(self):
        self._game.screen.blit(self.background.image, self.background.rect)
        self.all_sprites.update()
        self.all_sprites.draw(self._game.screen)


class Level1(Level):

    def _build(self):
        self.background = GrassBackground()

        platform = GrassPlatform(self, 10, 1, self.platforms, self.all_sprites)
        self.ninjia = Ninjia(self, 0, platform.rect.top)
        # to make Ninjin always stay in top layer
        self.all_sprites.add(self.ninjia, layer=1000)

        water = Water(self, 20, 1, self.decorators)
        platform = GrassFloatPlatform(self, water.rect.left + 150, 550, 3, self.platforms)
        platform = GrassFloatPlatform(self, platform.rect.right + 150, 650, 3, self.platforms)
        platform = GrassFloatPlatform(self, platform.rect.right + 150, 450, 3, self.platforms)
        platform = GrassFloatPlatform(self, platform.rect.right + 100, 250, 3, self.platforms)
        platform = GrassFloatPlatform(self, platform.rect.right + 100, 350, 3, self.platforms)
        #
        platform = GrassPlatform(self, 20, 3, self.platforms)
        for i in range(1, 5):
            Bat(platform.rect.left + i * 250, random.randint(70, platform.rect.top - 70), self.enemies)
            Snake(platform.rect.left + i * 250, platform.rect.top, self.enemies)

        NextLevelSign(self, platform.rect.right - 100, platform.rect.top, self.decorators)


class Level2(Level):

    def _build(self):
        self.background = DesertBackground()

        platform = DesertPlatform(self, 10, 1, self.platforms, self.all_sprites)
        self.ninjia = Ninjia(self, 0, platform.rect.top)
        # to make Ninjin always stay in top layer
        self.all_sprites.add(self.ninjia, layer=1000)

        SandFloatPlatform(self, platform.rect.left + 150, 300, 3, self.platforms)
        SandFloatPlatform(self, platform.rect.left + 700, 500, 4, self.platforms)

        water = Water(self, 3, 1, self.decorators)
        platform = SandFloatPlatform(self, water.rect.left + 150, 500, 3, self.platforms)
        platform = SandFloatPlatform(self, platform.rect.right + 150, 450, 3, self.platforms)
        platform = SandFloatPlatform(self, platform.rect.right + 150, 350, 3, self.platforms)
        platform = SandFloatPlatform(self, platform.rect.right + 100, 250, 3, self.platforms)
        platform = SandFloatPlatform(self, platform.rect.right + 100, 350, 3, self.platforms)

        platform = DesertPlatform(self, 40, 1, self.platforms)
        for i in range(1, 5):
            Bee(platform.rect.left + i * 250, random.randint(70, platform.rect.top - 70), self.enemies)
            Bat(platform.rect.left + i * 350, random.randint(70, platform.rect.top - 70), self.enemies)
            Spider(platform.rect.left + i * 250, platform.rect.top, self.enemies)
            Ladybug(platform.rect.left + i * 350, platform.rect.top, self.enemies)

        NextLevelSign(self, platform.rect.right - 100, platform.rect.top, self.decorators)


class Level3(Level):

    def _build(self):
        self.background = SnowBackground()

        platform = SnowPlatform(self, 10, 1, self.platforms, self.all_sprites)
        self.ninjia = Ninjia(self, 0, platform.rect.top)
        # to make Ninjin always stay in top layer
        self.all_sprites.add(self.ninjia, layer=1000)

        # for _ in range(5):
        #     Water(self, 3, 1, self.decorators)
        #     platform = Platform(self, 3, 1, self.platforms)
        #
        water = Water(self, 3, 1, self.decorators)
        platform = SnowFloatPlatform(self, water.rect.left + 150, 550, 3, self.platforms)
        platform = SnowFloatPlatform(self, platform.rect.right + 150, 450, 3, self.platforms)
        platform = SnowFloatPlatform(self, platform.rect.right + 150, 350, 3, self.platforms)
        platform = SnowFloatPlatform(self, platform.rect.right + 100, 250, 3, self.platforms)
        platform = SnowFloatPlatform(self, platform.rect.right + 100, 350, 3, self.platforms)
        #
        # platform = GrassPlatform(self, 20, 3, self.platforms)
        # for i in range(1, 5):
        #     Bat(platform.rect.left + i * 250, random.randint(70, platform.rect.top - 70), self.enemies)
        #     Snake(platform.rect.left + i * 250, platform.rect.top, self.enemies)

        platform = SnowPlatform(self, 20, 1, self.platforms)
        # for i in range(1, 5):
        #     Bat(platform.rect.left + i * 250, random.randint(70, platform.rect.top - 70), self.enemies)
        #     Spider(platform.rect.left + i * 250, platform.rect.top, self.enemies)

        GameWinSign(self, platform.rect.right - 200, platform.rect.top, self.decorators)


#     # platform = Platform(self, 6, 2, self.platforms)
    #     # Snail(platform.rect.centerx, platform.rect.top, self.enemies)
    #     #
    #     # Water(self, 3, 1, self.bottoms)
    #     #
    #     # platform = Platform(self, 6, 2, self.platforms)
    #     # Snail(platform.rect.centerx, platform.rect.top, self.enemies)
    #     #
    #     # Water(self, 3, 1, self.bottoms)
    #     #
    #     # platform = Platform(self, 6, 2, self.platforms)
    #     # Snake(platform.rect.centerx, platform.rect.top, self.enemies)
    #     #
    #     # Water(self, 4, 1, self.bottoms)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Mouse(platform.rect.centerx, platform.rect.top, self.enemies)
    #     #
    #     # Lava(self, 2, 1, self.bottoms)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     # Bat(platform.rect.centerx, platform.rect.top -100, self.enemies)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     # Bat(platform.rect.centerx, platform.rect.top - 100, self.enemies)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     # Bat(platform.rect.centerx, platform.rect.top - 100, self.enemies)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     # Bat(platform.rect.centerx, platform.rect.top - 100, self.enemies)
    #     #
    #     # platform = Platform(self, 5, 3, self.platforms)
    #     # Ladybug(platform.rect.centerx, platform.rect.top, self.enemies)
    #     # Bat(platform.rect.centerx, platform.rect.top - 100, self.enemies)
    #
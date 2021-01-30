from pygame_ninjia_level import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.levels = []
        self.levels.append(Level1(self))
        self.levels.append(Level2(self))
        self.levels.append(Level3(self))
        self.levels_iter = iter(self.levels)
        self.cur_level = next(self.levels_iter)

    def start(self):
        self.cur_level.start()

    def next_level(self):
        try:
            next(self.levels_iter).start()
        except StopIteration:
            self.game_win()

    def game_win(self):
        pass


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()

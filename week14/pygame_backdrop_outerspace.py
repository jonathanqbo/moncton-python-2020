import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load('assets/backdrops/space.png')
    screen.blit(background, background.get_rect())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()

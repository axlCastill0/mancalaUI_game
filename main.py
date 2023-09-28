import pygame, Puit

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_sprite = pygame.image.load("img/mancala_board.png").convert_alpha()


run = True
while run:

    screen.blit(board_sprite, (100, 85))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
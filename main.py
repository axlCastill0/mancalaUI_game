import pygame, Puit

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_sprite = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_sprite.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

run = True
while run:

    screen.blit(board_sprite, board_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
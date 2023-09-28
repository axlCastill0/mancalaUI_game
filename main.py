import pygame, Pit

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_img = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
red_pit_4 = pygame.image.load("img/red_4.png")

pits = pygame.sprite.Group()

pit1 = Pit.Pit("A", 151, 115, 4, red_pit_4)

pits.add(pit1)

run = True
while run:

    screen.blit(board_img, board_rect)

    pit1.draw(board_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
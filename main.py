import pygame, Pit

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

RED_PIT_HEIGHT = 115
BLUE_PIT_HEIGHT = 301
PIT_WIDTH_COORDS = [151, 252, 353, 454, 550, 647]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_img = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
red_pit_4 = pygame.image.load("img/red_4.png")
blue_pit_4 = pygame.image.load("img/blue_4.png")

pits = pygame.sprite.Group()

pit1 = Pit.Pit("A", PIT_WIDTH_COORDS[0], RED_PIT_HEIGHT, 4, red_pit_4)
pit2 = Pit.Pit("B", PIT_WIDTH_COORDS[1], RED_PIT_HEIGHT, 4, red_pit_4)
pit3 = Pit.Pit("C", PIT_WIDTH_COORDS[0], BLUE_PIT_HEIGHT, 4, blue_pit_4)

pits.add(pit1)
pits.add(pit2)
pits.add(pit3)

run = True
while run:

    screen.blit(board_img, board_rect)

    pit1.draw(board_img)
    pit2.draw(board_img)
    pit3.draw(board_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
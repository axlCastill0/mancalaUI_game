import pygame, Pit, Mancala_UI

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

pit_array = []

pit0 = Pit.Pit("A", PIT_WIDTH_COORDS[0], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit1 = Pit.Pit("B", PIT_WIDTH_COORDS[1], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit2 = Pit.Pit("C", PIT_WIDTH_COORDS[2], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit3 = Pit.Pit("D", PIT_WIDTH_COORDS[3], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit4 = Pit.Pit("E", PIT_WIDTH_COORDS[4], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit5 = Pit.Pit("F", PIT_WIDTH_COORDS[5], BLUE_PIT_HEIGHT, 4, blue_pit_4)
#pit6 = 
pit7 = Pit.Pit("H", PIT_WIDTH_COORDS[5], RED_PIT_HEIGHT, 4, red_pit_4)
pit8 = Pit.Pit("I", PIT_WIDTH_COORDS[4], RED_PIT_HEIGHT, 4, red_pit_4)
pit9 = Pit.Pit("J", PIT_WIDTH_COORDS[3], RED_PIT_HEIGHT, 4, red_pit_4)
pit10 = Pit.Pit("K", PIT_WIDTH_COORDS[2], RED_PIT_HEIGHT, 4, red_pit_4)
pit11 = Pit.Pit("L", PIT_WIDTH_COORDS[1], RED_PIT_HEIGHT, 4, red_pit_4)
pit12 = Pit.Pit("M", PIT_WIDTH_COORDS[0], RED_PIT_HEIGHT, 4, red_pit_4)

pit_array.append(pit0)
pit_array.append(pit1)
pit_array.append(pit2)
pit_array.append(pit3)
pit_array.append(pit4)
pit_array.append(pit5)

pit_array.append(pit7)
pit_array.append(pit8)
pit_array.append(pit9)
pit_array.append(pit10)
pit_array.append(pit11)
pit_array.append(pit12)

pits = Mancala_UI.Pits(pit_array)

run = True
while run:

    screen.blit(board_img, board_rect)

    pits.draw(board_img)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
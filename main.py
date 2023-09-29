import pygame, Pit, Mancala_UI

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

RED_PIT_HEIGHT = 115 + (SCREEN_HEIGHT - 416)/2
BLUE_PIT_HEIGHT = 301 + (SCREEN_HEIGHT - 416)/2
PIT_WIDTH_COORDS = [151 + (SCREEN_WIDTH - 800)/2, 
                    252 + (SCREEN_WIDTH - 800)/2,
                    353 + (SCREEN_WIDTH - 800)/2,
                    454 + (SCREEN_WIDTH - 800)/2,
                    550 + (SCREEN_WIDTH - 800)/2,
                    647 + (SCREEN_WIDTH - 800)/2]
POINT_PIT_HEIGHT = SCREEN_HEIGHT/2
POINT_PIT_WIDTH = [742 + (SCREEN_WIDTH - 800)/2,
                   59 + (SCREEN_WIDTH - 800)/2]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_img = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

red_pit_e = pygame.image.load("img/red_empty.png")
red_pit_1 = pygame.image.load("img/red_1.png")
red_pit_2 = pygame.image.load("img/red_2.png")
red_pit_3 = pygame.image.load("img/red_3.png")
red_pit_4 = pygame.image.load("img/red_4.png")
red_pit_5 = pygame.image.load("img/red_5.png")
red_pit_6 = pygame.image.load("img/red_6.png")
red_pit_f = pygame.image.load("img/red_full.png")

red_point_e = pygame.image.load("img/rpoint_empty.png")
red_point_1 = pygame.image.load("img/rpoint_1.png")
red_point_2 = pygame.image.load("img/rpoint_2.png")
red_point_3 = pygame.image.load("img/rpoint_3.png")
red_point_4 = pygame.image.load("img/rpoint_4.png")
red_point_5 = pygame.image.load("img/rpoint_5.png")
red_point_6 = pygame.image.load("img/rpoint_6.png")
red_point_7 = pygame.image.load("img/rpoint_7.png")
red_point_8 = pygame.image.load("img/rpoint_8.png")
red_point_9 = pygame.image.load("img/rpoint_9.png")
red_point_10 = pygame.image.load("img/rpoint_10.png")
red_point_f = pygame.image.load("img/rpoint_full.png")

blue_pit_e = pygame.image.load("img/blue_empty.png")
blue_pit_1 = pygame.image.load("img/blue_1.png")
blue_pit_2 = pygame.image.load("img/blue_2.png")
blue_pit_3 = pygame.image.load("img/blue_3.png")
blue_pit_4 = pygame.image.load("img/blue_4.png")
blue_pit_5 = pygame.image.load("img/blue_5.png")
blue_pit_6 = pygame.image.load("img/blue_6.png")
blue_pit_f = pygame.image.load("img/blue_full.png")

blue_point_e = pygame.image.load("img/bpoint_empty.png")
blue_point_1 = pygame.image.load("img/bpoint_1.png")
blue_point_2 = pygame.image.load("img/bpoint_2.png")
blue_point_3 = pygame.image.load("img/bpoint_3.png")
blue_point_4 = pygame.image.load("img/bpoint_4.png")
blue_point_5 = pygame.image.load("img/bpoint_5.png")
blue_point_6 = pygame.image.load("img/bpoint_6.png")
blue_point_7 = pygame.image.load("img/bpoint_7.png")
blue_point_8 = pygame.image.load("img/bpoint_8.png")
blue_point_9 = pygame.image.load("img/bpoint_9.png")
blue_point_10 = pygame.image.load("img/bpoint_10.png")
blue_point_f = pygame.image.load("img/bpoint_full.png")

pit_array = []

pit0 = Pit.Pit("A", PIT_WIDTH_COORDS[0], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit1 = Pit.Pit("B", PIT_WIDTH_COORDS[1], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit2 = Pit.Pit("C", PIT_WIDTH_COORDS[2], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit3 = Pit.Pit("D", PIT_WIDTH_COORDS[3], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit4 = Pit.Pit("E", PIT_WIDTH_COORDS[4], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit5 = Pit.Pit("F", PIT_WIDTH_COORDS[5], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit6 = Pit.Pit("G", POINT_PIT_WIDTH[0], POINT_PIT_HEIGHT, 0, blue_point_e)
pit7 = Pit.Pit("H", PIT_WIDTH_COORDS[5], RED_PIT_HEIGHT, 4, red_pit_4)
pit8 = Pit.Pit("I", PIT_WIDTH_COORDS[4], RED_PIT_HEIGHT, 4, red_pit_4)
pit9 = Pit.Pit("J", PIT_WIDTH_COORDS[3], RED_PIT_HEIGHT, 4, red_pit_4)
pit10 = Pit.Pit("K", PIT_WIDTH_COORDS[2], RED_PIT_HEIGHT, 4, red_pit_4)
pit11 = Pit.Pit("L", PIT_WIDTH_COORDS[1], RED_PIT_HEIGHT, 4, red_pit_4)
pit12 = Pit.Pit("M", PIT_WIDTH_COORDS[0], RED_PIT_HEIGHT, 4, red_pit_4)
pit13 = Pit.Pit("N", POINT_PIT_WIDTH[1], POINT_PIT_HEIGHT, 0, red_point_e)

pit_array.append(pit0)
pit_array.append(pit1)
pit_array.append(pit2)
pit_array.append(pit3)
pit_array.append(pit4)
pit_array.append(pit5)
pit_array.append(pit6)
pit_array.append(pit7)
pit_array.append(pit8)
pit_array.append(pit9)
pit_array.append(pit10)
pit_array.append(pit11)
pit_array.append(pit12)
pit_array.append(pit13)

pits = Mancala_UI.Pits(pit_array)

run = True
while run:
    
    screen.blit(board_img, board_rect)

    pits.draw(screen)

    if pit0.action() == True :
        print("hello")
    if pit1.action() == True :
        print(pit1.seeds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
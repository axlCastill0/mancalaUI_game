import pygame, Pit, Mancala_UI, Mancala

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

RED_PIT_HEIGHT = 115 + (SCREEN_HEIGHT - 416)/2
BLUE_PIT_HEIGHT = 301 + (SCREEN_HEIGHT - 416)/2
PIT_WIDTH_COORDS = [151 + (SCREEN_WIDTH - 800)/2, 
                    252 + (SCREEN_WIDTH - 800)/2,
                    353 + (SCREEN_WIDTH - 800)/2,
                    452 + (SCREEN_WIDTH - 800)/2,
                    550 + (SCREEN_WIDTH - 800)/2,
                    647 + (SCREEN_WIDTH - 800)/2]
POINT_PIT_HEIGHT = SCREEN_HEIGHT/2
POINT_PIT_WIDTH = [742 + (SCREEN_WIDTH - 800)/2,
                   59 + (SCREEN_WIDTH - 800)/2]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Axl Castillo / Thomas Journault")

board_img = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

red_pit_0 = pygame.image.load("img/red_empty.png")
red_pit_1 = pygame.image.load("img/red_1.png")
red_pit_2 = pygame.image.load("img/red_2.png")
red_pit_3 = pygame.image.load("img/red_3.png")
red_pit_4 = pygame.image.load("img/red_4.png")
red_pit_5 = pygame.image.load("img/red_5.png")
red_pit_6 = pygame.image.load("img/red_6.png")
red_pit_f = pygame.image.load("img/red_full.png")

red_point_0 = pygame.image.load("img/rpoint_empty.png")
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

blue_pit_0 = pygame.image.load("img/blue_empty.png")
blue_pit_1 = pygame.image.load("img/blue_1.png")
blue_pit_2 = pygame.image.load("img/blue_2.png")
blue_pit_3 = pygame.image.load("img/blue_3.png")
blue_pit_4 = pygame.image.load("img/blue_4.png")
blue_pit_5 = pygame.image.load("img/blue_5.png")
blue_pit_6 = pygame.image.load("img/blue_6.png")
blue_pit_f = pygame.image.load("img/blue_full.png")

blue_point_0 = pygame.image.load("img/bpoint_empty.png")
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

red_pit_img_array = []
red_pit_img_array.append(red_pit_0)
red_pit_img_array.append(red_pit_1)
red_pit_img_array.append(red_pit_2)
red_pit_img_array.append(red_pit_3)
red_pit_img_array.append(red_pit_4)
red_pit_img_array.append(red_pit_5)
red_pit_img_array.append(red_pit_6)
red_pit_img_array.append(red_pit_f)

blue_pit_img_array = []
blue_pit_img_array.append(blue_pit_0)
blue_pit_img_array.append(blue_pit_1)
blue_pit_img_array.append(blue_pit_2)
blue_pit_img_array.append(blue_pit_3)
blue_pit_img_array.append(blue_pit_4)
blue_pit_img_array.append(blue_pit_5)
blue_pit_img_array.append(blue_pit_6)
blue_pit_img_array.append(blue_pit_f)

red_point_img_array = []
red_point_img_array.append(red_point_0)
red_point_img_array.append(red_point_1)
red_point_img_array.append(red_point_2)
red_point_img_array.append(red_point_3)
red_point_img_array.append(red_point_4)
red_point_img_array.append(red_point_5)
red_point_img_array.append(red_point_6)
red_point_img_array.append(red_point_7)
red_point_img_array.append(red_point_8)
red_point_img_array.append(red_point_9)
red_point_img_array.append(red_point_10)
red_point_img_array.append(red_point_f)

blue_point_img_array = []
blue_point_img_array.append(blue_point_0)
blue_point_img_array.append(blue_point_1)
blue_point_img_array.append(blue_point_2)
blue_point_img_array.append(blue_point_3)
blue_point_img_array.append(blue_point_4)
blue_point_img_array.append(blue_point_5)
blue_point_img_array.append(blue_point_6)
blue_point_img_array.append(blue_point_7)
blue_point_img_array.append(blue_point_8)
blue_point_img_array.append(blue_point_9)
blue_point_img_array.append(blue_point_10)
blue_point_img_array.append(blue_point_f)

pit_array = []

pit0 = Pit.Pit(0, PIT_WIDTH_COORDS[0], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit1 = Pit.Pit(1, PIT_WIDTH_COORDS[1], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit2 = Pit.Pit(2, PIT_WIDTH_COORDS[2], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit3 = Pit.Pit(3, PIT_WIDTH_COORDS[3], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit4 = Pit.Pit(4, PIT_WIDTH_COORDS[4], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit5 = Pit.Pit(5, PIT_WIDTH_COORDS[5], BLUE_PIT_HEIGHT, 4, blue_pit_4)
pit6 = Pit.Pit(6, POINT_PIT_WIDTH[0], POINT_PIT_HEIGHT, 0, blue_point_0)
pit7 = Pit.Pit(7, PIT_WIDTH_COORDS[5], RED_PIT_HEIGHT, 4, red_pit_4)
pit8 = Pit.Pit(8, PIT_WIDTH_COORDS[4], RED_PIT_HEIGHT, 4, red_pit_4)
pit9 = Pit.Pit(9, PIT_WIDTH_COORDS[3], RED_PIT_HEIGHT, 4, red_pit_4)
pit10 = Pit.Pit(10, PIT_WIDTH_COORDS[2], RED_PIT_HEIGHT, 4, red_pit_4)
pit11 = Pit.Pit(11, PIT_WIDTH_COORDS[1], RED_PIT_HEIGHT, 4, red_pit_4)
pit12 = Pit.Pit(12, PIT_WIDTH_COORDS[0], RED_PIT_HEIGHT, 4, red_pit_4)
pit13 = Pit.Pit(13, POINT_PIT_WIDTH[1], POINT_PIT_HEIGHT, 0, red_point_0)

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

mancala = Mancala.Mancala([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])

def updateGameInterface() :
    grid = mancala.grid
    for i in range(7) :
        if (grid[i] > 6) :
            if (i == 6) and (grid[i] > 10):
                pits.pits[i].img = blue_point_img_array[len(blue_point_img_array) - 1]
            elif (i == 6) :
                pits.pits[i].img = blue_point_img_array[grid[i]]
            else :
                pits.pits[i].img = blue_pit_img_array[len(blue_pit_img_array) - 1]
        else :
            if (i == 6) :
                pits.pits[i].img = blue_point_img_array[grid[i]]
            else :
                pits.pits[i].img = blue_pit_img_array[grid[i]]

    for i in range(7, 14) :
        if (grid[i] > 6) :
            if (i == 13) and (grid[i] > 10):
                pits.pits[i].img = red_point_img_array[len(red_point_img_array) - 1]
            elif (i == 13) :
                pits.pits[i].img = red_point_img_array[grid[i]]
            else :
                pits.pits[i].img = red_pit_img_array[len(red_pit_img_array) - 1]
        else :
            if (i == 13) :
                pits.pits[i].img = red_point_img_array[grid[i]]
            else :
                pits.pits[i].img = red_pit_img_array[grid[i]]

run = True
while run:
    
    screen.blit(board_img, board_rect)

    pits.draw(screen)

    if pit0.action() == True :
        mancala.playerMove(0)
        mancala.cpuMove()
    if pit1.action() == True :
        mancala.playerMove(1)
        mancala.cpuMove()
    if pit2.action() == True :
        mancala.playerMove(2)
        mancala.cpuMove()
    if pit3.action() == True :
        mancala.playerMove(3)
        mancala.cpuMove()
    if pit4.action() == True :
        mancala.playerMove(4)
        mancala.cpuMove()
    if pit5.action() == True :
        mancala.playerMove(5)
        mancala.cpuMove()

    updateGameInterface()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    screen.fill((202, 228, 241))
    clock.tick(60)

pygame.quit()
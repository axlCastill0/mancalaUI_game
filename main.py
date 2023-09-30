import pygame, Pit, Mancala_UI, Mancala, sys, Button

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

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

OP_PIT_TEXT_HEIGHT = RED_PIT_HEIGHT - 65
MY_PIT_TEXT_HEIGHT = BLUE_PIT_HEIGHT + 65
OP_POINT_TEXT_WIDTH = POINT_PIT_WIDTH[1] + 70
MY_POINT_TEXT_WIDTH = POINT_PIT_WIDTH[0] - 70

POINT_COLOR = pygame.Color(183, 118, 59)
POINT_SIZE = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala - Game")

board_img = pygame.image.load("img/mancala_board.png").convert_alpha()
board_rect = board_img.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

BG = pygame.image.load("img/background_1.png")

def drawTransparentBG() :
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.fill((10,10,10))
    s.set_colorkey((255,255,255))
    s.set_alpha(32)
    screen.blit(s, (0, 0))

pause_img_base = pygame.image.load("img/pause_btn_base.png")
pause_img_hover = pygame.image.load("img/pause_btn_hover.png")
pausebtn = Button.Button(pause_img_base, pause_img_hover, (SCREEN_WIDTH-90,50))
pausenewgame_img_base = pygame.image.load("img/newgame_btn_base.png")
pausenewgame_img_hover = pygame.image.load("img/newgame_btn_hover.png")
pausenewgamebtn = Button.Button(pausenewgame_img_base, pausenewgame_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
menunewgame_img_base = pygame.image.load("img/newgame_btn_base.png")
menunewgame_img_hover = pygame.image.load("img/newgame_btn_hover.png")
menunewgamebtn = Button.Button(menunewgame_img_base, menunewgame_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150))
return_img_base = pygame.image.load("img/return_btn_base.png")
return_img_hover = pygame.image.load("img/return_btn_hover.png")
returnbtn = Button.Button(return_img_base, return_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150))
exit_img_base = pygame.image.load("img/exit_btn_base.png")
exit_img_hover = pygame.image.load("img/exit_btn_hover.png")
exitbtn = Button.Button(exit_img_base, exit_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150))
back_img_base = pygame.image.load("img/back_btn_base.png")
back_img_hover = pygame.image.load("img/back_btn_hover.png")
backbtn = Button.Button(back_img_base, back_img_hover, (90, 50))

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

def get_font(size) :
    return pygame.font.Font("PixelEmulator-xq08.ttf", size)

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

    for i in range(7) :
        if (i == 6) :
            text = get_font(POINT_SIZE).render(str(grid[i]), True, POINT_COLOR)
            text_rect = text.get_rect(center = (MY_POINT_TEXT_WIDTH, POINT_PIT_HEIGHT))
            screen.blit(text, text_rect)
            break
        text = get_font(POINT_SIZE).render(str(grid[i]), True, POINT_COLOR)
        text_rect = text.get_rect(center = (PIT_WIDTH_COORDS[i], MY_PIT_TEXT_HEIGHT))
        screen.blit(text, text_rect)

    for i in range(7, 14) :
        if (i == 13) :
            text = get_font(POINT_SIZE).render(str(grid[i]), True, POINT_COLOR)
            text_rect = text.get_rect(center = (OP_POINT_TEXT_WIDTH, POINT_PIT_HEIGHT))
            screen.blit(text, text_rect)
            break
        text = get_font(POINT_SIZE).render(str(grid[i]), True, POINT_COLOR)
        text_rect = text.get_rect(center = (PIT_WIDTH_COORDS[len(PIT_WIDTH_COORDS) - i], OP_PIT_TEXT_HEIGHT))
        screen.blit(text, text_rect)    

def main_menu() :
    pygame.display.set_caption("Mancala - Main Menu")

    run = True
    while run:
        screen.fill((0, 0, 20))

        menunewgamebtn.draw(screen)
        exitbtn.draw(screen)
        
        if menunewgamebtn.action() == True:
            mancala.newGrid()
            game()
            run = False
        if exitbtn.action() == True:
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def options_menu() :
    pass

def pause_menu() :
    pygame.display.set_caption("Mancala - Pause")

    run = True
    while run :
        drawTransparentBG()

        pausenewgamebtn.draw(screen)
        returnbtn.draw(screen)

        if pausenewgamebtn.action() == True:
            mancala.newGrid()
            run = False
        if returnbtn.action() == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def game():
    pygame.display.set_caption("Mancala - Game")

    run = True
    disabled = False
    current_time = 0
    button_press_time = 0
    while run:
        current_time = pygame.time.get_ticks()

        screen.blit(BG, (0, 0))

        screen.blit(board_img, board_rect)

        pits.draw(screen)

        pausebtn.draw(screen)
        backbtn.draw(screen)

        updateGameInterface()

        if pit0.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(0)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit1.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(1)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit2.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(2)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit3.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(3)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit4.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(4)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit5.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(5)
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pausebtn.action() == True :
            if (not disabled) :
                pause_menu()
        if backbtn.action() == True :
            if (not disabled) :
                main_menu()

        if current_time - button_press_time > 1200 :
            mancala.cpuMove()
            disabled = False

        if not mancala.gameEnded :
            mancala.checkEmpty()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()
import pygame, Pit, Mancala_UI, Mancala, sys, Button

pygame.mixer.pre_init(44100, -16, 1, 64)
pygame.init()
pygame.mixer.init()

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

hit_sound = pygame.mixer.Sound("sound/hitsound.wav")
btn_sound = pygame.mixer.Sound("sound/buttonsound.wav")

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
pausebtn = Button.Button(pause_img_base, pause_img_hover, (SCREEN_WIDTH-90, 50))

newgame_img_base = pygame.image.load("img/newgame_btn_base.png")
newgame_img_hover = pygame.image.load("img/newgame_btn_hover.png")
newgamebtn = Button.Button(newgame_img_base, newgame_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 75))
menunewgamebtn = Button.Button(newgame_img_base, newgame_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100))
gamenewgamebtn = Button.Button(newgame_img_base, newgame_img_hover, (SCREEN_WIDTH/2, 60))

return_img_base = pygame.image.load("img/return_btn_base.png")
return_img_hover = pygame.image.load("img/return_btn_hover.png")
returnbtn = Button.Button(return_img_base, return_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75))

exit_img_base = pygame.image.load("img/exit_btn_base.png")
exit_img_hover = pygame.image.load("img/exit_btn_hover.png")
exitbtn = Button.Button(exit_img_base, exit_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100))

back_img_base = pygame.image.load("img/back_btn_base.png")
back_img_hover = pygame.image.load("img/back_btn_hover.png")
backbtn = Button.Button(back_img_base, back_img_hover, (90, 50))

options_img_base = pygame.image.load("img/options_btn_base.png")
options_img_hover = pygame.image.load("img/options_btn_hover.png")
optionsbtn = Button.Button(options_img_base, options_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150))
menuoptionsbtn = Button.Button(options_img_base, options_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

difficulty_img_base = pygame.image.load("img/difficulty_btn_base.png")
difficulty_img_hover = pygame.image.load("img/difficulty_btn_hover.png")
difficultybtn = Button.Button(difficulty_img_base, difficulty_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75))

easy_img_base = pygame.image.load("img/easy_btn_base.png")
easy_img_hover = pygame.image.load("img/easy_btn_hover.png")
easybtn = Button.Button(easy_img_base, easy_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150))

medium_img_base = pygame.image.load("img/medium_btn_base.png")
medium_img_hover = pygame.image.load("img/medium_btn_hover.png")
mediumbtn = Button.Button(medium_img_base, medium_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

hard_img_base = pygame.image.load("img/hard_btn_base.png")
hard_img_hover = pygame.image.load("img/hard_btn_hover.png")
hardbtn = Button.Button(hard_img_base, hard_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150))

turn_img_base = pygame.image.load("img/turn_btn_base.png")
turn_img_hover = pygame.image.load("img/turn_btn_hover.png")
turnbtn = Button.Button(turn_img_base, turn_img_hover, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+75))

you_img_base = pygame.image.load("img/you_btn_base.png")
you_img_hover = pygame.image.load("img/you_btn_hover.png")
youbtn = Button.Button(you_img_base, you_img_hover, (SCREEN_WIDTH/2+150, SCREEN_HEIGHT/2))

cpu_img_base = pygame.image.load("img/cpu_btn_base.png")
cpu_img_hover = pygame.image.load("img/cpu_btn_hover.png")
cpubtn = Button.Button(cpu_img_base, cpu_img_hover, (SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2))

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
    pygame.display.set_caption("Mancala - Axl Castillo | Thomas Journault")

    run = True
    while run:
        screen.fill((0, 0, 30))

        text = get_font(110).render("Mancala", True, (255, 245, 245))
        text_rect = text.get_rect(center = (SCREEN_WIDTH/2, 90))
        screen.blit(text, text_rect)

        menunewgamebtn.draw(screen)
        exitbtn.draw(screen)
        menuoptionsbtn.draw(screen)
        
        if menunewgamebtn.action() == True:
            btn_sound.play()
            mancala.gameEnded = 0
            mancala.newGrid()
            game()
            run = False
        if exitbtn.action() == True:
            btn_sound.play()
            sys.exit()
        if menuoptionsbtn.action() == True:
            btn_sound.play()
            options_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def difficulty_menu() :
    pygame.display.set_caption("Mancala - Difficulty")

    run = True
    while run :
        screen.fill((0, 0, 30))

        easybtn.draw(screen)
        mediumbtn.draw(screen)
        hardbtn.draw(screen)
        backbtn.draw(screen)

        if backbtn.action() == True:
            btn_sound.play()
            run = False
        if easybtn.action() == True:
            btn_sound.play()
            mancala.difficulty = 0
            run = False
        if mediumbtn.action() == True:
            btn_sound.play()
            mancala.difficulty = 1
            run = False
        if hardbtn.action() == True:
            btn_sound.play()
            mancala.difficulty = 2
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def first_turn_menu() :
    pygame.display.set_caption("Mancala - First Turn")

    run = True
    while run :
        screen.fill((0, 0, 30))

        cpubtn.draw(screen)
        youbtn.draw(screen)
        backbtn.draw(screen)

        if cpubtn.action() == True:
            btn_sound.play()
            mancala.firstTurn = 1
            run = False
        if youbtn.action() == True:
            btn_sound.play()
            mancala.firstTurn = 0
            run = False
        if backbtn.action() == True:
            btn_sound.play()
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def options_menu() :
    pygame.display.set_caption("Mancala - Options")

    run = True
    while run :
        screen.fill((0, 0, 30))

        difficultybtn.draw(screen)
        backbtn.draw(screen)
        turnbtn.draw(screen)

        if difficultybtn.action() == True:
            btn_sound.play()
            difficulty_menu()
        if backbtn.action() == True:
            btn_sound.play()
            run = False
        if turnbtn.action() == True:
            btn_sound.play()
            first_turn_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def pause_menu() :
    pygame.display.set_caption("Mancala - Pause")

    run = True
    while run :
        drawTransparentBG()

        newgamebtn.draw(screen)
        returnbtn.draw(screen)

        if newgamebtn.action() == True:
            btn_sound.play()
            mancala.newGrid()
            mancala.gameEnded = 0
            run = False
        if returnbtn.action() == True:
            btn_sound.play()
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
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit1.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(1)
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit2.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(2)
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit3.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(3)
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit4.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(4)
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pit5.action() == True :
            if (not disabled) :
                button_press_time = pygame.time.get_ticks()
                mancala.playerMove(5)
                hit_sound.play()
                if mancala.currentTurn == 0 :
                    pass
                else :
                    disabled = True
        if pausebtn.action() == True :
            if (not disabled) :
                btn_sound.play()
                pause_menu()
        if backbtn.action() == True :
            if (not disabled) :
                btn_sound.play()
                main_menu()
        if mancala.gameEnded != 0:
            if gamenewgamebtn.action() == True :
                btn_sound.play()
                mancala.newGrid()
                mancala.gameEnded = 0

        if current_time - button_press_time > 1200 and mancala.gameEnded == 0:
            if mancala.difficulty == 0:
                mancala.cpuMove()
            elif mancala.difficulty == 1:
                mancala.cpuMoveMax()
            elif mancala.difficulty == 2:
                mancala.cpuMoveMinMax()
            disabled = False

        if mancala.gameEnded == 0:
            mancala.checkEmpty()
        if mancala.gameEnded == 1:
            text = get_font(60).render("YOU WON", True, (255, 245, 245))
            text_rect = text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)
            gamenewgamebtn.draw(screen)
        if mancala.gameEnded == 2:
            text = get_font(60).render("CPU WON", True, (255, 245, 245))
            text_rect = text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(text, text_rect)
            gamenewgamebtn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()
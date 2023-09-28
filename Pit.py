import pygame

class Pit(pygame.sprite.Sprite) :
    def __init__(self, label, x, y, seeds, img) :
        pygame.sprite.Sprite.__init__(self)
        self.label = label
        self.seeds = seeds
        self.img = img
        self.rect = self.img.get_rect(center = (x, y))
        self.clicked = False

    def draw(self, screen) :
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print(self.seeds)

        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False

        screen.blit(self.img, self.rect)

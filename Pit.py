import pygame

class Pit(pygame.sprite.Sprite) :
    def __init__(self, id, x, y, seeds, img) :
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.seeds = seeds
        self.img = img
        self.rect = self.img.get_rect(center = (x, y))
        self.clicked = False

    def draw(self, screen) :
        screen.blit(self.img, self.rect)

    def action(self) -> bool:
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True

        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False
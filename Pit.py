import pygame

class Pit(pygame.sprite.Sprite) :
    def __init__(self, label, x, y, seeds, img) :
        pygame.sprite.Sprite.__init__(self)
        self.label = label
        self.seeds = seeds
        self.img = img
        self.rect = self.img.get_rect(center = (x, y))

    def draw(self, screen) :
        screen.blit(self.img, self.rect)

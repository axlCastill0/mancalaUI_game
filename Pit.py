import pygame

class Pit(pygame.sprite.Sprite) :
    def __init__(self, label, x, y, seeds, img) :
        pygame.sprite.Sprite.__init__(self)
        self.label = label
        self.x = x
        self.y = y
        self.seeds = seeds
        self.img = img

import pygame

class Button() :
    def __init__(self, base_img, hover_img, pos):
        self.base_img = base_img
        self.hover_img = hover_img
        self.x = pos[0]
        self.y = pos[1]
        self.rect = self.base_img.get_rect(center = (self.x, self.y))

    def draw(self, screen) :
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) :
            screen.blit(self.hover_img, self.rect)
        else :
            screen.blit(self.base_img, self.rect)
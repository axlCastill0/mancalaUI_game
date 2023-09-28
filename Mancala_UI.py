import pygame

class Pits() :
    def __init__(self, pits) :
        self.pits = pits

    def draw(self, screen) :
        for pit in self.pits :
            pit.draw(screen)

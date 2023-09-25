import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.fill((255, 0, 0))
    clock.tick(60)
    print(clock.tick())
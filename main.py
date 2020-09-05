# imports
import pygame
import sys

# globals
particle_size = 25
snek = [[13, 13], [13, 14]]
direction = 0
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 700])


def draw():
    screen.fill((0, 100, 0))
    head = True
    for x in snek:
        coords = [x[0] * particle_size, x[1] * particle_size]
        if head:
            pygame.draw.rect(screen, (0, 0, 0),
                             (coords[0], coords[1],
                              particle_size, particle_size), 0)
            head = False
        else:
            pygame.draw.rect(screen, (47, 79, 79),
                             (coords[0], coords[1],
                              particle_size, particle_size), 0)


go = True
grow = None
food_ind = -1
stop = False
score = 0
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 2:
                direction = 0
            if event.key == pygame.K_RIGHT and direction != 3:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 0:
                direction = 2
            if event.key == pygame.K_LEFT and direction != 1:
                direction = 3
    num = len(snek) - 1
    for i in range(1, len(snek)):
        snek[num] = snek[num - 1].copy()
        num -= 1
    if direction == 0:
        snek[0][1] -= 1
    if direction == 1:
        snek[0][0] += 1
    if direction == 2:
        snek[0][1] += 1
    if direction == 3:
        snek[0][0] -= 1
    if not(stop):
        draw()
        pygame.display.update()
    else:
        print("u reached " + str(score))
        sys.exit()
    clock.tick(10)


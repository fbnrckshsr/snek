# imports
import pygame
import sys
import numpy as np

# globals
particle_size = 25
snek = [[13, 13], [13, 14]]
food_coords = []
direction = 0
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('arialblack', 35)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 700])


def score_text(text, font):
    text_space = font.render(text, True, (255, 255, 255))
    return text_space, text_space.get_rect()


def draw():
    screen.fill((102, 0, 51))
    for a in food_coords:
        coords = [a[0] * particle_size, a[1] * particle_size]
        pygame.draw.rect(screen, (255, 0, 127),
                         (coords[0], coords[1],
                          particle_size, particle_size), 0)
    head = True
    for x in snek:
        coords = [x[0] * particle_size, x[1] * particle_size]
        if head:
            pygame.draw.rect(screen, (0, 0, 0),
                             (coords[0], coords[1],
                              particle_size, particle_size), 0)
            head = False
        else:
            pygame.draw.rect(screen, (128, 128, 128),
                             (coords[0], coords[1],
                              particle_size, particle_size), 0)


def gen_food():
    not_viable = True
    while not_viable:
        coord = [np.random.randint(0, 28), np.random.randint(0, 28)]
        change = False
        for x in snek:
            if coord == x:
                change = True
        for x in food_coords:
            if coord == x:
                change = True
        if not(change):
            return coord


# main
food_coords.append(gen_food())
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

    if grow != None:
        snek.append(grow.copy())
        grow = None
        food_coords.pop(food_ind)

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

    for x in range(1, len(snek)):
        if snek[0] == snek[x]:
            stop = True
    if snek[0][0] < 0 or snek[0][0] > 27:
        stop = True
    if snek[0][1] < 0 or snek[0][1] > 27:
        stop = True

    for x in range(0, len(food_coords)):
        if food_coords[x] == snek[0]:
            grow = snek[-1].copy()
            food_ind = x
            score += 10
    rand = np.random.randint(0, 100)
    if rand <= 1 and len(food_coords) < 4 or len(food_coords) == 0:
        food_coords.append(gen_food())

    if not(stop):
        draw()
        text_ground, text_box = score_text("Score: " + str(score), font)
        text_box.center = (350, 40)
        screen.blit(text_ground, text_box)
        pygame.display.update()
    else:
        print("u reached " + str(score) + " points!")
        sys.exit()
    clock.tick(10)


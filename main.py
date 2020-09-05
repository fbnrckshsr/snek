# imports
import pygame
import sys

particle = 25
snek = [[13, 13], [13, 14]]
direction = 0

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([700, 700])

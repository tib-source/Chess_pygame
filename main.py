import pygame
import sys

pygame.init()

board = [[" "]*8 for x in range(8)]
size = width, height = 800, 600
WHITE = (255,255,255)
BLACK = (0,0,0)
SQUARE = 20

screen = pygame.display.set_mode(size)

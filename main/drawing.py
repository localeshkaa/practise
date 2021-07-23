import pygame
from settings import *


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("МАШИНКА РУРУРУ")
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Aerial', 25)


def drawWindow():
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, deliver_pos, 50, 0)


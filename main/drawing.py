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

# def drawText():
#     textsurface2 = font.render("R   vec: " + str(robot.vector), False, (0, 0, 0))
#     textsurface3 = font.render("polar: " + str(math.floor(robot.vector.as_polar()[1])), False, (0, 0, 0))
#     screen.blit(textsurface2, (10, 50))
#     screen.blit(textsurface3, (10, 100))
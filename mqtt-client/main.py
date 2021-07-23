import time
import pygame
from pygame.locals import *
import publisher
from settings import *

pygame.init()
screen = pygame.display.set_mode((main_width, main_height))
pygame.display.set_caption('ПИВКО ИЩЕМ ДА ТОИСТЬ')
font = pygame.font.SysFont('Aerial', 25)


class Button():
    button_colour = (0, 0, 139)
    hover_colour = (0, 0, 255)
    click_colour = (65, 105, 225)
    text_colour = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        button_rect = Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_colour, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_colour, button_rect)
        else:
            pygame.draw.rect(screen, self.button_colour, button_rect)

        text_img = font.render(self.text, True, self.text_colour)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
        return action

start = Button(5, 150, 'Старт')
stop = Button(215, 150, 'Стоп')
auto = Button(5, 250, 'Автомат')
manual = Button(215, 250, 'Ручками')



run = True
while run:

    screen.fill(background)

    if auto.draw_button():
        msg = "Автомат"
        publisher.publish(msg)

    if manual.draw_button():
        msg = "Ручками"
        publisher.publish(msg)

    if start.draw_button():
        msg = "Поехали"
        publisher.publish(msg)

    if stop.draw_button():
        msg = "Стоп"
        publisher.publish(msg)


    message = font.render(msg, True, WHITE)
    screen.blit(message, (75, 100))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
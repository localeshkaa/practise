from settings import *
from drawing import *
import random


class Beer():
    def __init__(self):
        self.beer_heght = 30
        self.beer_width = 70
        self.beer_x_pos = random.randint(200, 750)
        self.beer_y_pos = random.randint(15, 600)
        self.beer = pygame.Surface((self.beer_heght, self.beer_width), pygame.SRCALPHA)
        self.beer.fill(GREEN)
        self.beer_rect = self.beer.get_rect(center=(self.beer_x_pos, self.beer_y_pos))
        self.transparency = 255
        pygame.draw.line(self.beer, DARK_GREEN, [0, 25], [70, 25], 15)

    def setBeerPos(self, pos):
        self.beer_x_pos = pos[0]
        self.beer_y_pos = pos[1]
        self.beer_rect = self.beer.get_rect(center=pos)
        self.transparency = 255

    def getBeerPos(self):
        return self.beer_rect.center

    def takeBeer(self):
        for i in range (0, 255):
            self.transparency -= 5

    def draw(self):
        self.beer.set_alpha(self.transparency)
        screen.blit(self.beer, (self.beer_x_pos, self.beer_y_pos))



##################################################################
##################################################################
##################################################################
###############################################################



class Robot():
    def __init__(self, x_start, y_start):
        self.robot_height = 70
        self.robot_width = 40
        self.angle = -90
        self.speed = 0.0005
        self.rotation_speed = 0.5
        self.takeBeer = False
        self.deliverBeer = False
        self.robotStart = False
        self.robotAuto = False
        self.vector = pygame.math.Vector2(1, 0)
        self.robot = pygame.Surface((self.robot_height, self.robot_width), pygame.SRCALPHA)
        self.robot.fill(RED)
        pygame.draw.line(self.robot, BLACK, [10, 0], [25, 0], 15)
        pygame.draw.line(self.robot, BLACK, [60, 0], [45, 0], 15)



        self.robot_rect = self.robot.get_rect(center =(x_start,y_start))


        self.previous_x_pos = 0
        self.previous_y_pos = 0

    def draw(self):
        self.rotated_robot = pygame.transform.rotozoom(self.robot, self.angle, 0.9)
        self.robot_rect = self.rotated_robot.get_rect(center=self.robot_rect.center)
        screen.blit(self.rotated_robot, self.robot_rect)

    def rotation(self, direction):
        if direction == 1:
            self.angle -= self.rotation_speed
            if self.angle <= -359: self.angle = 0
            self.vector.rotate_ip(+self.rotation_speed)

        if direction == -1:
            self.angle += self.rotation_speed
            if self.angle >= 359: self.angle = 0
            self.vector.rotate_ip(-self.rotation_speed)

    def movement(self, move):
        if move == 1:
            self.robot_rect.center += self.vector * 5.5
        if move == -1:
            self.robot_rect.center -= self.vector * 5.5

    def getRobotPos(self):
        return self.robot_rect.center

    def goTo(self, x_pos, y_pos):

        if self.robotStart and self.robotAuto:
            dx = self.robot_rect.center[0] - x_pos
            dy = self.robot_rect.center[1] - y_pos
            dist = math.sqrt(dx * dx + dy * dy)
            if dist != 0:
                vec_x = dx / dist
                vec_y = dy / dist
            else:
                vec_x, vec_y = 1, 1

            vector2 = pygame.math.Vector2(-vec_x, -vec_y)
            vector2.normalize()

            if vector2.as_polar()[1] < 0:
                if math.fabs(self.vector.as_polar()[1] - vector2.as_polar()[1]) > 2:
                    self.rotation(-1)
                if math.fabs(self.vector.as_polar()[1] - vector2.as_polar()[1]) < 2:
                    self.rotation(1)

            if vector2.as_polar()[1] > 0:
                if math.fabs(self.vector.as_polar()[1] - vector2.as_polar()[1]) > 2:
                    self.rotation(1)
                if math.fabs(self.vector.as_polar()[1] - vector2.as_polar()[1]) < 2:
                    self.rotation(-1)

            if math.fabs(self.vector.as_polar()[1] - vector2.as_polar()[1]) <= 6:
                self.movement(1)

    def startRobot(self):
        self.robotStart = True

    def stopRobot(self):
        self.robotStart = False

    def auto(self):
        self.robotAuto = True

    def manual(self):
        self.robotAuto = False

from classes import Robot, Beer
from drawing import *
from settings import *
import subscriber

subscriber.start()
robot = Robot(width/2, height/2)
beer = Beer()


def manual():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot.rotation(-1)
    if keys[pygame.K_RIGHT]:
        robot.rotation(1)
    if keys[pygame.K_UP]:
        robot.movement(1)
    if keys[pygame.K_DOWN]:
        robot.movement(-1)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()



while start:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    drawWindow()

    beer.draw()

    robot.draw()

    surf = pygame.Surface((1280, 720))
    surf.blit(screen, (0, 0))


    if str(subscriber.get_msg()) == "Поехали": robot.startRobot()
    if str(subscriber.get_msg()) == "Автомат": robot.auto()
    if str(subscriber.get_msg()) == "Ручками":
        robot.manual()
        manual()
    if str(subscriber.get_msg()) == "Стоп": robot.stopRobot()


    if robot.takeBeer == True:
        robot.goTo(deliver_pos[0], deliver_pos[1])
        if robot.robot_rect.collidepoint(deliver_pos):
            robot.takeBeer = False
            robot.deliverBeer = True
            beer.setBeerPos(deliver_pos)

    elif not robot.deliverBeer:
        robot.goTo(beer.getBeerPos()[0], beer.getBeerPos()[1])
        if robot.robot_rect.collidepoint(beer.getBeerPos()):
            robot.takeBeer = True
            beer.takeBeer()





    pygame.display.flip()


pygame.quit()
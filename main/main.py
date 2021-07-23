from main.classes import Robot, Beer
from main.drawing import *
from settings import *
import subscriber


#список, в который помещается нажатая кнопка
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

subscriber.start()

robot = Robot(width/2, height/2)
beer = Beer()

#запуск пайгейма
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


    #управление роботом
    if str(subscriber.get_msg()) == "Поехали": robot.startRobot()
    if str(subscriber.get_msg()) == "Автомат": robot.auto()
    if str(subscriber.get_msg()) == "Ручками":
        robot.manual()
        manual()
    if str(subscriber.get_msg()) == "Стоп": robot.stopRobot()


    if robot.beerTake == True:    # если груз взят, то везем его
        robot.goTo(deliver_pos[0], deliver_pos[1])
        if robot.robot_rect.collidepoint(deliver_pos):
            robot.beerTake = False
            robot.beerDeliver = True
            beer.setBeerPos(deliver_pos)

    elif not robot.beerDeliver:  # если груз не взят и не доставлен
        robot.goTo(beer.getBeerPos()[0], beer.getBeerPos()[1])
        if robot.robot_rect.collidepoint(beer.getBeerPos()):  # определяет пересечение поверхности робота и поверхности пива
            robot.beerTake = True
            beer.beerTake()  # при взятии пива удаляет его с экрана





    pygame.display.flip()


pygame.quit()
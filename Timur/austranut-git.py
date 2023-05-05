import pygame
import sys


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('After Dark.mp3')
pygame.mixer.music.play()
boom = pygame.mixer.Sound('boom.mp3')

myfont = pygame.font.SysFont("monospace", 55)
text = myfont.render("Welcome to station!", True, (10, 10, 10))

picture = pygame.transform.scale(pygame.image.load("skumbria.jpeg"), (2000, 2000))
space_station = pygame.transform.scale(pygame.image.load("space-station (1).png"), (350, 350))
austronaut = pygame.transform.scale(pygame.image.load("austronaut.png"), (150, 150))
meteo = pygame.transform.scale(pygame.image.load("meteo.png"), (150, 150))

clock = pygame.time.Clock()
mw = pygame.display.set_mode(flags=pygame.FULLSCREEN)

counter_for_text = 0
counter = 0

BLACK = (0, 0, 0)
run = True
achived_station = False
move_up = False
move_down = False
move_left = False
move_right = False

x_austr = 300
y_austr = 300
dx = 0
dy = 0
rect_for_station = pygame.Rect(250, 350, 70, 70)
rect_for_end = pygame.Rect(0, 0, 1000, 1000)

while run:
    mw.blit(picture, (0, 0))
    pygame.draw.rect(mw, BLACK, rect_for_station)
    mw.blit(space_station, (100, 100))
    rect_for_austronaut = pygame.Rect(x_austr, y_austr, 25, 25)
    health_box = pygame.Rect(50, 50, 70, 70)
    pygame.draw.rect(mw, (240, 10, 10), health_box)
    mw.blit(meteo, (0, 0))
    if pygame.mouse.get_pressed()[0] and health_box.collidepoint(pygame.mouse.get_pos()):
        print(pygame.mouse.get_pressed())
        boom.play()
        #run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and rect_for_austronaut.colliderect(rect_for_station):
                achived_station = True
            if event.key == pygame.K_UP:
                dy = -3
            if event.key == pygame.K_DOWN:
                dy = 3
            if event.key == pygame.K_LEFT:
                dx = -3
            if event.key == pygame.K_RIGHT:
                dx = 3

            if event.key == pygame.K_SPACE:
                if rect_for_austronaut.colliderect(rect_for_station):
                    run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0

    y_austr += dy
    x_austr += dx
    if rect_for_austronaut.colliderect(rect_for_station):
        if dy > 0:
            y_austr -= 10
        elif dy < 0:
            y_austr += 10
            





    if rect_for_austronaut.colliderect(health_box):
        boom.play()
        s = pygame.Surface((2000, 2000))  # the size of your rect
        s.set_alpha(30)  # alpha level
        s.fill((230, 50, 50))  # this fills the entire surface
        mw.blit(s, (0, 0))
    pygame.draw.rect(mw, BLACK, rect_for_austronaut)
    mw.blit(austronaut, (x_austr - 70, y_austr - 70))
    clock.tick(40)
    pygame.display.update()


run = True
back = pygame.transform.scale(pygame.image.load("space-station.jpg"), (2000, 2000))

while run:
    mw.blit(back, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                y_austr -= 40
                dy = 1
            if event.key == pygame.K_LEFT:
                dx = -3
            if event.key == pygame.K_RIGHT:
                dx = 3

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0
    if y_austr < 400:
        y_austr += dy
        if dy < 5:
            dy += 0.3
    x_austr += dx


    rect_for_austronaut = pygame.Rect(x_austr, y_austr, 25, 25)
    pygame.draw.rect(mw, BLACK, rect_for_austronaut)
    mw.blit(austronaut, (x_austr - 70, y_austr - 70))

    clock.tick(40)
    pygame.display.update()


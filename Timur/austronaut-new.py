import pygame
import sys


pygame.init()
#pygame.mixer.init()
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
dx = 2
dy = 2
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
        boom.play()
        #run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and rect_for_austronaut.colliderect(rect_for_station):
                achived_station = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False



    if move_up == True:
        y_austr += -dy
    if move_down == True:
        y_austr += dy
    if move_left == True:
        x_austr += -dx
    if move_right == True:
        x_austr += dx

    if rect_for_austronaut.colliderect(health_box):
        boom.play()
        s = pygame.Surface((2000, 2000))  # the size of your rect
        s.set_alpha(30)  # alpha level
        s.fill((230, 50, 50))  # this fills the entire surface
        mw.blit(s, (0, 0))

    if not achived_station:
        pygame.draw.rect(mw, BLACK, rect_for_austronaut)
        mw.blit(austronaut, (x_austr - 70, y_austr - 70))
    else:
        s = pygame.Surface((2000, 2000))  # the size of your rect
        s.set_alpha(counter)  # alpha level
        s.fill((128, 128, 170))  # this fills the entire surface
        mw.blit(s, (0, 0))
        if counter >= 128:
            mw.blit(text, (200, 400))
            if counter_for_text >= 90:
                text = myfont.render('Press enter to continue', True, (10, 10, 10))
            counter_for_text += 1
        else:
            counter += 1

    clock.tick(40)
    pygame.display.update()

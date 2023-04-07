import pygame
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Настройки цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Загрузка изображений
PLAYER_IMAGE = pygame.image.load("player.png")
BULLET_IMAGE = pygame.image.load("bul.png")

# Настройки игрока
player_x = WIDTH / 2
player_y = HEIGHT / 2
player_speed = 5
player_rotation = 0

# Настройки снарядов
bullets = []
bullet_speed = 10

# Настройки игровой петли
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullet_x = player_x + math.cos(math.radians(player_rotation - 90)) * 40
            bullet_y = player_y + math.sin(math.radians(player_rotation - 90)) * 40
            bullet_dx = math.cos(math.radians(player_rotation - 90)) * bullet_speed
            bullet_dy = math.sin()
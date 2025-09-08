import os
import pygame

pygame.init()
info = pygame.display.Info()
width = info.current_w
height = info.current_h

# входные переменные
n = 4  # кол-во строк
m = 12  # кол-во столбцов
base_width = width
base_height = height
# width = 1400  # ширина экрана
# height = 640  # высота экрана
half_decay_time = 6  # с какой секунды плита треснет
decay_time = 3  # с какой секунды плита будет выглядеть как почти сломавшаяся
min_start_tile_time = 3  # для рандома стартового времени платформы
max_start_tile_time = 10  # для рандома стартового времени платформы
fps = 60
character_width = 100
character_height = 100
character_shift = 65
tiles_count = int(m * n / 2) + 10  # надо изменить
tile_width = 100
tile_height = 100
upper_margin = character_height
left_margin = 20
right_margin = 20
bottom_margin = 200
bg_color = (0, 0, 0)
current_skin = os.path.join('img','character.png')


# pygame.display.set_mode((1, 1))
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
character_img = pygame.image.load(current_skin).convert_alpha()
character_img = pygame.transform.scale(character_img, (character_width * 7, character_height))
tile_img = pygame.image.load('img/tile.png').convert_alpha()
tile_img = pygame.transform.scale(tile_img, (tile_width, tile_height))
final_tile_img = pygame.image.load('img/final_tile.png').convert_alpha()
final_tile_img = pygame.transform.scale(final_tile_img, (tile_width, tile_height))
half_decay_tile_img = pygame.image.load('img/half_decay_tile.png').convert_alpha()
half_decay_tile_img = pygame.transform.scale(half_decay_tile_img, (tile_width, tile_height))
decay_tile_img = pygame.image.load('img/decay_tile.png').convert_alpha()
decay_tile_img = pygame.transform.scale(decay_tile_img, (tile_width, tile_height))
void_img = pygame.image.load('img/void.png').convert_alpha()
void_img = pygame.transform.scale(void_img, (tile_width, tile_height))
pygame.quit()
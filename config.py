import pygame

# входные переменные
n = 8  # кол-во строк
m = 12  # кол-во столбцов
base_width = 1400
base_height = 640
width = 1400  # ширина экрана
height = 640  # высота экрана
half_decay_time = 8  # с какой секунды плита треснет
decay_time = 2  # с какой секунды плита будет выглядеть как почти сломавшаяся
min_start_tile_time = 4  # для рандома стартового времени платформы
max_start_tile_time = 14  # для рандома стартового времени платформы
fps = 60
character_width = 100
character_height = 100
character_shift = 65
tiles_count = int(m * n / 2)
tile_width = 100
tile_height = 100
upper_margin = character_height
left_margin = 120
right_margin = 120
bottom_margin = 200
centalize_margin = (width - right_margin - left_margin - tile_width * m) / 2
bg_color = (0, 0, 0)
max_block_size = 4
current_level = 0

pygame.init()
pygame.display.set_mode((1, 1))
character_img = pygame.image.load('img/character.png').convert_alpha()
character_img = pygame.transform.scale(character_img, (character_width * 7, character_height))
tile_img = pygame.image.load('img/tile.png').convert_alpha()
tile_img = pygame.transform.scale(tile_img, (tile_width, tile_height))
final_tile_img = pygame.image.load('img/final_tile.png').convert_alpha()
final_tile_img = pygame.transform.scale(final_tile_img, (tile_width, tile_height))
half_decay_tile_img = pygame.image.load('img/half_decay_tile.png').convert_alpha()
half_decay_tile_img = pygame.transform.scale(half_decay_tile_img, (tile_width, tile_height))
decay_tile_img = pygame.image.load('img/decay_tile.png').convert_alpha()
decay_tile_img = pygame.transform.scale(decay_tile_img, (tile_width, tile_height))
pygame.quit()
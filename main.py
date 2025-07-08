import numpy as np
import pygame
import random

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, key):
        match key:
            case 'right':
                self.x += 1
            case 'left':
                self.x -= 1
            case 'up':
                self.y -= 1
            case 'down':
                self.y += 1
        return None
    
    def set(self, x, y):
        self.x = x
        self.y = y
        return None
    
    def get(self):
        return (self.x, self.y)
    
    def draw_player(self):
        screen.blit(character_img, (self.x * tile_width, self.y * tile_height))
        return None


class Field:
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.zeros((n, m))

    def generate(self):
        k = 0
        i = 0
        j = 0
        while k < tiles_count:
            if random.randint(0, 1) == 1 and self.matrix[i][j] == 0:
                k += 1
                self.matrix[i][j] = random.randint(min_start_tile_time, max_start_tile_time)
            j += 1
            if j == m:
                j = 0
                i += 1
                if i == n:
                    i = 0
        return None

    def tile_death(self):
        position = random.randint(0, tiles_count - 1)
        k = 0
        break_flag = False
        for i in range(n):
            if break_flag:
                break
            for j in range(m):
                if self.matrix[i][j] == 0:
                    if k == position:
                        self.matrix[i][j] = random.randint(min_start_tile_time, max_start_tile_time)
                        break_flag = True
                        break
                    k += 1
        return None
            
    def tick(self):
        for i in range(n):
            for j in range(m):
                if self.matrix[i][j] == 1:
                    self.tile_death()
                if self.matrix[i][j] != 0:
                    self.matrix[i][j] -= 1
        return None

    def draw_grid(self):
        for i in range(n):
            for j in range(m):
                if self.matrix[i][j] == 0:
                    screen.blit(void_img, (j * tile_width, i * tile_height))
                elif self.matrix[i][j] <= decay_time:
                    screen.blit(decay_tile_img, (j * tile_width, i * tile_height))
                elif self.matrix[i][j] <= half_decay_time:
                    screen.blit(half_decay_tile_img, (j * tile_width, i * tile_height))
                else:
                    screen.blit(tile_img, (j * tile_width, i * tile_height))
        return None


#входные переменные
n = 4 #кол-во строк
m = 12 #кол-во столбцов
width = 1280 #ширина экрана
height = 640 #высота экрана
half_decay_time = 6 #с какой секунды плита треснет
decay_time = 3 #с какой секунды плита будет выглядеть как почти сломавшаяся
min_start_tile_time = 7 #для рандома стартового времени платформы
max_start_tile_time = 9 #для рандома стартового времени платформы
fps = 60
character_width = 100
character_height = 100
tiles_count = int(m * n / 2) #надо изменить
tile_width = 100
tile_height = 100

#инициализация объектов
player = Player(0, 0)
field = Field(n, m)
runtime = 0

#тело игры
pygame.init()

screen = pygame.display.set_mode((width, height)) #создание основного окна
character_img = pygame.image.load('img/character.png').convert_alpha() #convert чтобы объект стал "surface" и с ним можно было работать
character_img = pygame.transform.scale(character_img, (character_width, character_height))
tile_img = pygame.image.load('img/tile.png').convert_alpha()
tile_img = pygame.transform.scale(tile_img, (tile_width, tile_height))
half_decay_tile_img = pygame.image.load('img/half_decay_tile.png').convert_alpha()
half_decay_tile_img = pygame.transform.scale(half_decay_tile_img, (tile_width, tile_height))
decay_tile_img = pygame.image.load('img/decay_tile.png').convert_alpha()
decay_tile_img = pygame.transform.scale(decay_tile_img, (tile_width, tile_height))
void_img = pygame.image.load('img/void.png').convert_alpha()
void_img = pygame.transform.scale(void_img, (tile_width, tile_height))
clock = pygame.time.Clock()
field.generate()

running = True
while running:
    screen.fill((255, 255, 255)) #заливка окна
    runtime += 1
    if runtime == fps:
        field.tick()
        runtime = 0

    field.draw_grid()
    player.draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move('right')
            if event.key == pygame.K_w:
                player.move('up')   
            if event.key == pygame.K_s:
                player.move('down')
            if event.key == pygame.K_a:
                player.move('left') 

    pygame.display.flip() #"refresh" в pygame
    clock.tick(fps) #задержка

pygame.quit()
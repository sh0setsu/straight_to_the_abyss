import numpy as np
import random
import config


class Field:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.zeros((n, m))

    def generate(self):
        k = 0
        i = 0
        j = 0
        self.matrix[0][0] = -1
        self.matrix[config.n - 1][config.m - 1] = -1
        while k < config.tiles_count:
            if random.randint(0, 1) == 1 and self.matrix[i][j] == 0:
                k += 1
                self.matrix[i][j] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
            j += 1
            if j == config.m:
                j = 0
                i += 1
                if i == config.n:
                    i = 0
        return None

    def tile_death(self):
        position = random.randint(0, int(config.n * config.m - config.tiles_count))
        k = 0
        break_flag = False
        for i in range(config.n):
            if break_flag:
                break
            for j in range(config.m):
                if self.matrix[i][j] == 0:
                    if k == position:
                        self.matrix[i][j] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
                        break_flag = True
                        break
                    k += 1
        return None

    def tick(self):
        for i in range(config.n):
            for j in range(config.m):
                if self.matrix[i][j] == 1:
                    self.tile_death()
                if self.matrix[i][j] > 0:
                    self.matrix[i][j] -= 1
        return None

    def draw_grid(self, screen):
        screen.blit(config.tile_img, (0, 0))
        screen.blit(config.final_tile_img, ((config.m - 1) * config.tile_width, (config.n - 1) * config.tile_height))
        for i in range(config.n):
            for j in range(config.m):
                if (i == 0 and j == 0) or (i == config.n - 1 and j == config.m - 1):
                    continue
                if self.matrix[i][j] == 0:
                    screen.blit(config.void_img, (j * config.tile_width, i * config.tile_height))
                elif self.matrix[i][j] <= config.decay_time:
                    screen.blit(config.decay_tile_img, (j * config.tile_width, i * config.tile_height))
                elif self.matrix[i][j] <= config.half_decay_time:
                    screen.blit(config.half_decay_tile_img, (j * config.tile_width, i * config.tile_height))
                else:
                    screen.blit(config.tile_img, (j * config.tile_width, i * config.tile_height))
        return None
    
    def check_tile(self, x, y):
        if self.matrix[y][x] != 0:
            return True
        return False
    
    def clear(self):
        for i in range(config.n):
            for j in range(config.m):
                if (i == 0 and j == 0) or (i == config.n - 1 and j == config.m - 1):
                    continue
                self.matrix[i][j] = 0

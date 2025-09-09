import numpy as np
import random
import config


class Field:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.zeros((n, m))
        self.key_x = 0
        self.key_y = 0
        self.key_found = False

    def generate(self, amount):
        k = 0
        #i = 0
        #j = 0
        self.matrix[0][0] = -1

        while k < amount:
            block_size = random.randint(1, config.max_block_size)
            if k + block_size > amount:
                block_size = amount - k
            x = 0
            y = 0
            stop_flag = False
            if config.auto_help:
                for i in range(config.n - 3):
                    for j in range(config.m - 3):
                        if (self.matrix[i][j] + self.matrix[i][j + 1] + self.matrix[i][j + 2] +
                            self.matrix[i + 1][j] + self.matrix[i + 1][j + 1] + self.matrix[i + 1][j + 2] +
                            self.matrix[i + 2][j] + self.matrix[i + 2][j + 1] + self.matrix[i + 2][j + 2] <= 0):
                            while self.matrix[x][y] != 0:
                                x = i + random.randint(0, 2)
                                y = j + random.randint(0, 2)
                            stop_flag = True
                            break
                    if stop_flag:
                        break
            if not stop_flag:
                while self.matrix[x][y] != 0:
                    x = random.randint(0, config.n - 1)
                    y = random.randint(0, config.m - 1)
            self.matrix[x][y] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
            block_size -= 1
            k += 1
            while block_size != 0:
                free_cells = (
                    int(x != config.n - 1 and self.matrix[x + 1][y] == 0),
                    int(y != config.m - 1 and self.matrix[x][y + 1] == 0), 
                    int(x != 0 and self.matrix[x - 1][y] == 0),
                    int(y != 0 and self.matrix[x][y - 1] == 0)
                )
                s = free_cells[0] + free_cells[1] + free_cells[2] + free_cells[3]
                if s == 0:
                    break
                move = random.randint(1, s)
                i = -1
                while move != 0:
                    i += 1
                    if free_cells[i] == 1:
                        move -= 1
                match i:
                    case 0:
                        x += 1
                    case 1:
                        y += 1
                    case 2:
                        x -= 1
                    case 3:
                        y -= 1
                self.matrix[x][y] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
                block_size -= 1
                k += 1
                




            #if random.randint(0, 1) == 1 and self.matrix[i][j] == 0:
            #    k += 1
            #    self.matrix[i][j] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
            #j += 1
            #if j == config.m:
            #    j = 0
            #    i += 1
            #    if i == config.n:
            #       i = 0
        return None

    #def tile_death(self):
    #    position = random.randint(0, int(config.n * config.m - config.tiles_count))
    #    k = 0
    #    break_flag = False
    #    for i in range(config.n):
    #        if break_flag:
    #            break
    #        for j in range(config.m):
    #            if self.matrix[i][j] == 0:
    #                if k == position:
    #                    self.matrix[i][j] = random.randint(config.min_start_tile_time, config.max_start_tile_time)
    #                    break_flag = True
    #                    break
    #                k += 1
    #    return None

    def create_key(self):
        if config.key_challenge:
            while self.matrix[self.key_x][self.key_y] != 0:
                self.key_x = random.randint(0, config.n - 1)
                self.key_y = random.randint(0, config.m - 1)
            self.matrix[self.key_x][self.key_y] = -1
            self.key_found = False

    def create_portal(self):
        if config.portal_challenge:
            self.matrix[random.randint(int(config.n / 4), config.n - 1)][random.randint(int(config.m / 4), config.m - 1)] = -2
        else:
            self.matrix[config.n - 1][config.m - 1] = -2

    def tick(self):
        k = 0
        for i in range(config.n):
            for j in range(config.m):
                if self.matrix[i][j] == 1:
                    k += 1
                if self.matrix[i][j] > 0:
                    self.matrix[i][j] -= 1
        self.generate(k)
        return None

    def draw_grid(self, screen):
        for i in range(config.n):
            for j in range(config.m):
                if self.matrix[i][j] == -1:
                    screen.blit(config.tile_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
                elif self.matrix[i][j] == -2:
                    screen.blit(config.final_tile_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
                    if config.key_challenge and not self.key_found:
                        screen.blit(config.keyhole_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
                elif self.matrix[i][j] == 0:
                    pass
                elif self.matrix[i][j] <= config.decay_time:
                    screen.blit(config.decay_tile_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
                elif self.matrix[i][j] <= config.half_decay_time:
                    screen.blit(config.half_decay_tile_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
                else:
                    screen.blit(config.tile_img, (config.left_margin + config.centalize_margin + j * config.tile_width, config.upper_margin + i * config.tile_height))
        if config.key_challenge and not self.key_found:    
            screen.blit(config.key_img, (config.left_margin + config.centalize_margin +  (self.key_y + 0.25) * config.tile_width, config.upper_margin + (self.key_x + 0.25) * config.tile_height))
        return None
    
    def check_tile(self, x, y):
        if self.matrix[y][x] == -2 and config.key_challenge and not self.key_found:
            return -1
        return self.matrix[y][x]
    
    def check_key(self, x, y):
        if y == self.key_x and x == self.key_y:
            self.key_found = True
        return None
    
    def clear(self):
        for i in range(config.n):
            for j in range(config.m):
                self.matrix[i][j] = 0
        self.matrix[0][0] = -1

import pygame
from src import player, field
import config


# инициализация объектов
player = player.Player(0, 0)
field = field.Field(config.n, config.m)
runtime = 0

# тело игры
pygame.init()

screen = pygame.display.set_mode((config.width, config.height))  # создание основного окна
clock = pygame.time.Clock()
field.generate()

active = True
while active:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = True
                while running and active:
                    screen.fill((255, 255, 255))  # заливка окна
                    runtime += 1
                    if runtime == config.fps:
                        field.tick()
                        runtime = 0

                    field.draw_grid(screen)
                    player.draw_player(screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            active = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_d and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                player.move('right')
                            if event.key == pygame.K_w and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                player.move('up')
                            if event.key == pygame.K_s and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                player.move('down')
                            if event.key == pygame.K_a and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                player.move('left')
                            if event.key == pygame.K_d and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                player.move('jump_right')
                            if event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                player.move('jump_up')
                            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                player.move('jump_down')
                            if event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                player.move('jump_left')

                    pygame.display.flip()  # "refresh" в pygame
                    clock.tick(config.fps)  # задержка

    pygame.display.flip()       
    clock.tick(config.fps)

pygame.quit()

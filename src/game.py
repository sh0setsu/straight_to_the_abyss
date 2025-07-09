import pygame
from src.player import Player
from src.field import Field
import config

def game_running(active, screen):
    clock = pygame.time.Clock()
    player = Player(0, 0)
    field = Field(config.n, config.m)
    field.generate()
    runtime = 0
    running = True
    player.set(0, 0)
    while running and active:
        screen.fill((255, 255, 255))  # заливка окна
        runtime += 1
        if runtime == config.fps:
            field.tick()
            runtime = 0

        player_x, player_y = player.get()
        if player.check_win():
            running = False
            return True
        elif not field.check_tile(player_x, player_y):
            print(2)
            running = False
            return True
        field.draw_grid(screen)
        player.draw_player(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
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
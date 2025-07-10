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
    game_running = True
    player.set(0, 0)
    while running and active:
        screen.fill((7,24,33))  # заливка окна
        if game_running:
            runtime += 1
            if runtime == config.fps:
                field.tick()
                runtime = 0

            player_x, player_y = player.get()
            if player.check_win():
                game_running = False
                config.character_img = pygame.transform.flip(config.character_img, True, True)
            elif not field.check_tile(player_x, player_y):
                game_running = False
                config.character_img = pygame.transform.flip(config.character_img, True, True)
        field.draw_grid(screen)
        player.draw_player(screen, game_running)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                    running = False
                if not game_running and event.key == pygame.K_RETURN:
                    player.set(0, 0)
                    field.clear()
                    field.generate()
                    config.character_img = pygame.transform.flip(config.character_img, True, True)
                    game_running = True
                if game_running:
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('right')
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('up')
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('down')
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('left')
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_right')
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_up')
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_down')
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_left')

        pygame.display.flip()  # "refresh" в pygame
        clock.tick(config.fps)  # задержка
    return True
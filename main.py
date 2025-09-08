import pygame
from src import functions, data, game
import config
import os


def resize_screen():
    config.tile_height = config.tile_width = int(min((config.height - config.bottom_margin) / (config.n + 1), (config.width - config.left_margin - config.right_margin) / config.m))
    config.character_width, config.character_height = config.tile_width, config.tile_height
    config.character_shift = int(config.tile_width * 0.65)
    config.upper_margin = config.character_height
    config.centalize_margin = (config.width - config.right_margin - config.left_margin - config.tile_width * config.m) / 2
    config.tile_img = pygame.transform.scale(config.tile_img, (config.tile_width, config.tile_height))
    config.half_decay_tile_img = pygame.transform.scale(config.half_decay_tile_img, (config.tile_width, config.tile_height))
    config.decay_tile_img = pygame.transform.scale(config.decay_tile_img, (config.tile_width, config.tile_height))
    config.final_tile_img = pygame.transform.scale(config.final_tile_img, (config.tile_width, config.tile_height))
    config.character_img = pygame.transform.scale(config.character_img, (config.character_width * 7, config.character_height))
    


play_button, settings_button, exit_button = data.buttons

# тело игры
pygame.init()
screen = pygame.display.set_mode((config.width, config.height))  # создание основного окна
main_background = pygame.image.load(os.path.join("assets", "background.jpg")).convert()
resize_screen()
main_background = pygame.transform.scale(main_background, (config.width, config.height))
clock = pygame.time.Clock()

active = True
fullscreen = False
while active:

    for event in pygame.event.get():
        #screen.fill(config.bg_color)
        screen.blit(main_background, (0, 0))
        functions.set_title(screen, 72, "STRAIGHT TO THE ABYSS", config.width, config.height)
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    config.width, config.height = screen.get_size()
                    main_background = pygame.transform.scale(main_background, (config.width, config.height))
                    resize_screen()
                else:
                    config.width, config.height = config.base_width, config.base_height
                    screen = pygame.display.set_mode((config.width, config.height))
                    resize_screen()
                    main_background = pygame.transform.scale(main_background, (config.width, config.height))
        if event.type == pygame.USEREVENT and event.button == play_button:
            active = game.game_running(active, screen)
        if event.type == pygame.USEREVENT and event.button == settings_button:
            active = functions.settings_page(screen, config.bg_color, 72, "Настройки", config.width, config.height)
        if event.type == pygame.USEREVENT and event.button == exit_button:
            active = False
            # functions.exit_game()

        for i_button in data.buttons:
            i_button.handle_event(event)


    for i_button in data.buttons:
        i_button.check_hover(pygame.mouse.get_pos())
        i_button.draw(screen)

    pygame.display.flip()
    clock.tick(config.fps)

pygame.quit()

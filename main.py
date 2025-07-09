import pygame
from src import functions, data, game
import config

play_button, settings_button, exit_button = data.buttons

# тело игры
pygame.init()

screen = pygame.display.set_mode((config.width, config.height))  # создание основного окна
clock = pygame.time.Clock()

active = True
while active:

    for event in pygame.event.get():
        screen.fill(config.bg_color)
        functions.set_title(screen, 72, "ИГРА НА PYTHON", config.width, config.height)
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                active = game.game_running(active)
        if event.type == pygame.USEREVENT and event.button == play_button:
            active = True
            game.game_running(active, screen)
        if event.type == pygame.USEREVENT and event.button == settings_button:
            functions.settings_page(screen, config.bg_color, 72, "Настройки", config.width, config.height)
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

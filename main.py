import pygame
from src import player, field
import config
from data import buttons
from functions import set_title, settings_page, exit_game

play_button, settings_button, exit_button = buttons


def game_running(active):
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


# инициализация объектов
player = player.Player(0, 0)
field = field.Field(config.n, config.m)

# тело игры
pygame.init()

screen = pygame.display.set_mode((config.width, config.height))  # создание основного окна
clock = pygame.time.Clock()
field.generate()

active = True
while active:

    for event in pygame.event.get():
        screen.fill(config.bg_color)
        set_title(screen, 72, "ИГРА НА PYTHON", config.width, config.height)
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                active = game_running(active)
        if event.type == pygame.USEREVENT and event.button == play_button:
            active = True
            game_running(active)
        if event.type == pygame.USEREVENT and event.button == settings_button:
            settings_page(screen, config.bg_color, 72, "Настройки", config.width, config.height)
        if event.type == pygame.USEREVENT and event.button == exit_button:
            active = False
            exit_game()

        for i_button in buttons:
            i_button.handle_event(event)


    for i_button in buttons:
        i_button.check_hover(pygame.mouse.get_pos())
        i_button.draw(screen)

    pygame.display.flip()
    clock.tick(config.fps)

pygame.quit()

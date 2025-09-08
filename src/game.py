import pygame
import config
from src.player import Player
from src.field import Field


def load_character_image():
    img = pygame.image.load(config.current_skin).convert_alpha()
    return pygame.transform.scale(img, (config.character_width * 7, config.character_height))


def game_running(active, screen):
    config.character_img = load_character_image()
    original_character_img = config.character_img
    clock = pygame.time.Clock()
    player = Player(0, 0)
    field = Field(config.n, config.m)
    field.generate()
    runtime = 0
    is_game_active = True
    player.set(0, 0)

    while active:
        screen.fill((7, 24, 33))

        if is_game_active:
            runtime += 1
            if runtime == config.fps:
                field.tick()
                runtime = 0

            player_x, player_y = player.get()
            if player.check_win():
                is_game_active = False
                config.character_img = pygame.transform.flip(config.character_img, True, True)
            elif not field.check_tile(player_x, player_y):
                is_game_active = False

        field.draw_grid(screen)
        player.draw_player(screen, is_game_active)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                    return True

                if not is_game_active and event.key == pygame.K_RETURN:
                    player.set(0, 0)
                    field.clear()
                    field.generate()
                    config.character_img = original_character_img
                    is_game_active = True

                if is_game_active:
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not (
                            pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('right')
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not (
                            pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('up')
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not (
                            pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('down')
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and not (
                            pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        player.move('left')
                    if (
                            event.key == pygame.K_d or event.key == pygame.K_RIGHT) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_right')
                    if (
                            event.key == pygame.K_w or event.key == pygame.K_UP) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_up')
                    if (
                            event.key == pygame.K_s or event.key == pygame.K_DOWN) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_down')
                    if (
                            event.key == pygame.K_a or event.key == pygame.K_LEFT) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        player.move('jump_left')

        pygame.display.flip()
        clock.tick(config.fps)

    return True
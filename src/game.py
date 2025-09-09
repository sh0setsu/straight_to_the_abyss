import pygame
from src.player import Player
from src.field import Field
import config

def get_abyss_color(level):
    base_dark = (10, 15, 40)
    base_deep = (20, 25, 60)
    
    darkness = min(level / 10, 0.8)
    
    r = int(base_deep[0] * (1 - darkness) + base_dark[0] * darkness)
    g = int(base_deep[1] * (1 - darkness) + base_dark[1] * darkness)
    b = int(base_deep[2] * (1 - darkness) + base_dark[2] * darkness)
    
    return (r, g, b)

def game_level_change():
    match config.current_level:
        case 0:
            config.tiles_count = int(config.m * config.n / 2)
            config.max_block_size = 4
            config.max_start_tile_time = 16
            config.key_challenge = False
        case 1:
            config.tiles_count -= 2
            config.max_block_size = 3
            config.max_start_tile_time = 12
        case 2:
            config.tiles_count -= 2
            config.key_challenge = True
        case 3:
            config.tiles_count -= 2
            config.portal_challenge = True
        case 4:
            config.tiles_count -= 2
        case 5:
            config.tiles_count -= 2
    return None


def game_running(active, screen):
    config.character_img = pygame.image.load('img/character.png').convert_alpha()
    config.character_img = pygame.transform.scale(config.character_img, (config.character_width * 7, config.character_height))
    clock = pygame.time.Clock()
    player = Player(0, 0)
    field = Field(config.n, config.m)
    field.create_portal()
    field.create_key()
    field.generate(config.tiles_count)
    runtime = 0
    running = True
    game_running = True
    player.set(0, 0)
    font = pygame.font.SysFont('Comic Sans', 36)  # Шрифт и размер
    while running and active:
        screen.fill(get_abyss_color(config.current_level))  # заливка окна
        text_surface = font.render(f"""level: {config.current_level}        points: 1456""", True, (255, 255, 255))
        screen.blit(text_surface, (config.left_margin + config.centalize_margin, config.height - config.upper_margin))
        if game_running:
            runtime += 1
            if runtime == config.fps:
                field.tick()
                runtime = 0

            player_x, player_y = player.get()
            field.check_key(player_x, player_y)
            if (field.check_tile(player_x, player_y) == -2):
                game_running = False 
                config.character_img = pygame.transform.flip(config.character_img, True, True)
            elif field.check_tile(player_x, player_y) == 0:
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
                    p_x, p_y = player.get()
                    if (field.check_tile(p_x, p_y) == -2):
                        config.current_level += 1
                    else:
                        config.current_level = 0
                    game_level_change()
                    player.set(0, 0)
                    field.clear()
                    field.create_portal()
                    field.create_key()
                    field.generate(config.tiles_count)
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
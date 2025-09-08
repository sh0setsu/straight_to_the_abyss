import pygame
import config
from src import button
import os

config.current_skin = os.path.join('img','character.png')


# def change_skin(new_value):
#     current_skin = new_value


def set_title(screen, title_size, title_text, screen_width, screen_height):
    font = pygame.font.Font(None, title_size)  # можно не стандартный
    text_surface = font.render(title_text, True, (107, 142, 35))
    text_rect = text_surface.get_rect(
        center=(screen_width / 2, screen_height / 100 * 8))  # тут можно было бы подправить форматирование
    screen.blit(text_surface, text_rect)


def skins_page(screen, bg_color, title_size, title, screen_width, screen_height, active=True):  # Дополни!
    background = pygame.image.load(os.path.join("assets", "background2.jpg")).convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    skin1_button = button.MenuButton(screen_width / 2 - (252 / 2), 200, 252, 74, "", os.path.join("skins", "skin1.png"),
                                     os.path.join("skins", "skin1.png"),
                                     "assets/click.mp3")
    skin2_button = button.MenuButton(screen_width / 2 - (252 / 2), 300, 252, 74, "", os.path.join("skins", "skin2.png"),
                                     os.path.join("skins", "skin2.png"),
                                     "assets/click.mp3")
    skin3_button = button.MenuButton(screen_width / 2 - (252 / 2), 400, 252, 74, "", os.path.join("skins", "skin3.png"),
                                     os.path.join("skins", "skin3.png"),
                                     "assets/click.mp3")
    back_button = button.MenuButton(screen_width / 2 - (252 / 2), 500, 252, 74, "Назад", "assets/pale.jpg",
                                    "assets/pale.jpg",
                                    "assets/click.mp3")
    buttons = [skin1_button, skin2_button, skin3_button, back_button]

    while active:
        screen.blit(background, (0, 0))
        set_title(screen, title_size, title, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

            if event.type == pygame.USEREVENT and event.button == back_button:
                return True

            if event.type == pygame.USEREVENT and event.button == skin1_button:
                config.current_skin = os.path.join("skins", "skin1.png")

            if event.type == pygame.USEREVENT and event.button == skin2_button:
                config.current_skin= os.path.join("skins", "skin2.png")

            if event.type == pygame.USEREVENT and event.button == skin3_button:
                config.current_skin = os.path.join("skins", "skin3.png")

            for i_button in buttons:
                i_button.handle_event(event)

        for i_button in buttons:
            i_button.check_hover(pygame.mouse.get_pos())
            i_button.draw(screen)

        pygame.display.flip()

    return True


def settings_page(screen, bg_color, title_size, title, screen_width, screen_height, active=True):  # Дополни!
    background = pygame.image.load(os.path.join("assets", "background2.jpg")).convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))
    back_button = button.MenuButton(screen_width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg",
                                    "assets/pale.jpg",
                                    "assets/click.mp3")
    skins_button = button.MenuButton(screen_width / 2 - (252 / 2), 300, 252, 74, "Скины", "assets/pale.jpg",
                                     "assets/pale.jpg",
                                     "assets/click.mp3")
    buttons = [back_button, skins_button]

    while active:
        screen.blit(background, (0, 0))
        set_title(screen, title_size, title, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

            if event.type == pygame.USEREVENT and event.button == back_button:
                return True

            if event.type == pygame.USEREVENT and event.button == skins_button:
                skins_page(screen, config.bg_color, 72, "Скины", config.width, config.height)
                # return False

            for i_button in buttons:
                i_button.handle_event(event)

        for i_button in buttons:
            i_button.check_hover(pygame.mouse.get_pos())
            i_button.draw(screen)

        pygame.display.flip()

    return True

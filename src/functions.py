import pygame
import sys
from src import button
import os


def set_title(screen, title_size, title_text, screen_width, screen_height):
    font = pygame.font.Font(None, title_size)  # можно не стандартный
    text_surface = font.render(title_text, True, (107, 142, 35))
    text_rect = text_surface.get_rect(
        center=(screen_width / 2, screen_height / 100 * 8))  # тут можно было бы подправить форматирование
    screen.blit(text_surface, text_rect)


def settings_page(screen, bg_color, title_size, title, screen_width, screen_height, active=True):  # Дополни!
    background = pygame.image.load(os.path.join("assets", "background2.jpg")).convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))
    back_button = button.MenuButton(screen_width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg",
                                    "assets/pale.jpg",
                                    "assets/click.mp3")
    buttons = [back_button]

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

            for i_button in buttons:
                i_button.handle_event(event)

        for i_button in buttons:
            i_button.check_hover(pygame.mouse.get_pos())
            i_button.draw(screen)

        pygame.display.flip()

    return True
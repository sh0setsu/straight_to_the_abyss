import pygame
import sys
from src import button


def exit_game():
    pygame.quit()
    sys.exit()


def set_title(screen, title_size, title_text, screen_width, screen_height):
    font = pygame.font.Font(None, title_size)
    text_surface = font.render(title_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 100 * 8))
    screen.blit(text_surface, text_rect)


def settings_page(screen, bg_color, title_size, title, screen_width, screen_height):
    back_button = button.MenuButton(screen_width / 2 - (252 / 2), 200, 252, 74, "Назад", "assets/pale.jpg", "assets/pale.jpg",
                             "assets/click.mp3")
    buttons = [back_button]

    running = True
    while running:
        screen.fill(bg_color)
        set_title(screen, title_size, title, screen_width, screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for i_button in buttons:
                i_button.handle_event(event)

        for i_button in buttons:
            i_button.check_hover(pygame.mouse.get_pos())
            i_button.draw(screen)

        pygame.display.flip()






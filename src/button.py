import pygame


class MenuButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path="assets/click.mp3"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.current_image = self.image ###
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        pygame.mixer.init(44100, -16, 2, 2048)
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path) ##########
        self.is_hovered = False
        self.last_hover_state = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 40)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_position):
        #self.is_hovered = self.rect.collidepoint(mouse_position)
        #self.hover_image.set_alpha(90)

        self.last_hover_state = self.is_hovered
        self.is_hovered = self.rect.collidepoint(mouse_position)

        # Изменяем изображение только при изменении состояния
        if self.is_hovered != self.last_hover_state:
            if self.is_hovered:
                self.current_image = self.hover_image
            else:
                self.current_image = self.image

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play() ###############3
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

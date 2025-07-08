import config

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, key):
        match key:
            case 'right':
                if self.x < config.m - 1:
                    self.x += 1
            case 'left':
                if self.x > 0:
                    self.x -= 1
            case 'up':
                if self.y > 0:
                    self.y -= 1
            case 'down':
                if self.y < (config.n - 1):
                    self.y += 1
            case 'jump_right':
                if self.x < config.m - 2:
                    self.x += 2
            case 'jump_left':
                if self.x > 1:
                    self.x -= 2
            case 'jump_up':
                if self.y > 1:
                    self.y -= 2
            case 'jump_down':
                if self.y < config.n - 2:
                    self.y += 2
        return None

    def set(self, x, y):
        self.x = x
        self.y = y
        return None

    def get(self):
        return self.x, self.y

    def draw_player(self, screen):
        screen.blit(config.character_img, (self.x * config.tile_width, self.y * config.tile_height))
        return None
    
    def check_win(self):
        if self.x == config.m - 1 and self.y == config.n - 1:
            return True
        return False
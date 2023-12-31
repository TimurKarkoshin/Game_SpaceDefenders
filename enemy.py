import pygame


class Enemy(pygame.sprite.Sprite):
    """
    Класс для реализации врагов и их коллизии
    """
    def __init__(self, window):
        super(Enemy, self).__init__()
        self.window = window
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def enemy_pozition(self):
        self.window.blit(self.image, self.rect)

    def update(self):
        self.y += 0.1
        self.rect.y = self.y

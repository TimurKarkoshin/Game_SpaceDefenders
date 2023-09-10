import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Клас для реализации пуль, их отрисовки и коллизии
    """
    def __init__(self, window, ship):
        super(Bullet, self).__init__()
        self.window = window
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (255, 242, 0)
        self.speed = 1.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def bullet_visual(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        self.update()

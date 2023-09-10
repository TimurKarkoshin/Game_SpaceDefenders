import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, window):

        super(Ship, self).__init__()
        self.window = window
        self.image = pygame.image.load('images/cool_ship.png')
        self.rect = self.image.get_rect()
        self.window_rect = window.get_rect()
        self.rect.centerx = self.window_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.window_rect.bottom
        self.move_right = False
        self.move_left = False

    def ship_display(self):
        """
        Отрисовка коробля
        :return:
        """
        self.window.blit(self.image, self.rect)

    def ship_pozition(self):
        """
        Позиция корабля на экране
        :return:
        """
        if self.move_right and self.rect.right < self.window_rect.right:
            self.center += 1.5
        if self.move_left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def ship_homelander(self):
        """
        Позиционирование корабля
        :return:
        """
        self.center = self.window_rect.centerx

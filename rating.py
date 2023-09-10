import pygame.font
from ship import Ship
from pygame.sprite import Group


class Score:

    def __init__(self, window, stats):
        self.window = window
        self.window_rect = window.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_top_score()
        self.image_hp()

    def image_score(self):
        """
        Устанавливает позицию счёта на экране
        :return:
        """
        self.scr_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.scr_img.get_rect()
        self.score_rect.left = self.window_rect.left + 40
        self.score_rect.top = 20

    def image_top_score(self):
        """
        Отображает лучший счёт
        :return:
        """
        self.hgh_scr_img = self.font.render(str(self.stats.top_score), True, self.text_color, (0, 0, 0))
        self.top_score_rect = self.hgh_scr_img.get_rect()
        self.top_score_rect.centerx = self.window_rect.centerx
        self.top_score_rect.top = self.window_rect.top + 20

    def image_hp(self):
        """
        Отображает кол-во здоровья корабля
        :return:
        """
        self.ships = Group()
        for ship_number in range(self.stats.ship_hp):
            ship = Ship(self.window)
            ship.rect.x = 550 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)

    def show_score(self):
        """
        Функция для отрисовки и взаимодействия эелементов совместно
        :return:
        """
        self.window.blit(self.scr_img, self.score_rect)
        self.window.blit(self.hgh_scr_img, self.top_score_rect)
        self.ships.draw(self.window)

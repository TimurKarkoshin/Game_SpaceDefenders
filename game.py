import pygame
import actions
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from rating import Score


def window_run():
    """
    Запускает игру, инициализирует окно и обеспечивает взаимодействие классов
    :return:
    """
    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Оборона в космосе')
    bg_color = (0, 0, 0)
    ship = Ship(window)
    bullets = Group()
    skull = Group()
    actions.create_army(window, skull)
    stats = Stats()
    scr = Score(window, stats)

    while True:
        actions.events(window, ship, bullets)
        if stats.run_game:
            ship.ship_pozition()
            actions.update_screen(bg_color, window, stats, scr, ship, skull, bullets)
            actions.update_bullets(window, stats, scr, skull, bullets)
            actions.skull_move(stats, window, scr, ship, skull, bullets)


window_run()

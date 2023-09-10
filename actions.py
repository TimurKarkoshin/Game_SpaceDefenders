import pygame
import sys
from bullet import Bullet
from enemy import Enemy
import time


def events(window, ship, bullets):
    """
    Обработка событий внутри окна
    :param window:
    :param ship:
    :param bullets:
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:
                ship.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(window, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(bg_color, window, stats, scr, ship, skulls, bullets):
    """
    Задаёт фон, обновляет экран и выводит экран при смерти
    :param bg_color:
    :param window:
    :param stats:
    :param scr:
    :param ship:
    :param skulls:
    :param bullets:
    :return:
    """
    window.fill(bg_color)
    scr.show_score()
    for bullet in bullets.sprites():
        bullet.bullet_visual()
    ship.ship_display()
    skulls.draw(window)
    pygame.display.flip()


def update_bullets(window, stats, scr, skulls, bullets):
    """
    Отрисовка пуль
    :param window:
    :param stats:
    :param scr:
    :param skulls:
    :param bullets:
    :return:
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, skulls, True, True)
    if collisions:
        for skulls in collisions.values():
            stats.score += 10 * len(skulls)
        scr.image_score()
        check_top_score(stats, scr)
        scr.image_hp()
    if len(skulls) == 0:
        bullets.empty()
        create_army(window, skulls)


def ship_destroing(stats, window, scr, ship, skulls, bullets):
    """
    Декларирует уничтожение корабля
    :param stats:
    :param window:
    :param scr:
    :param ship:
    :param skulls:
    :param bullets:
    :return:
    """
    if stats.ship_hp > 0:
        stats.ship_hp -= 1
        scr.image_hp()
        skulls.empty()
        bullets.empty()
        create_army(window, skulls)
        ship.ship_homelander()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def skull_move(stats, window, scr, ship, skulls, bullets):
    """
    Декларирует движение врагов
    :param stats:
    :param window:
    :param scr:
    :param ship:
    :param skulls:
    :param bullets:
    :return:
    """
    skulls.update()
    if pygame.sprite.spritecollideany(ship, skulls):
        ship_destroing(stats, window, scr, ship, skulls, bullets)
    skull_check(stats, window, scr, ship, skulls, bullets)


def skull_check(stats, window, scr, ship, skulls, bullets):
    """
    Проверяет позицию врагов
    :param stats:
    :param window:
    :param scr:
    :param ship:
    :param skulls:
    :param bullets:
    :return:
    """
    window_rect = window.get_rect()
    for skull in skulls.sprites():
        if skull.rect.bottom >= window_rect.bottom:
            ship_destroing(stats, window, scr, ship, skulls, bullets)
            break


def create_army(window, skulls):
    """
    Создаёт и описывает поведение врагов, устанавливает параметры скорости и поражения
    :param window:
    :param skulls:
    :return:
    """
    skull = Enemy(window)
    enemy_width = skull.rect.width
    enemy_x_count = int((800 - 2 * enemy_width) / enemy_width)
    enemy_height = skull.rect.height
    enemy_y_count = int((800 - 100 - 2 * enemy_height) / enemy_height)

    for height_enemy_row in range(enemy_y_count - 4):
        for one_enemy in range(enemy_x_count):
            skull = Enemy(window)
            skull.x = enemy_width + enemy_width * one_enemy
            skull.y = enemy_height + enemy_height * height_enemy_row
            skull.rect.x = skull.x
            skull.rect.y = skull.rect.height + skull.rect.height * height_enemy_row
            skulls.add(skull)


def check_top_score(stats, scr):
    """
    Проверяет лучший счёт
    :param stats:
    :param scr:
    :return:
    """
    if stats.score > stats.top_score:
        stats.top_score = stats.score
        scr.image_top_score()
        with open('topScore.txt', 'w') as ver:
            ver.write(str(stats.top_score))

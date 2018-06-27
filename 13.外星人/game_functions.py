import sys
import pygame
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint
from time import sleep


def check_events(ship, setting, scene, bullets, stats, play_button, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_keydown_events(event, ship, setting, scene, bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, setting, scene, ship, aliens, bullets)


def check_event_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_event_keydown_events(event, ship, setting, scene, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(setting, scene, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def ship_hit(setting, stats, scene, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        creat_fleet(setting, scene, ship, aliens)
        ship.center_ship()
        sleep(1.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def get_numer_rows(setting, ship_height, alien_height):
    available_space_y = (setting.game_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    print(number_rows)
    return number_rows


def get_number_aliens_x(setting, alien_width):
    available_space_x = setting.game_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def creat_fleet(setting, scene, ship, aliens):
    alien = Alien(setting, scene)
    number_aliens_x = get_number_aliens_x(setting, alien.rect.width)
    number_rows = get_numer_rows(setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(setting, scene, aliens, alien_number, row_number)


def creat_alien(setting, scene, aliens, alien_number, row_number):
    alien = Alien(setting, scene)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_aliens_bottom(setting, stats, scene, ship, aliens, bullets):
    scene_rect = scene.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= scene_rect.bottom:
            ship_hit(setting, stats, scene, ship, aliens, bullets)
            break


def update_aliens(setting, aliens, ship, stats, scene, bullets):
    check_fleet_edges(setting, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Mayday！！")
        ship_hit(setting, stats, scene, ship, aliens, bullets)
    check_aliens_bottom(setting, stats, scene, ship, aliens, bullets)


def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break


def change_fleet_direction(setting, aliens):
    for alien in aliens:
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1


def creat_stars(setting, scene, stars):
    for count in range(setting.star_count):
        star = Star(scene, setting)
        star.rect.x = randint(0, setting.game_width)
        star.rect.y = randint(0, setting.game_height)
        stars.add(star)


def fire_bullet(setting, scene, ship, bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting, scene, ship)
        bullets.add(new_bullet)


def update_bullets(bullets, aliens, setting, scene, ship):
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(setting, scene, ship, aliens, bullets)


def check_bullet_alien_collisions(setting, scene, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(setting, scene, ship, aliens)


def check_play_button(stats, play_button, mouse_x, mouse_y, setting, scene, ship, aliens, bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        creat_fleet(setting, scene, ship, aliens)
        ship.center_ship()


def update_scene(scene, setting, ship, aliens, bullets, stars, play_button, stats):
    scene.fill(setting.game_bgColor)
    stars.draw(scene)
    ship.blitme()
    aliens.draw(scene)

    for bullet in bullets:
        bullet.draw_bullet()
        bullet.update()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

import sys
import pygame
from bullet import Bullet


def check_events(ship, setting, scene, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_keydown_events(event, ship, setting, scene, bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup_events(event, ship)


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
    if event.key == pygame.K_Q:
        sys.exit()


def fire_bullet(setting, scene, ship, bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting, scene, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_scene(scene, setting, ship, bullets):
    scene.fill(setting.game_bgColor)
    ship.blitme()
    for bullet in bullets:
        bullet.draw_bullet()
        bullet.update()
    pygame.display.flip()

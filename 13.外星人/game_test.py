import pygame
from gamesetting import GameSetting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()

    gs = GameSetting()

    scene = pygame.display.set_mode(
        (gs.game_width, gs.game_height))
    pygame.display.set_caption(gs.game_name)

    stats = GameStats(gs)

    sp = Ship(scene, gs)

    stars = Group()
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(gs, scene, sp, aliens)
    gf.creat_stars(gs, scene, stars)
    while True:
        gf.check_events(sp, gs, scene, bullets)
        sp.update()
        gf.update_aliens(gs, aliens, sp)
        gf.update_bullets(bullets, aliens, gs, scene, sp)
        gf.update_scene(scene, gs, sp, aliens, bullets, stars)


run_game()

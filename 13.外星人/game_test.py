import pygame
from gamesetting import GameSetting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    pygame.init()

    gs = GameSetting()

    scene = pygame.display.set_mode(
        (gs.game_width, gs.game_height))
    pygame.display.set_caption(gs.game_name)

    play_button = Button(scene, gs, "Play")

    stats = GameStats(gs)

    sp = Ship(scene, gs)

    stars = Group()
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(gs, scene, sp, aliens)
    gf.creat_stars(gs, scene, stars)
    while True:
        gf.check_events(sp, gs, scene, bullets, stats, play_button, aliens)
        if stats.game_active:
            sp.update()
            gf.update_aliens(gs, aliens, sp, stats, scene, bullets)
            gf.update_bullets(bullets, aliens, gs, scene, sp)
        gf.update_scene(scene, gs, sp, aliens, bullets, stars, play_button, stats)


run_game()

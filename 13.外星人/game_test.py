import pygame
from gamesetting import GameSetting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()

    gs = GameSetting()

    scene = pygame.display.set_mode(
        (gs.game_width, gs.game_height))
    pygame.display.set_caption(gs.game_name)

    sp = Ship(scene, gs)

    bullets = Group()

    while True:
        gf.check_events(sp, gs, scene, bullets)
        sp.update()
        gf.update_bullets(bullets)
        gf.update_scene(scene, gs, sp, bullets)


run_game()

import pygame
from pygame.sprite import Sprite
from random import randint


class Bullet(Sprite):
    """docstring for bullet"""

    def __init__(self, setting, scene, ship):
        super().__init__()
        self.setting = setting
        self.scene = scene
        self.ship = ship
        self.rect = pygame.Rect(
            0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = tuple([randint(0, 255) for x in range(3)])
        # self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        pass

    def draw_bullet(self):
        pygame.draw.rect(self.scene, self.color, self.rect)

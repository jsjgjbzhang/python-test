import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """docstring for Alien"""

    def __init__(self, setting, scene):
        super().__init__()
        self.setting = setting
        self.scene = scene

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.setting.alien_speed_factor *
                   self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        scene_rect = self.scene.get_rect()
        if self.rect.right >= scene_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.scene.blit(self.image, self.rect)

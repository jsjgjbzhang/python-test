import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """docstring for Star"""

    def __init__(self, scene, setting):
        super().__init__()
        self.scene = scene
        self.setting = setting

        self.image = pygame.image.load("images/27-Stars.png")
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

    def blitme(self):
        self.scene.blit(self.image, self.rect)

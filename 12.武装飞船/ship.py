import pygame


class Ship():
    """docstring for Ship"""

    def __init__(self, scene, setting):
        self.scene = scene
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.scene_rect = scene.get_rect()
        self.setting = setting
        self.rect.centerx = self.scene_rect.centerx
        self.rect.bottom = self.scene_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.centerx += self.setting.ship_speed_factor
        if self.moving_left:
            self.centerx -= self.setting.ship_speed_factor
        if self.moving_up:
            self.centery -= self.setting.ship_speed_factor
        if self.moving_down:
            self.centery += self.setting.ship_speed_factor

        if(self.rect.centerx > self.scene_rect.right):
            self.centerx = self.scene_rect.left
        if(self.rect.centerx < self.scene_rect.left):
            self.centerx = self.scene_rect.right
        if(self.rect.centery > self.scene_rect.bottom):
            self.centery = self.scene_rect.top
        if(self.rect.centery < self.scene_rect.top):
            self.centery = self.scene_rect.bottom

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.scene.blit(self.image, self.rect)

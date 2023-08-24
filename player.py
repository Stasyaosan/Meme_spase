import pygame
windows_spase_im = pygame.transform.scale(pygame.image.load('windows.png'), (200, 150))
windows_push_im = pygame.transform.scale(pygame.image.load('windows push.png'), (50, 50))


class Spase_windows(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = windows_spase_im
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def move(self):
        self.rect.center = pygame.mouse.get_pos()
        self.x = self.rect.center[0]
        self.y = self.rect.center[1]


class Windows_push(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speed = 10
        self.x = x
        self.y = y
        self.image = windows_push_im
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def move(self):
        self.y -= 10
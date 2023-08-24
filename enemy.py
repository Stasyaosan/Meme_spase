mac_im = pygame.transform.scale(pygame.image.load('mac.png'), (300, 200))
pygame.transform.scale(pygame.image.load('mac push.png'), (50, 50))


class Mac_fignya():

    def __init__(self, x, y):
        super().__init__()
        self.image = mac_im

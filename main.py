import pygame.key
from player import *

pygame.init()

win_x = 1000
win_y = 800
win = pygame.display.set_mode([win_x, win_y])
clock = pygame.time.Clock()
run = True
mous_pos = [0, 0]

windows_spase = Spase_windows(win_x // 2, win_y - 150)
player = pygame.sprite.Group(windows_spase)


def redraw():
    win.fill((0, 0, 0))
    player.draw(win)
    pygame.display.update()


while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit()

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        windows_push = Windows_push(windows_spase.x, windows_spase.y)
        player.add(windows_push)



    windows_spase.move()
    redraw()

pygame.quit()

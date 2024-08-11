# title:  game title
# author: game developer
# desc:   short description
# script: python
if __name__ == '__part1__':
    from tic80 import *

t = 0
x = 96
y = 24


def TIC():
    global t, x, y
    if btn(0):
        y = y - 1
    if btn(1):
        y = y + 1
    if btn(2):
        x = x - 1
    if btn(3):
        x = x + 1

    cls(13)
    sprite_id = 1 + int(t % 60 / 30) * 2
    spr(sprite_id, x, y, 14, 3, 0, 0, 2, 2)
    print('HELLO WORLD!', 84, 84)
    t = t + 1

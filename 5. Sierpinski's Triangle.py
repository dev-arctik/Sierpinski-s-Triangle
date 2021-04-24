import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))

white = (255, 255, 255)

a = [250, 20]
b = [20, 480]
c = [480, 480]
x = [random.randrange(20, 480), random.randrange(20, 480)]

# music = pygame.mixer.music.load('Illuminati.mp3')
# pygame.mixer.music.play(-1)


def layout():
    pygame.draw.circle(win, white, (a), 2)
    pygame.draw.circle(win, white, (b), 2)
    pygame.draw.circle(win, white, (c), 2)


def draw():
    pnt = random.choice(['a', 'b', 'c'])

    if (pnt == 'a'):
        x[0] = (x[0]+a[0])//2
        x[1] = (x[1]+a[1])//2
    elif (pnt == 'b'):
        x[0] = (x[0]+b[0])//2
        x[1] = (x[1]+b[1])//2
    elif (pnt == 'c'):
        x[0] = (x[0]+c[0])//2
        x[1] = (x[1]+c[1])//2

    pygame.draw.circle(win, white, (x), 2)


# mainloop
run = True
while run:

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_SPACE]:
            run = False

    draw()

    pygame.display.update()

pygame.quit()

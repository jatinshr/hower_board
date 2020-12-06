import time
import pygame
hr=3
mn=0
sec=8

pygame.init()

# watch window
screen=pygame.display.set_mode((210,50))


# title,icon
pygame.display.set_caption("Timer")
icon= pygame.image.load('clock.png')
pygame.display.set_icon(icon)

#font type
font = pygame.font.Font('freesansbold.ttf', 22, bold=True)
textX = 10
textY = 10


def timer(h,m,s):
    i=1
    while True:

        s= s - i

        if s<0:
            m=m-i
            s=59
        if m<0:
            h = h - i
            m = 59
        if h<0:
            text = font.render("Time Left ", True, (0, 0, 0))
            screen.blit(text, (textX, textY))
            pygame.display.flip()
            screen.fill((255, 127, 39))
            time.sleep(1)

            break

        output = f"{h}:{m}:{s}"
        text = font.render("Time Left:- "+str(output), True, (0, 0, 0))
        screen.blit(text, (textX, textY))
        pygame.display.flip()
        screen.fill((255, 127, 39))
        time.sleep(1)




run=True
while run:

    timer(hr, mn, sec+1)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False



pygame.quit()



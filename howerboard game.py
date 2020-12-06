import pygame
import random
from pygame import mixer

# pygame initiation
pygame.init()

# no of balls
nb = 5
# board speed
bs = 20
# soccer speed
socspeedX = random.randint(-20, 20)
socspeedY = random.randint(1, 4)
if socspeedX == 0:
    socspeedX = 1

# window of game
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

# icon and name
pygame.display.set_caption('HOWER BOARD GAME')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('space.png')

# hower board
playerimg = pygame.image.load('board.png')
bposX = width / 2 - 50
bposY = height - 10
bposX_change = 0


def player(x, y):
    screen.blit(playerimg, (round(x), round(y)))


# balling intro

ballimg = []
ballX = []
ballY = []
ballX_change = []
ballY_change = []
socsX = []
socsY = []
no_of_balls = nb
for i in range(no_of_balls):
    socsX.append(random.randint(-20, 20))
    socsY.append(random.randint(1, 4))
    if socsX == 0:
        socsX.append(1)

    ballimg.append(pygame.image.load("ball.png"))
    ballX.append(random.randint(0, width - 24))
    ballY.append(0)
    ballX_change.append(socsX[i])
    ballY_change.append(socsY[i])


def ball(x, y, i):
    screen.blit(ballimg[i], (round(x), round(y)))


# collision

def collision(bposX, bposY, ballX, ballY):
    deltaX = (bposX - ballX)
    deltaY = abs(bposY - ballY - 24)

    if deltaX >= -88 and deltaX <= 10 and ballY > 600 - 40:
        return True

    else:
        return False


# game over
over = pygame.image.load("gameover.png")

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 22, bold=True)
textX = 10
textY = 10


def score_val(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# event loop
run = True
while run:
    screen.blit(background, (0, 0))
    screen.fill((31, 29, 32))

    # stablistaion of game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # for change in X axis
            if event.key == pygame.K_RIGHT:
                bposX_change = bs
            if event.key == pygame.K_LEFT:
                bposX_change = -bs

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                bposX_change = 0

    # insertion of board
    bposX += bposX_change
    if bposX <= 0:
        bposX = 0
    elif bposX > width - 100:
        bposX = width - 100
    # player(bposX, bposY)

    # insertion of ball

    for i in range(no_of_balls):
        if ballY[i] >= height - 21:
            ballY[i] = 800
            ballX[i] = 2
        ballX[i] += ballX_change[i]

        if ballX[i] <= 0:
            ballX_change[i] += abs(socsX[i])
            shoot = mixer.Sound('shoot.wav')
            shoot.play()
        if ballX[i] >= width - 24:
            shoot = mixer.Sound('shoot.wav')
            shoot.play()
            ballX_change[i] += -abs(socsX[i])
        ballY[i] += ballY_change[i]
        ball(ballX[i], ballY[i], i)

        coll_collision = collision(bposX, bposY, ballX[i], ballY[i])
        if coll_collision and ballY[i]<700:
            shoot = mixer.Sound('shoot.wav')
            shoot.play()
            ballY_change[i] += -socsY[i]
            score_value+=1
        if ballY[i] < 0:
            shoot = mixer.Sound('shoot.wav')
            shoot.play()
            ballY_change[i] += socsY[i]

        if ballY[i] == 800:
            pygame.display.flip()
            screen.blit(over, (0, 0))

    player(bposX, bposY)

    score_val(textX,textY)


    pygame.display.update()

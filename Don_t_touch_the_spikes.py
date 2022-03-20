import pygame
from random import randint as rand

# global variables
score = 0
spikelistl = ()
spikelistr = ()
birdY = 400
birdX = 238
birdA = -0.05
birdVY = 0
birdAX = 0
urbest = 0
lastscore = 0
alive = True
gamestarted = False
rl = 'right'
rls = 'right'
spikesanimation = 0
birdcondition = 'normal'
jumpreload = 0
# Initialize pygame
pygame.init()

# Create the screen 6,8:11
screen = pygame.display.set_mode((550, 900))
pygame.display.set_caption("Don't touch the spikes")
font = pygame.font.Font('freesansbold.ttf', 128)
font2 = pygame.font.Font('freesansbold.ttf', 32)


# make container
def container(r1, g1, b1, r2, g2, b2):
    pygame.draw.rect(screen, (r1, g1, b1), (0, 0, 550, 900))
    pygame.draw.rect(screen, (r2, g2, b2), (25, 25, 500, 850))


def scoredisp(r, g, b):
    global score
    if score < 10:
        point = font.render('0' + str(score), True, (r, g, b))
    else:
        point = font.render(str(score), True, (r, g, b))
    screen.blit(point, (205, 390))


def again(alive1, started, r, g, b):
    if not alive1:
        text = font2.render('Press any key to reset', True, (r, g, b))
        screen.blit(text, (100, 200))
    if not started:
        text1 = font2.render('Your best score: ' + str(urbest), True, (r, g, b))
        screen.blit(text1, (135, 550))
        text2 = font2.render('Your last score: ' + str(lastscore), True, (r, g, b))
        screen.blit(text2, (140, 625))
        text3 = font2.render("Don't touch the spikes", True, (r, g, b))
        screen.blit(text3, (100, 200))


def spikesgen():
    global score
    if score < 1:
        a = ()
    elif score < 3:
        a = [rand(0, 14), rand(0, 14)]
    elif score < 7:
        a = [rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 10:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 13:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 16:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 20:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 23:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14)]
    elif score < 25:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14), rand(0, 14)]
    elif score < 30:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 35:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 40:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    elif score < 50:
        a = [rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
             rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14)]
    else:
        a = [
            rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14), rand(0, 14),
            rand(0, 14), rand(0, 14), rand(0, 14)]
    return a


# Spike
def spike(x, lrud, r, g, b, animation):
    if lrud == 'up':
        pygame.draw.polygon(screen, (r, g, b), [(x, 25), (x + 40, 25), (x + 20, 55)])
    if lrud == 'down':
        pygame.draw.polygon(screen, (r, g, b), [(x, 875), (x + 40, 875), (x + 20, 845)])
    if lrud == 'left':
        y = animation / 40 - 10
        pygame.draw.polygon(screen, (r, g, b), [(y, x), (y, x + 40), (y + 30, x + 20)])
    if lrud == 'right':
        y = animation / 40
        pygame.draw.polygon(screen, (r, g, b), [(525 + y, x), (525 + y, x + 40), (495 + y, x + 20)])


# make spikes
def spikes(r, g, b):
    for i in range(9):
        spike(i * 53 + 43, 'up', r, g, b, 0)
    for i in range(9):
        spike(i * 53 + 43, 'down', r, g, b, 0)
    for i in spikelistl:
        spike(i * 54 + 53, 'left', r, g, b, spikesanimation)
    for i in spikelistr:
        spike(i * 54 + 53, 'right', r, g, b, spikesanimation)


# Make bird
def bird(x, y, z):
    global rls
    if z == 'normal':
        if rl == 'right':
            pygame.draw.rect(screen, (242, 49, 95), (x + 15, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 50, y + 15), 5)
            pygame.draw.polygon(screen, (242, 49, 95), [(x, y + 15), (x + 15, y + 15), (x + 15, y + 30)])
            pygame.draw.polygon(screen, (190, 33, 64), [(x + 25, y + 25), (x + 42, y + 25), (x + 25, y + 42)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 65, y + 15), (x + 65, y + 25), (x + 75, y + 25)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 65, y + 35), (x + 65, y + 25), (x + 75, y + 25)])
        else:
            pygame.draw.rect(screen, (242, 49, 95), (x + 10, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 25, y + 15), 5)
            pygame.draw.polygon(screen, (242, 49, 95), [(x + 75, y + 15), (x + 60, y + 15), (x + 60, y + 30)])
            pygame.draw.polygon(screen, (190, 33, 64), [(x + 50, y + 25), (x + 33, y + 25), (x + 50, y + 42)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 10, y + 15), (x + 10, y + 25), (x, y + 25)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 10, y + 35), (x + 10, y + 25), (x, y + 25)])
    elif z == 'jump':
        if rl == 'right':
            pygame.draw.rect(screen, (242, 49, 95), (x + 15, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 50, y + 15), 5)
            pygame.draw.polygon(screen, (242, 49, 95), [(x, y + 15), (x + 15, y + 15), (x + 15, y + 30)])
            pygame.draw.polygon(screen, (190, 33, 64), [(x + 25, y + 25), (x + 42, y + 25), (x + 25, y + 8)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 65, y + 15), (x + 65, y + 25), (x + 75, y + 15)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 65, y + 35), (x + 65, y + 25), (x + 75, y + 35)])
        else:
            pygame.draw.rect(screen, (242, 49, 95), (x + 10, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 25, y + 15), 5)
            pygame.draw.polygon(screen, (242, 49, 95), [(x + 75, y + 15), (x + 60, y + 15), (x + 60, y + 30)])
            pygame.draw.polygon(screen, (190, 33, 64), [(x + 50, y + 25), (x + 33, y + 25), (x + 50, y + 8)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 10, y + 15), (x + 10, y + 25), (x, y + 15)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 10, y + 35), (x + 10, y + 25), (x, y + 35)])
    elif z == 'dead':
        if rl == 'right':
            pygame.draw.rect(screen, (30, 30, 30), (x + 15, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 50, y + 15), 5)
            pygame.draw.polygon(screen, (30, 30, 30), [(x, y + 15), (x + 15, y + 15), (x + 15, y + 30)])
            pygame.draw.polygon(screen, (70, 70, 70), [(x + 25, y + 25), (x + 42, y + 25), (x + 25, y + 8)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 65, y + 15), (x + 65, y + 25), (x + 75, y + 15)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 65, y + 35), (x + 65, y + 25), (x + 75, y + 35)])
        else:
            pygame.draw.rect(screen, (30, 30, 30), (x + 10, y, 50, 50), border_radius=10)
            pygame.draw.circle(screen, (255, 255, 255), (x + 25, y + 15), 5)
            pygame.draw.polygon(screen, (30, 30, 30), [(x + 75, y + 15), (x + 60, y + 15), (x + 60, y + 30)])
            pygame.draw.polygon(screen, (70, 70, 70), [(x + 50, y + 25), (x + 33, y + 25), (x + 50, y + 8)])
            pygame.draw.polygon(screen, (242, 188, 0), [(x + 10, y + 15), (x + 10, y + 25), (x, y + 15)])
            pygame.draw.polygon(screen, (222, 162, 0), [(x + 10, y + 35), (x + 10, y + 25), (x, y + 35)])


# Make graphic
def graphic():
    global score, birdX, birdY, alive, gamestarted
    if score < 5:
        r = 129
        g = 129
        b = 129
        rb = 237
        gb = 237
        bb = 237
    elif score < 10:
        r = 98
        g = 117
        b = 129
        rb = 220
        gb = 236
        bb = 241
    elif score < 15:
        r = 130
        g = 108
        b = 97
        rb = 248
        gb = 235
        bb = 227
    elif score < 20:
        r = 117
        g = 126
        b = 99
        rb = 232
        gb = 241
        bb = 223
    elif score < 25:
        r = 117
        g = 126
        b = 99
        rb = 232
        gb = 241
        bb = 223
    elif score < 30:
        r = 255
        g = 255
        b = 255
        rb = 115
        gb = 115
        bb = 115
    elif score < 35:
        r = 0
        g = 175
        b = 237
        rb = 0
        gb = 97
        bb = 127
    elif score < 40:
        r = 124
        g = 213
        b = 0
        rb = 34
        gb = 116
        bb = 0
    elif score < 45:
        r = 0
        g = 105
        b = 245
        rb = 0
        gb = 40
        bb = 137
    elif score < 50:
        r = 253
        g = 30
        b = 104
        rb = 140
        gb = 15
        bb = 62
    elif score < 55:
        r = 255
        g = 255
        b = 255
        rb = 255
        gb = 174
        bb = 46
    elif score < 60:
        r = 255
        g = 255
        b = 255
        rb = 0
        gb = 152
        bb = 255
    else:
        r = 255
        g = 25
        b = 0
        rb = 0
        gb = 0
        bb = 0
    container(r, g, b, rb, gb, bb)
    spikes(r, g, b)
    scoredisp(r, g, b)
    again(alive, gamestarted, r, g, b)
    bird(birdX, birdY, birdcondition)


def birdcords(al, dead):  # birdX
    if al and dead:
        global birdX, birdY, birdA, score, rl, rls, spikesanimation, spikelistl, spikelistr
        if rl == 'right':
            birdX += birdAX
        else:
            birdX -= birdAX
        if birdX > 449:
            rl = 'left'
            rls = 'left'
            score += 1
            spikelistl = spikesgen()
        elif birdX < 26:
            rl = 'right'
            rls = 'right'
            score += 1
            spikelistr = spikesgen()
            spikesanimation = 500
        # BirdY
        birdY -= birdA
        birdA -= 0.0007


def birdcordsb(st):
    if not st:
        global birdY, birdA, birdVY
        if birdY < 425:
            birdA = 0.0001
        if birdY > 425:
            birdA = -0.0001
        birdVY -= birdA
        birdY -= birdVY


def birdcordsd(dead):
    if not dead:
        global birdX, birdY, birdA, score, rl, alive
        if not alive:
            if birdX < 25:
                rl = 'right'
            elif birdX > 450:
                rl = 'left'
            if birdY < 25:
                birdA = -birdA
            elif birdY > 825:
                birdA = -birdA
            if rl == 'right':
                birdX += 1
            else:
                birdX -= 1
            birdY -= birdA


def spikescolision():
    global birdX, birdY, alive, rl, birdcondition
    if birdY < 55 or birdY > 795:
        alive = False
        birdcondition = 'dead'
    if rl == 'right':
        for i in spikelistr:
            if (i + 1) * 54 - 20 < birdY < (i + 1) * 54 + 35 and birdX > 440:
                alive = False
                birdcondition = 'dead'
    else:
        for i in spikelistl:
            if (i + 1) * 54 - 20 < birdY < (i + 1) * 54 + 35 and 30 > birdX:
                alive = False
                birdcondition = 'dead'


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not gamestarted:
                gamestarted = True
                birdAX = 0.25
            if alive:
                birdA = 0.35
                birdcondition = 'jump'
                jumpreload = 300
            else:

                spikelistl = ()
                spikelistr = ()
                birdY = 400
                birdX = 238
                birdA = -0.05
                birdVY = 0
                birdAX = 0
                if score > urbest:
                    urbest = score
                lastscore = score
                score = 0
                alive = True
                gamestarted = False
                rl = 'right'
                rls = 'right'
                spikesanimation = 0
                birdcondition = 'normal'

    if jumpreload == 0:
        birdcondition = 'normal'
    jumpreload -= 1
    if spikesanimation < 1399 and rls == 'left':
        spikesanimation += 2
    elif spikesanimation > 1 and rls == 'right':
        spikesanimation -= 2
    birdcordsb(gamestarted)

    birdcordsd(alive)

    birdcords(alive, gamestarted)
    spikescolision()
    graphic()
    pygame.display.update()

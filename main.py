import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Stop Coronavirus")
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)

font = pygame.font.Font("Font.ttf", 32)
font2 = pygame.font.Font("Font.ttf", 48)

score = 0

weapons = {
    "Covered Cough": True,
    "Sanitizer": True,
    "Soap": True,
    "Wipes": True,
    "Social Distancing": True,
    "Uncovered Cough": False,
    "Shake Hands": False,
}
weapon = "Soap"


class Virus:
    def __init__(self):
        self.x = random.randint(10, 726)
        self.y = random.randint(10, 110)
        self.xchange = invadermove
        self.xmultiplier = 0.4
        self.ymultiplier = 0.05
        self.image = pygame.image.load("virus.png")

    def display(self):
        screen.blit(self.image, (self.x, self.y))

    def randomize(self):
        self.x = random.randint(10, 726)
        self.y = random.randint(10, 110)


def bullet(x, y, myweapon):
    screen.blit(pygame.image.load(myweapon + ".png"), (x, y))


def bulleticon(myweapon):
    screen.blit(pygame.image.load(myweapon + "64.png"), (726, 526))


def showscore(x=10, y=10, color=(200, 200, 200)):
    screen.blit(font.render("Coronaviruses stopped: {0}".format(score), True, color), (x, y))


def player(x, y):
    screen.blit(pygame.image.load("player.png"), (x, y))


def checkCollision():
    if bullet1X is not None:
        if -7 < bullet1X - invader1.x < 47 and 0 < bullet1Y - invader1.y < 40:
            return 1
        elif -7 < bullet1X - invader2.x < 47 and 0 < bullet1Y - invader2.y < 40:
            return 2
        else:
            return 0
    else:
        return -1


def virusGone(virus):
    global bullet1X
    global bullet1Y
    global weapon
    global multiplied
    global score
    bulletmusic = pygame.mixer.Sound("explosion.wav")
    bulletmusic.play()
    if virus == 1:
        screen.blit(pygame.image.load("explosion.png"), (invader1.x, invader1.y))
        pygame.display.update()
        time.sleep(0.5)
        invader1.randomize()
    else:
        screen.blit(pygame.image.load("explosion.png"), (invader2.x, invader2.y))
        pygame.display.update()
        time.sleep(0.5)
        invader2.randomize()
    bullet1X = None
    bullet1Y = None
    weapon = random.choice([key for key in weapons.keys()])
    score += 1
    multiplied = False


def gameover(myweapon=False):
    time.sleep(0.5)
    while invader1.y < 498 and invader2.y < 498:
        screen.fill((200, 100, 100))
        invader1.y += 1
        invader2.y += 1
        invader1.display()
        invader2.display()
        player(playerX, playerY)
        showscore()
        bulleticon(weapon)
        screen.blit(font.render("Weapon: " + weapon[:], True, (200, 200, 200)), (10, 558))
        screen.blit(font.render("WORLD", True, (200, 200, 200), (50, 50, 200)), (350, 562))
        pygame.display.update()
    pygame.mixer.music.stop()
    time.sleep(1)
    endsound = pygame.mixer.Sound("gameover.wav")
    endsound.play()
    screen.fill((200, 200, 200))
    screen.blit(pygame.image.load("gameover.png"), (144, 44))
    showscore(color=(0, 0, 0))
    pygame.display.update()
    time.sleep(4)
    if myweapon == "Shake Hands":
        pygame.mixer.music.load("ShakeHands.mp3")
        pygame.mixer.music.play()
    elif myweapon == "Uncovered Cough":
        pygame.mixer.music.load("UncoveredCough.mp3")
        pygame.mixer.music.play()
    screen.fill((200, 200, 200))
    screen.blit(font2.render("Well done, human!", True, (0, 0, 0)), (50, 50))
    screen.blit(
        font2.render("You prevented " + str(score) + " coronavirus" + str("es" if not score == 1 else ""), True,
                     (0, 0, 0)), (50, 150))
    screen.blit(font2.render("from infecting the world!", True, (0, 0, 0)), (50, 225))
    screen.blit(font2.render("You kept the world safe from " + str(math.ceil(score / 10)), True, (0, 0, 0)),
                (50, 325))
    screen.blit(
        font2.render("mutation" + str("s" if not math.ceil(score / 10) == 1 else "") + " of the coronavirus!", True,
                     (0, 0, 0)), (50, 400))
    screen.blit(font2.render("Press Q to quit, or R to restart", True, (0, 0, 0)), (50, 500))
    pygame.display.update()
    end = False
    while not end:
        for EVENT in pygame.event.get():
            if EVENT.type == pygame.KEYDOWN:
                if EVENT.key == pygame.K_q:
                    end = True
                if EVENT.key == pygame.K_r:
                    global repeat
                    repeat = True
                    end = True
            if EVENT.type == pygame.QUIT:
                end = True


screen.fill((200, 100, 100))
screen.blit(font.render("Attention, human!", True, (200, 200, 200)), (50, 50))
screen.blit(font.render("The human race is in danger!", True, (200, 200, 200)), (50, 125))
screen.blit(font.render("A new virus called the Coronavirus", True, (200, 200, 200)), (50, 200))
screen.blit(font.render("is spreading rapidly! It is up to", True, (200, 200, 200)), (50, 275))
screen.blit(font.render("you to protect the world from this", True, (200, 200, 200)), (50, 350))
screen.blit(font.render("deadly disease. Press C to continue", True, (200, 200, 200)), (50, 425))
screen.blit(font.render("or H to learn how to play.", True, (200, 200, 200)), (50, 500))
pygame.display.update()
pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play()
moveon = False
repeat = True
howto = False
while not moveon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            moveon = True
            repeat = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                moveon = True
                break
            if event.key == pygame.K_h:
                howto = True
                moveon = True
                break

if howto:
    pygame.mixer.music.load("HowToPlay.mp3")
    pygame.mixer.music.play()
    screen.fill((200, 100, 100))
    screen.blit(font.render("Move right and left by using the arrow keys.", True, (200, 200, 200)), (50, 50))
    screen.blit(font.render("You are randomly given a weapon for every shot.", True, (200, 200, 200)), (50, 125))
    screen.blit(font.render("Your current weapon is shown at the bottom of the screen.", True, (200, 200, 200)),
                (50, 200))
    screen.blit(font.render("The weapon can either help the virus or kill it.", True, (200, 200, 200)), (50, 275))
    screen.blit(font.render("If the weapon helps the virus, shoot away from the virus.", True, (200, 200, 200)),
                (50, 350))
    screen.blit(font.render("If not, try to hit the virus. Press space to shoot.", True, (200, 200, 200)), (50, 425))
    screen.blit(font.render("Remember, the world needs you. Press C to start.", True, (200, 200, 200)), (50, 500))
    pygame.display.update()
    moveon = False
    while not moveon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                moveon = True
                repeat = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    moveon = True
                    break


while repeat:
    repeat = False
    pygame.mixer.music.load("background.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    starttime = time.time()
    score = 0
    playerX = 368
    playerY = 500
    playerXchange = 0
    invadermove = random.choice([0.4, -0.4])
    multiplied = True
    invader1 = Virus()
    invader2 = Virus()
    while abs(invader1.x - invader2.x) < 74:
        invader2.randomize()
    bullet1X = None
    bullet1Y = None
    bullet1Ychange = 1
    weapon = "Soap"
    running = True
    while running:
        screen.fill((200, 100, 100))
        screen.blit(font.render("WORLD", True, (200, 200, 200), (50, 50, 200)), (350, 562))
        if time.time() - starttime > 20:
            pygame.mixer.music.rewind()
            pygame.mixer.music.play(-1)
            starttime = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerXchange = -0.5
                if event.key == pygame.K_RIGHT:
                    playerXchange = 0.5
                if event.key == pygame.K_SPACE:
                    if bullet1X is None:
                        bulletsound = pygame.mixer.Sound("laser.wav")
                        bulletsound.play()
                        bullet1X = playerX + 20
                        bullet1Y = 484
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerXchange = 0
        if playerX > 726 and playerXchange > 0:
            playerXchange = 0
        if playerX < 10 and playerXchange < 0:
            playerXchange = 0
        playerX += playerXchange
        player(playerX, playerY)
        if score % 10 == 0 and not multiplied:
            screen.fill((200, 0, 0))
            screen.blit(font.render("The virus has mutated and evolved!", True, (200, 200, 0)), (185, 232))
            screen.blit(font.render("It is now faster and harder to hit.", True, (200, 200, 0)), (200, 284))
            screen.blit(font.render("Be very cautious. Good luck!", True, (200, 200, 0)), (220, 336))
            pygame.display.update()
            time.sleep(5)
            invader1.xmultiplier += 0.1
            invader1.ymultiplier += 0.02
            invader2.xmultiplier += 0.1
            invader2.ymultiplier += 0.02
            bullet1Ychange += 0.2
            multiplied = True
        invader1.display()
        invader2.display()
        if invader1.x > 726:
            invader1.xchange = invader1.xmultiplier * -1
        elif invader1.x < 10:
            invader1.xchange = invader1.xmultiplier
        if invader2.x > 726:
            invader2.xchange = invader2.xmultiplier * -1
        elif invader2.x < 10:
            invader2.xchange = invader1.xmultiplier
        invader1.x += invader1.xchange
        invader1.y += invader1.ymultiplier
        invader2.x += invader2.xchange
        invader2.y += invader2.ymultiplier
        if bullet1Y is not None and bullet1Y < 10:
            bullet1X = None
            bullet1Y = None
            weapon = random.choice([key for key in weapons.keys()])
        if bullet1X is not None:
            bullet(bullet1X, bullet1Y, weapon)
            bullet1Y -= bullet1Ychange
        bulleticon(weapon)
        screen.blit(font.render("Weapon: " + weapon[:], True, (200, 200, 200)), (10, 558))
        showscore()
        collision = checkCollision()
        if collision == 1:
            if weapons[weapon]:
                virusGone(1)
            else:
                gameover(weapon)
                break
        elif collision == 2:
            if weapons[weapon]:
                virusGone(2)
            else:
                gameover(weapon)
                break
        if invader1.y > 436 or invader2.y > 436:
            gameover()
            break
        pygame.display.update()

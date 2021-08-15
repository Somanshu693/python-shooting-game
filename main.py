import pygame as py
from pygame import mixer
import random as rd
import math

py.init()

# Screen
screen = py.display.set_mode((1280, 720))

# Background Image
background = py.image.load('background.jpg')


# Name and Icon
py.display.set_caption("Yoda Fights The Dark")
icon = py.image.load('y.png')
py.display.set_icon(icon)

start_game = False
screen.fill((0, 0, 0))
screen.blit(background, (0, 0))
ready_font = py.font.Font('StarWars.ttf', 40)
start_font = py.font.Font('StarWars.ttf', 20)
owner_font = py.font.Font('StarWars.ttf',15)
ready_text = ready_font.render("ARE YOU READY TO FIGHT THE DARK ?", True, (206, 210, 204))
start_text = start_font.render("PRESS RETURN TO START", True, (255,250,204))
owner_text = owner_font.render("MADE BY : SOMANSHU GUPTA© ",True,(255,250,204))
screen.blit(ready_text, (230, 350))
screen.blit(start_text, (530, 450))
screen.blit(owner_text,(550,700))
py.display.update()

while True:
    for event in py.event.get():
        if event.type == py.KEYDOWN and event.key == py.K_RETURN:
            start_game = True
            # Background Sound
            mixer.music.load('The-Imperial-March.mp3')
            mixer.music.play(-1)
        if event.type == py.QUIT:
            py.quit()
    if start_game == True:
        break

# Player
playerImg = py.image.load('yoda.png')
playerX = 640
playerY = 595
playerX_change = 0

# Enemy
darth_vader = py.image.load('darth-vader.png')
darth_maul = py.image.load('darth-maul.png')
darth_sidious = py.image.load('darth-sidious.png')
darth_revan = py.image.load('darth-revan.png')
kylo_ren = py.image.load('kylo-ren.png')
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10
for i in range(no_of_enemies):
    enemyImg.append(darth_vader)
    enemyImg.append(darth_maul)
    enemyImg.append(darth_sidious)
    enemyImg.append(darth_revan)
    enemyImg.append(kylo_ren)
    enemyX.append(rd.randint(0, 1215))
    enemyY.append(rd.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)

# Bullet
bulletImg = py.image.load('saber.png')
bulletX = 0
bulletY = 595
bulletX_change = 0
bulletY_change = 12
bullet_state = "ready"

# Score
score_value = 0
font = py.font.Font('StarWars.ttf', 40)
textX = 10
textY = 10

# Game Over
over_font = py.font.Font('StarWars.ttf', 80)
over_font_quote = py.font.Font('StarWars.ttf', 30)
again_font = py.font.Font('StarWars.ttf', 20)
quit_font = py.font.Font('StarWars.ttf', 20)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (206, 210, 204))
    screen.blit(score, (x, y))


def game_over():
    over_text = over_font.render("YOU LOST", True, (216, 240, 252))
    screen.blit(over_text, (450, 250))
    over_quote = over_font_quote.render("YOU DON'T KNOW THE POWER OF THE DARK SIDE !", True, (235, 230, 240))
    screen.blit(over_quote, (250, 350))
    mixer.music.pause()
    sound = mixer.Sound('youdont.wav')
    sound.play()
    sound.fadeout(4400)



def play_again():
    again_text = again_font.render("PRESS RETURN TO PLAY AGAIN", True, (255,250,204))
    screen.blit(again_text, (500, 550))
    quit_text = quit_font.render("PRESS Q TO QUIT", True, (255,250,204))
    screen.blit(quit_text, (580, 570))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 2, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((math.pow(enemyX - bulletX, 2)) + math.pow(enemyY - bulletY, 2)))
    if distance < 60:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in py.event.get():
        latest_key = None
        if event.type == py.QUIT:
            running = False
        # Check which key: Left or Right
        if event.type == py.KEYDOWN:
            latest_key = event.key
            if event.key == py.K_LEFT:
                playerX_change = -4
            if event.key == py.K_RIGHT:
                playerX_change = 4
            if event.key == py.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('light-saber-on.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == py.K_RETURN:
                enemyImg = []
                enemyY = []
                enemyX_change = []
                enemyY_change = []
                no_of_enemies = 10
                score_value = 0

                for i in range(no_of_enemies):
                    enemyImg.append(darth_vader)
                    enemyImg.append(darth_maul)
                    enemyImg.append(darth_sidious)
                    enemyImg.append(darth_revan)
                    enemyImg.append(kylo_ren)
                    enemyX.append(rd.randint(0, 1215))
                    enemyY.append(rd.randint(50, 150))
                    enemyX_change.append(5)
                    enemyY_change.append(40)
                mixer.music.load('The-Imperial-March.mp3')
                mixer.music.play(-1)
            if event.key == py.K_q:
                quit()
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                playerX_change = 0

    # Boundary check for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1152:
        playerX = 1152

    # Enemy Movement
    for i in range(no_of_enemies):
        # Game Over
        if enemyY[i] > 480:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over()
            play_again()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1180:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('blaster-firing.wav')
            explosion_sound.play()
            bulletY = 595
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = rd.randint(0, 1215)
            enemyY[i] = rd.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 595
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    py.display.update()

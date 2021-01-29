import math
import random
import pygame
from pygame import mixer
import os
import configparser

configparser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'space_odyssey.cfg')
configparser.read(configFilePath)

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 950))

# Background
backgroundimage = configparser.get("images", "backgroundimage")
background = pygame.image.load(backgroundimage)

# mixer.music.load("background.wav")
# mixer.music.play(-1)
mixer.music.load("explosion.wav")
mixer.music.play(-1)

# game name and title
pygame.display.set_caption("mygame")
#icon = pygame.image.load('icon.png')
#pygame.display.set_icon(icon)

asteroid_speed = configparser.getint("integers", "asteroid_speed")
rocket1_img = pygame.image.load('rocket1.png')
rocket1_x = configparser.getint("integers", "rocket1_x")
rocket1_y = configparser.getint("integers", "rocket1_y")
rocket1_x_change = 0
rocket1_y_change = 0
rocket1_speed = configparser.getint("integers", "rocket1_speed")
asteroid_speed_rocket1 = asteroid_speed

rocket2_img = pygame.image.load('rocket2.png')
rocket2_x = configparser.getint("integers", "rocket2_x")
rocket2_y = configparser.getint("integers", "rocket2_y")
rocket2_x_change = 0
rocket2_y_change = 0
rocket2_speed = configparser.getint("integers", "rocket2_speed")
asteroid_speed_rocket2 = asteroid_speed

rocket3_img = pygame.image.load('rocket3.png')


asteroid_img = pygame.image.load('asteroid1.png')
boom_img = pygame.image.load('boom.png')


def rocket1(x, y):
    screen.blit(rocket1_img, (x, y))


def rocket2(x, y):
    screen.blit(rocket2_img, (x, y))


def asteroid(x, y):
    screen.blit(asteroid_img, (x, y))

game_font = configparser.get("fonts", "game_font")
over_font = pygame.font.Font(game_font, 64)
game_over_text = configparser.get("texts", "game_over_text")

level_font = pygame.font.Font(game_font, 30)
level_no = 1
level_count1 = 1
level_count2 = 1


def level(levelno):
    level_text = level_font.render('Level' + str(levelno), True, (255, 255, 255))
    screen.blit(level_text, (5, 5))


# stationer objects
sobjectImg = []
sobjectX1 = []
sobjectX2 = []
sobjectX3 = []
sobjectX4 = []
sobjectX5 = []

n = 7

for i in range(n):
    sobjectImg.append(pygame.image.load('ufo.png'))
    sobjectX1.append(random.randint(10, 900))
    sobjectX2.append(random.randint(10, 900))
    sobjectX3.append(random.randint(10, 900))
    sobjectX4.append(random.randint(10, 900))
    sobjectX5.append(random.randint(10, 900))


player1 = True
player2 = False

count1 = 0
count2 = 0
count = 1
countl = 2
score1 = 0
score2 = 0
final_score1 = 0
a1 = 1
final_score2 = 0
a2 = 1
time1 = 0
time2 = 0


def newgame():
    global rocket1_x, rocket1_speed, rocket1_x_change, rocket1_y_change, rocket1_y
    global rocket2_speed, rocket2_x, rocket2_x_change, rocket2_y, rocket2_y_change
    global asteroid_speed, asteroid_speed_rocket1, asteroid_speed_rocket2
    global player1, player2
    global count, count1, count2, countl
    global score1, score2, final_score1, final_score2, a1, a2
    global level_count1, level_count2, level_no
    global time1, time2

    screen.blit(background, (0, 0))
    over_font = pygame.font.Font(game_font, 64)
    over_text = over_font.render(game_over_text, True, (255, 255, 255))
    screen.blit(over_text, (300, 150))

    # print(str(score1) + "score1")
    score1_font = pygame.font.Font(game_font, 30)
    Score1_font = score1_font.render("Player1's score : " + str(score1-time1/100), True, (255, 255, 255))

    screen.blit(Score1_font, (300, 300))

    score2_font = pygame.font.Font(game_font, 30)
    # print(str(score2) + "score2")
    Score2_font = score2_font.render("Player2's score : " + str(score2-time2/100), True, (255, 255, 255))
    screen.blit(Score2_font, (300, 400))

    time1_font = score1_font.render("time penalty P1: " + str(time1/100), True, (255, 255, 255))
    time2_font = score1_font.render("time penalty P2: " + str(time2/100), True, (255, 255, 255))

    screen.blit(time1_font, (300, 500))
    screen.blit(time2_font, (300, 600))
    winner1_font = score1_font.render("WINNER : Player1 ", True, (255, 255, 255))
    winner2_font = score1_font.render("WINNER : Player2 ", True, (255, 255, 255))

    if(score1-time1/100 > score2-time2/100):
        screen.blit(winner1_font, (300, 800))
    else:
        screen.blit(winner2_font, (300, 800))

    pygame.display.update()
    pygame.time.delay(5000)

    asteroid_speed = 1
    player1 = True
    player2 = False

    count1 = 0
    count2 = 0
    count = 1
    countl = 2

    score1 = 0
    score2 = 0
    final_score1 = 0
    a1 = 1
    final_score2 = 0
    a2 = 1

    level_no = 1
    level_count1 = 1
    level_count2 = 1

    rocket2_x = 450
    rocket2_y = 30
    rocket2_x_change = 0
    rocket2_y_change = 0
    rocket2_speed = 7
    asteroid_speed_rocket2 = 1

    rocket1_x = 450
    rocket1_y = 840
    rocket1_x_change = 0
    rocket1_y_change = 0
    rocket1_speed = 7
    asteroid_speed_rocket1 = 1
    time1 = 0
    time2 = 0

    countl += -1
n = 7

for i in range(n):
    sobjectImg.append(pygame.image.load('ufo.png'))
    sobjectX1.append(random.randint(10, 900))
    sobjectX2.append(random.randint(10, 900))
    sobjectX3.append(random.randint(10, 900))
    sobjectX4.append(random.randint(10, 900))
    sobjectX5.append(random.randint(10, 900))


def col_w_mtr(ocket1_x, ocket1_y, mtr_x, mtr_y):
    global asteroid_speed
    global asteroid_speed_rocket1, rocket1_speed
    global asteroid_speed_rocket2, rocket2_speed
    global rocket1_x
    global rocket1_y
    global rocket2_x
    global rocket2_y
    global count1
    global count2
    global player1
    global player2
    global rocket1_y_change
    global rocket2_y_change
    global rocket1_x_change
    global rocket2_x_change
    global score1
    global final_score1
    global score2
    global final_score2
    distance = math.sqrt(math.pow((ocket1_x - mtr_x), 2) + math.pow((ocket1_y - mtr_y), 2))

    if distance < 60:
        # print('//////////////')
        # print(score1,score2)
       
        mixer.music.load("explosion.wav")
        mixer.music.play(0)
        pygame.time.delay(100)

        if (rocket1_x == ocket1_x and rocket1_y == ocket1_y):
            count1 += 1
            player2 = True
            player1 = False
            asteroid_speed = asteroid_speed_rocket2
            rocket2_speed += 1
            rocket1_x_change = 0
            rocket1_y_change = 0
            score1 = final_score1 + score1
            score2 = final_score2 + score2
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            pygame.display.update()
            pygame.time.delay(500)

        if (rocket2_x == ocket1_x and rocket2_y == ocket1_y):
            count2 += 1
            player2 = False
            player1 = True
            asteroid_speed = asteroid_speed_rocket1
            rocket1_speed += 1
            rocket2_x_change = 0
            rocket2_y_change = 0
            score2 = final_score2 + score2
            score1 = final_score1 + score1
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            pygame.display.update()
            pygame.time.delay(500)

        return True
    else:
        return False
# moving objects
m = 4
mobjectx1 = []
for i in range(m):
    mobjectx1.append(random.randint(-300, 0))
    mobjectx1.append(random.randint(900, 1200))
    mobjectx1.append(random.randint(-300, 0))
    mobjectx1.append(random.randint(900, 1200))

running = True
while(running):
    screen.blit(background, (0, 0))
    over_font = pygame.font.Font(game_font, 90)
    global over_text
    over_text = over_font.render('SPACE ODYSSEY', True, (255, 255, 255))
    screen.blit(over_text, (150, 150))
    pygame.display.update()
    pygame.time.delay(1000)
    x = 0
    y = 0
    for i in range(200):
        screen.blit(background, (0, 0))
        screen.blit(rocket3_img, (x, 250))
        x += 5

        screen.blit(over_text, (150, 150))
        pygame.display.update()

    running = False

running = True
while(running):
    screen.blit(background, (0, 0))
    over_font = pygame.font.Font(game_font, 90)

    over_text = over_font.render("GAME BEGINS IN", True, (255, 255, 255))
    screen.blit(over_text, (100, 150))
    pygame.display.update()
    pygame.time.delay(1000)
    over_text = over_font.render("3", True, (255, 255, 255))
    screen.blit(over_text, (450, 250))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(background, (0, 0))
    over_text = over_font.render("GAME BEGINS IN", True, (255, 255, 255))
    screen.blit(over_text, (100, 150))

    over_text = over_font.render("2", True, (255, 255, 255))
    screen.blit(over_text, (450, 250))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(background, (0, 0))
    over_text = over_font.render("GAME BEGINS IN", True, (255, 255, 255))
    screen.blit(over_text, (100, 150))

    over_text = over_font.render("1", True, (255, 255, 255))
    screen.blit(over_text, (450, 250))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(background, (0, 0))

    over_text = over_font.render("GO !!", True, (255, 255, 255))
    screen.blit(over_text, (450, 250))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(background, (0, 0))
    running = False

running = True

# ###############################################################################################
while running:
    # print(rocket1_x, " ", rocket1_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
# Background Image
    screen.blit(background, (0, 0))

    if event.type == pygame.KEYDOWN:
        if player1 is True:
            if event.key == pygame.K_LEFT:
                rocket1_x_change = -rocket1_speed
            if event.key == pygame.K_RIGHT:
                rocket1_x_change = +rocket1_speed
            if event.key == pygame.K_DOWN:
                rocket1_y_change = +rocket1_speed
            if event.key == pygame.K_UP:
                rocket1_y_change = -rocket1_speed

        if player2 is True:
            if event.key == pygame.K_a:
                rocket2_x_change = -rocket2_speed
            if event.key == pygame.K_d:
                rocket2_x_change = +rocket2_speed
            if event.key == pygame.K_s:
                rocket2_y_change = +rocket2_speed
            if event.key == pygame.K_w:
                rocket2_y_change = -rocket2_speed

    if event.type == pygame.KEYUP:
        if player1 is True:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocket1_x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                rocket1_y_change = 0
        if player2 is True:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                rocket2_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                rocket2_y_change = 0

    if player1 is True:
        turn_font = pygame.font.Font(game_font, 30)
        Turn_font = turn_font.render("Player1's turn", True, (255, 255, 255))
        screen.blit(Turn_font, (780, 10))

    if player2 is True:
        turn_font = pygame.font.Font(game_font, 30)
        Turn_font = turn_font.render("Player2's turn", True, (255, 255, 255))
        screen.blit(Turn_font, (780, 10))

    score1_font = pygame.font.Font(game_font, 30)
    a = str(score1)

    Score1_font = score1_font.render("Player1's score : " + a, True, (255, 255, 255))
    screen.blit(Score1_font, (10, 910))
    b = str(score2)

    score2_font = pygame.font.Font(game_font, 30)

    Score2_font = score2_font.render("Player2's score : " + b, True, (255, 255, 255))
    screen.blit(Score2_font, (690, 910))

    for i in range(n):
        screen.blit(sobjectImg[i], (sobjectX1[i], 120))
        screen.blit(sobjectImg[i], (sobjectX2[i], 270))
        screen.blit(sobjectImg[i], (sobjectX3[i], 450))
        screen.blit(sobjectImg[i], (sobjectX4[i], 600))
        screen.blit(sobjectImg[i], (sobjectX5[i], 750))

        mobjectx1[1] += asteroid_speed
        if mobjectx1[1] >= 920:
            mobjectx1[1] = random.randint(-300, 0)

        mobjectx1[2] += -asteroid_speed
        if mobjectx1[2] <= 0:
            mobjectx1[2] = random.randint(900, 1200)

        mobjectx1[3] += asteroid_speed
        if mobjectx1[3] >= 920:
            mobjectx1[3] = random.randint(-300, 0)

        mobjectx1[4] += -asteroid_speed
        if mobjectx1[4] <= 0:
            mobjectx1[4] = random.randint(900, 1200)

    rocket1_x += rocket1_x_change
    if(rocket1_x <= 10):
        rocket1_x = 10
    if(rocket1_x >= 920):
        rocket1_x = 920

    rocket1_y += rocket1_y_change
    if(rocket1_y >= 840):
        rocket1_y = 840
    if(rocket1_y <= 10):
        rocket1_y = 10

    rocket2_x += rocket2_x_change
    if(rocket2_x <= 10):
        rocket2_x = 10
    if(rocket2_x >= 920):
        rocket2_x = 920

    rocket2_y += rocket2_y_change
    if(rocket2_y >= 840):
        rocket2_y = 840
    if(rocket2_y <= 10):
        rocket2_y = 10

    if player1 is True:
        if a1 == level_count1:
            # print( " ...")
            if rocket1_y > 750:
                score1 = 0 + final_score1
            if rocket1_y < 750 and rocket1_y > 673:
                score1 = 5 + final_score1
            if rocket1_y > 600 and rocket1_y < 673:
                score1 = 15 + final_score1
            if 600 > rocket1_y and rocket1_y > 512:
                score1 = 20 + final_score1
            if 512 > rocket1_y and rocket1_y > 450:
                score1 = 30 + final_score1
            if 450 > rocket1_y and rocket1_y > 358:
                score1 = 35 + final_score1
            if 358 > rocket1_y and rocket1_y > 270:
                score1 = 45 + final_score1
            if 270 > rocket1_y and rocket1_y > 200:
                score1 = 50 + final_score1
            if 200 > rocket1_y and rocket1_y > 512:
                score1 = 60 + final_score1
            if 120 > rocket1_y:
                score1 = 65 + final_score1
                a1 += 1
                final_score1 = score1

    if player2 is True:
        if a2 == level_count2:
            # print( " ...")
            if rocket2_y > 750:
                score2 = 65 + final_score2
                a2 += 1
                final_score2 = score2
            if rocket2_y < 750 and rocket2_y > 673:
                score2 = 60 + final_score2
            if rocket2_y > 600 and rocket2_y < 673:
                score2 = 50 + final_score2
            if 600 > rocket2_y and rocket2_y > 512:
                score2 = 45 + final_score2
            if 512 > rocket2_y and rocket2_y > 450:
                score2 = 35 + final_score2
            if 450 > rocket2_y and rocket2_y > 358:
                score2 = 30 + final_score2
            if 358 > rocket2_y and rocket2_y > 270:
                score2 = 20 + final_score2
            if 270 > rocket2_y and rocket2_y > 200:
                score2 = 15 + final_score2
            if 200 > rocket2_y and rocket2_y > 512:
                score2 = 5 + final_score2
            if 120 > rocket2_y:
                score2 = 0 + final_score2

# colision with meteor for rocket 1

    if col_w_mtr(rocket1_x, rocket1_y, mobjectx1[1], 200):
        screen.blit(boom_img, (rocket1_x, rocket1_y))
        rocket1_x = 450
        rocket1_y = 840

    if col_w_mtr(rocket1_x, rocket1_y, mobjectx1[2], 358):
        screen.blit(boom_img, (rocket1_x, rocket1_y))
        rocket1_x = 450
        rocket1_y = 840

    if col_w_mtr(rocket1_x, rocket1_y, mobjectx1[3], 512):
        screen.blit(boom_img, (rocket1_x, rocket1_y))
        rocket1_x = 450
        rocket1_y = 840

    if col_w_mtr(rocket1_x, rocket1_y, mobjectx1[4], 673):
        screen.blit(boom_img, (rocket1_x, rocket1_y))
        rocket1_x = 450
        rocket1_y = 840
# cooision eith rocket 2 and meterooo

    if col_w_mtr(rocket2_x, rocket2_y, mobjectx1[1], 200):
        screen.blit(boom_img, (rocket2_x, rocket2_y))
        rocket2_x = 450
        rocket2_y = 30

    if col_w_mtr(rocket2_x, rocket2_y, mobjectx1[2], 358):
        screen.blit(boom_img, (rocket2_x, rocket2_y))
        rocket2_x = 450
        rocket2_y = 30

    if col_w_mtr(rocket2_x, rocket2_y, mobjectx1[3], 512):
        screen.blit(boom_img, (rocket2_x, rocket2_y))
        rocket2_x = 450
        rocket2_y = 30

    if col_w_mtr(rocket2_x, rocket2_y, mobjectx1[4], 673):
        screen.blit(boom_img, (rocket2_x, rocket2_y))
        rocket2_x = 450
        rocket2_y = 30

# collision with ufo????????????????????????????????????????????????????????
    for i in range(n):
        if col_w_mtr(rocket1_x, rocket1_y, sobjectX1[i], 120):
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            rocket1_x = 450
            rocket1_y = 840
        if col_w_mtr(rocket1_x, rocket1_y, sobjectX2[i], 270):
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            rocket1_x = 450
            rocket1_y = 840
        if col_w_mtr(rocket1_x, rocket1_y, sobjectX3[i], 450):
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            rocket1_x = 450
            rocket1_y = 840
        if col_w_mtr(rocket1_x, rocket1_y, sobjectX4[i], 600):
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            rocket1_x = 450
            rocket1_y = 840
        if col_w_mtr(rocket1_x, rocket1_y, sobjectX5[i], 750):
            screen.blit(boom_img, (rocket1_x, rocket1_y))
            rocket1_x = 450
            rocket1_y = 840
# collision with rocket2 and ufo////////////////////////////////////
    for i in range(n):
        if col_w_mtr(rocket2_x, rocket2_y, sobjectX1[i], 120):
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            rocket2_x = 450
            rocket2_y = 30
        if col_w_mtr(rocket2_x, rocket2_y, sobjectX2[i], 270):
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            rocket2_x = 450
            rocket2_y = 30
        if col_w_mtr(rocket2_x, rocket2_y, sobjectX3[i], 450):
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            rocket2_x = 450
            rocket2_y = 30
        if col_w_mtr(rocket2_x, rocket2_y, sobjectX4[i], 600):
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            rocket2_x = 450
            rocket2_y = 30
        if col_w_mtr(rocket2_x, rocket2_y, sobjectX5[i], 750):
            screen.blit(boom_img, (rocket2_x, rocket2_y))
            rocket2_x = 450
            rocket2_y = 30

    if rocket1_y <= 20:
        rocket1_y = 840
        rocket1_x = 450
        asteroid_speed_rocket1 += asteroid_speed_rocket1
        rocket1_speed += 1
        # asteroid_speed  = asteroid_speed_rocket2
        player1 = False

        if count2 == 0:
            player2 = True
            asteroid_speed = asteroid_speed_rocket2
            rocket2_speed += 1
        else:
            player2 = False
            player1 = True
            asteroid_speed = asteroid_speed_rocket1
            rocket1_speed += 1

        level_count1 += 1
        rocket2_x_change = 0
        rocket2_y_change = 0
        rocket1_x_change = 0
        rocket1_y_change = 0

    if (rocket2_y >= 800):
        rocket2_y = 30
        rocket2_x = 450
        asteroid_speed_rocket2 += asteroid_speed_rocket2
        rocket2_speed += 1
        # asteroid_speed = asteroid_speed_rocket1
        player2 = False
        if count1 == 0:
            player1 = True
            asteroid_speed = asteroid_speed_rocket1
            rocket1_speed += 1
        else:
            player1 = False
            player2 = True
            asteroid_speed = asteroid_speed_rocket2
            rocket2_speed += 1

        level_count2 += 1
        rocket1_x_change = 0
        rocket1_y_change = 0
        rocket2_x_change = 0
        rocket2_y_change = 0

    if player1 is True:
        time1 += 1
        level_no = level_count1
    if player2 is True:
        time2 += 1
        level_no = level_count2

    level(level_no)
    # new list being created
    if level_count1 >= level_count2:
        count = level_count2
    if level_count2 >= level_count1:
        count = level_count1

    if count == countl:
        sobjectX1.clear()
        sobjectX2.clear()
        sobjectX3.clear()
        sobjectX4.clear()
        sobjectX5.clear()
        countl += 1
        for i in range(n):
            sobjectImg.append(pygame.image.load('ufo.png'))
            sobjectX1.append(random.randint(10, 900))
            sobjectX2.append(random.randint(10, 900))
            sobjectX3.append(random.randint(10, 900))
            sobjectX4.append(random.randint(10, 900))
            sobjectX5.append(random.randint(10, 900))

    screen.blit(asteroid_img, (mobjectx1[1], 200))
    screen.blit(asteroid_img, (mobjectx1[2], 358))
    screen.blit(asteroid_img, (mobjectx1[3], 512))
    screen.blit(asteroid_img, (mobjectx1[4], 673))

    rocket1(rocket1_x, rocket1_y)

    rocket2(rocket2_x, rocket2_y)

    # scoring for player1
    # for moving objects
    # print(score1, score2)

    if count1 >= 1:
        if count2 >= 1:
            newgame()
            sobjectX1.clear()
            sobjectX2.clear()
            sobjectX3.clear()
            sobjectX4.clear()
            sobjectX5.clear()
            countl += 1
            for i in range(n):
                sobjectImg.append(pygame.image.load('ufo.png'))
                sobjectX1.append(random.randint(10, 900))
                sobjectX2.append(random.randint(10, 900))
                sobjectX3.append(random.randint(10, 900))
                sobjectX4.append(random.randint(10, 900))
                sobjectX5.append(random.randint(10, 900))

    screen.blit(asteroid_img, (mobjectx1[1], 200))
    screen.blit(asteroid_img, (mobjectx1[2], 358))
    screen.blit(asteroid_img, (mobjectx1[3], 512))
    screen.blit(asteroid_img, (mobjectx1[4], 673))

    pygame.display.update()

# Joseph Rock - jhr4qz & Rhyane Lowman - rll6bq

# Our game is based on The World's Hardest Game (with some minor differences)
# The user controls a red square with the arrow keys
# The user has three lives to begin with
# There will be 3 levels. In each level, the goal is to attain the purple circle without being hit by an enemy
# When the user runs out of lives, the game is over and the player has the option to play again
# Optional Features:
#   - The game will have enemies that move. Being hit by an enemy will result in the loss of a life
#   - There will be collectibles: key on level 2 and coins on level 3
#   - There are 3 levels
#   - We have a save point in the game after completing level 2
#   - Level 3 is a scrolling level

import gamebox
import pygame

camera = gamebox.Camera(800, 600)

# Level 1 scenery

player1 = gamebox.from_color(400, 475, 'blue', 20, 20)

target = gamebox.from_circle(400, 125, 'purple', 7)

fence1 = gamebox.from_color(400, 100, 'black', 400, 10)
fence2 = gamebox.from_color(200, 300, 'black', 10, 400)
fence3 = gamebox.from_color(600, 300, 'black', 10, 400)
fence4 = gamebox.from_color(400, 500, 'black', 400, 10)
course_obstacles_1 = [
    fence1, fence2, fence3, fence4
]

enemy1 = gamebox.from_circle(250, 150, 'red', 8)
enemy2 = gamebox.from_circle(250, 210, 'red', 8)
enemy3 = gamebox.from_circle(250, 270, 'red', 8)
enemy4 = gamebox.from_circle(250, 330, 'red', 8)
enemy5 = gamebox.from_circle(250, 390, 'red', 8)
enemy6 = gamebox.from_circle(550, 180, 'red', 8)
enemy7 = gamebox.from_circle(550, 240, 'red', 8)
enemy8 = gamebox.from_circle(550, 300, 'red', 8)
enemy9 = gamebox.from_circle(550, 360, 'red', 8)
enemy10 = gamebox.from_circle(550, 420, 'red', 8)
# enemy_look = gamebox.from_image(400, 300, 'enemy_look.png')
enemies1 = [
    enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10
]

# Level 2 scenery

key = gamebox.from_image(370, 217.5, 'https://www.freepngimg.com/thumb/key/15-golden-key-png-image-.png')
key.scale_by(0.12)

bound_gate = gamebox.from_color(400, 300, 'tan', 5, 80)
bound1 = gamebox.from_color(450, 180, 'black', 600, 10)
bound2 = gamebox.from_color(450, 420, 'black', 600, 10)
bound3 = gamebox.from_color(150, 220, 'black', 10, 80)
bound4 = gamebox.from_color(150, 380, 'black', 10, 80)
bound5 = gamebox.from_color(110, 260, 'black', 80, 10)
bound6 = gamebox.from_color(110, 340, 'black', 80, 10)
bound7 = gamebox.from_color(70, 300, 'black', 10, 80)
bound8 = gamebox.from_color(400, 220, 'black', 10, 80)
bound9 = gamebox.from_color(400, 380, 'black', 10, 80)
bound10 = gamebox.from_color(360, 255, 'black', 80, 10)
bound11 = gamebox.from_color(750, 300, 'black', 10, 240)
course_obstacles_2 = [bound1, bound2, bound3, bound4, bound5, bound6, bound7, bound8, bound9, bound10, bound11]

enemy11 = gamebox.from_circle(168, 237, 'red', 8)
enemy12 = gamebox.from_circle(382, 198, 'red', 8)
enemy13 = gamebox.from_circle(275, 198, 'red', 8)
enemy14 = gamebox.from_circle(275, 237, 'red', 8)
enemies2_1 = [enemy11, enemy12, enemy13, enemy14]

enemy15 = gamebox.from_circle(425, 200, 'red', 8)
enemy16 = gamebox.from_circle(500, 200, 'red', 8)
enemy17 = gamebox.from_circle(575, 200, 'red', 8)
enemy18 = gamebox.from_circle(650, 200, 'red', 8)
enemy19 = gamebox.from_circle(425, 400, 'red', 8)
enemy20 = gamebox.from_circle(500, 400, 'red', 8)
enemy21 = gamebox.from_circle(575, 400, 'red', 8)
enemy22 = gamebox.from_circle(650, 400, 'red', 8)
enemies2_2_1 = [enemy15, enemy16, enemy17, enemy18]
enemies2_2_2 = [enemy19, enemy20, enemy21, enemy22]

player2 = gamebox.from_color(110, 300, 'blue', 20, 20)

target2 = gamebox.from_circle(725, 300, 'purple', 7)

# Level 3 Scenery

outside1 = gamebox.from_color(400, 100, 'black', 600, 10)
outside2 = gamebox.from_color(100, 300, 'black', 10, 400)
outside3 = gamebox.from_color(400, 500, 'black', 600, 10)
outside4 = gamebox.from_color(700, 475, 'black', 10, 50)
outside5 = gamebox.from_color(700, 125, 'black', 10, 50)
outside6 = gamebox.from_color(950, 150, 'black', 500, 10)
outside7 = gamebox.from_color(950, 450, 'black', 500, 10)
outside8 = gamebox.from_color(1200, 175, 'black', 10, 50)
outside9 = gamebox.from_color(1200, 425, 'black', 10, 50)
outside10 = gamebox.from_color(1275, 200, 'black', 150, 10)
outside11 = gamebox.from_color(1275, 400, 'black', 150, 10)
outside12 = gamebox.from_color(1350, 300, 'black', 10, 200)
outside13 = gamebox.from_color(700, 425, 'black', 10, 150)
outside14 = gamebox.from_color(700, 175, 'black', 10, 150)
outside15 = gamebox.from_color(800, 200, 'black', 10, 100)
outside16 = gamebox.from_color(800, 400, 'black', 10, 100)
outside17 = gamebox.from_color(535, 300, 'black', 100, 10)
course_obstacles_3 = [outside1, outside2, outside3, outside4, outside5, outside6, outside7, outside8, outside9,
                      outside10, outside11, outside12, outside13, outside14, outside15, outside16, outside17]

open_door1 = gamebox.from_color(800, 300, 'lightgreen', 5, 100)
open_door2 = gamebox.from_color(1200, 300, 'lightgreen', 5, 200)

enemy23 = gamebox.from_circle(250, 470, 'red', 8)
enemy24 = gamebox.from_circle(280, 470, 'red', 8)
enemy25 = gamebox.from_circle(310, 130, 'red', 8)
enemy26 = gamebox.from_circle(340, 130, 'red', 8)
enemy27 = gamebox.from_circle(370, 470, 'red', 8)
enemy28 = gamebox.from_circle(400, 470, 'red', 8)
enemy29 = gamebox.from_circle(430, 130, 'red', 8)
enemy30 = gamebox.from_circle(460, 130, 'red', 8)
enemy36 = gamebox.from_circle(640, 470, 'red', 8)
enemy37 = gamebox.from_circle(670, 470, 'red', 8)
enemies3_1 = [enemy23, enemy24, enemy25, enemy26, enemy27, enemy28, enemy29, enemy30, enemy36, enemy37]

enemy31 = gamebox.from_circle(490, 120, 'red', 8)
enemy32 = gamebox.from_circle(520, 280, 'red', 8)
enemy33 = gamebox.from_circle(550, 120, 'red', 8)
enemy34 = gamebox.from_circle(580, 280, 'red', 8)
enemy50 = gamebox.from_circle(490, 480, 'red', 8)
enemy51 = gamebox.from_circle(520, 320, 'red', 8)
enemy52 = gamebox.from_circle(550, 480, 'red', 8)
enemy53 = gamebox.from_circle(580, 320, 'red', 8)
enemies3_1_1 = [enemy31, enemy32, enemy33, enemy34, enemy50, enemy51, enemy52, enemy53]

enemy_boss_1 = gamebox.from_circle(1150, 175, 'red', 18)
enemy_boss_3 = gamebox.from_circle(1150, 425, 'red', 18)
enemies3_bosses = [enemy_boss_1, enemy_boss_3]
enemy35 = gamebox.from_circle(826, 165, 'red', 8)
enemy36 = gamebox.from_circle(884, 165, 'red', 8)
enemy37 = gamebox.from_circle(942, 165, 'red', 8)
enemy38 = gamebox.from_circle(1000, 165, 'red', 8)
enemy39 = gamebox.from_circle(1058, 165, 'red', 8)
enemy40 = gamebox.from_circle(1116, 165, 'red', 8)
enemy41 = gamebox.from_circle(1174, 165, 'red', 8)
enemy42 = gamebox.from_circle(855, 435, 'red', 8)
enemy43 = gamebox.from_circle(913, 435, 'red', 8)
enemy44 = gamebox.from_circle(971, 435, 'red', 8)
enemy45 = gamebox.from_circle(1029, 435, 'red', 8)
enemy46 = gamebox.from_circle(1087, 435, 'red', 8)
enemy47 = gamebox.from_circle(1145, 435, 'red', 8)
enemies3_2 = [enemy35, enemy36, enemy37, enemy38, enemy39, enemy40, enemy41,
              enemy42, enemy43, enemy44, enemy45, enemy46, enemy47]

player3 = gamebox.from_color(150, 300, 'blue', 20, 20)

target3 = gamebox.from_circle(1300, 300, 'purple', 7)

coin1 = gamebox.from_image(375, 175, 'https://www.clipartwiki.com/clipimg/full/184-1848741_gold-coin-png.png')
coin1.scale_by(0.04)
coin2 = gamebox.from_image(375, 425, 'https://www.clipartwiki.com/clipimg/full/184-1848741_gold-coin-png.png')
coin2.scale_by(0.04)
coin3 = gamebox.from_image(700, 300, 'https://www.clipartwiki.com/clipimg/full/184-1848741_gold-coin-png.png')
coin3.scale_by(0.04)


# Level 1 Functions


def move_player1(keys, square):
    global level, lives
    if pygame.K_RIGHT in keys:
        square.x += 5
    if pygame.K_LEFT in keys:
        square.x -= 5
    if pygame.K_UP in keys:
        square.y -= 5
    if pygame.K_DOWN in keys:
        square.y += 5
    for obstacle in course_obstacles_1:
        square.move_to_stop_overlapping(obstacle)
    for enemy in enemies1:
        if square.touches(enemy):
            square.x = 400
            square.y = 475
            lives -= 1


def move_enemies1():
    for enemy in enemies1:
        camera.draw(enemy)
        if enemy.x >= 575:
            enemy.xspeed *= -1
        if enemy.x <= 225:
            enemy.xspeed *= -1
        enemy.move_speed()


# Level 2 Functions


def move_player2(keys, square):
    global level, lives, bound_10_bool
    if pygame.K_RIGHT in keys:
        square.x += 5
    if pygame.K_LEFT in keys:
        square.x -= 5
    if pygame.K_UP in keys:
        square.y -= 5
    if pygame.K_DOWN in keys:
        square.y += 5
    for obstacle in course_obstacles_2:
        square.move_to_stop_overlapping(obstacle)
    if square.touches(key):
        bound_10_bool = False
    for enemy in enemies2_1:
        if square.touches(enemy):
            square.x = 110
            square.y = 300
            lives -= 1
            bound_10_bool = True
    for enemy in enemies2_2_1:
        if square.touches(enemy):
            square.x = 110
            square.y = 300
            lives -= 1
            bound_10_bool = True
    for enemy in enemies2_2_2:
        if square.touches(enemy):
            square.x = 110
            square.y = 300
            lives -= 1
            bound_10_bool = True


def move_enemies2():
    for enemy in enemies2_1:
        camera.draw(enemy)
        if enemy.x >= 380 and enemy.y >= 235:
            enemy.x = 382
            enemy.y = 237
            enemy.xspeed = 0
            enemy.yspeed = -5
        if enemy.x >= 380 and enemy.y <= 200:
            enemy.x = 382
            enemy.y = 198
            enemy.xspeed = -5
            enemy.yspeed = 0
        if enemy.x <= 170 and enemy.y <= 200:
            enemy.x = 168
            enemy.y = 198
            enemy.xspeed = 0
            enemy.yspeed = 5
        if enemy.x <= 170 and enemy.y >= 235:
            enemy.x = 168
            enemy.y = 237
            enemy.xspeed = 5
            enemy.yspeed = 0
        enemy.move_speed()
    for enemy in enemies2_2_1:
        camera.draw(enemy)
        if enemy.y == 285:
            enemy.xspeed *= -1
            enemy.yspeed *= -1
        if enemy.y == 195:
            enemy.xspeed *= -1
            enemy.yspeed *= -1
        enemy.move_speed()
    for enemy in enemies2_2_2:
        camera.draw(enemy)
        if enemy.y == 315:
            enemy.xspeed *= -1
            enemy.yspeed *= -1
        if enemy.y == 405:
            enemy.xspeed *= -1
            enemy.yspeed *= -1
        enemy.move_speed()


# Level 3 Functions


def move_player3(keys, square):
    global level, lives, coin1_bool, coin2_bool, coin3_bool
    if pygame.K_RIGHT in keys:
        square.x += 5
    if pygame.K_LEFT in keys:
        square.x -= 5
    if pygame.K_UP in keys:
        square.y -= 5
    if pygame.K_DOWN in keys:
        square.y += 5
    for obstacle in course_obstacles_3:
        square.move_to_stop_overlapping(obstacle)
    for enemy in enemies3_1:
        if square.touches(enemy):
            square.x = 150
            square.y = 300
            lives -= 1
            coin1_bool = True
            coin2_bool = True
            coin3_bool = True
    for enemy in enemies3_1_1:
        if square.touches(enemy):
            square.x = 150
            square.y = 300
            lives -= 1
            coin1_bool = True
            coin2_bool = True
            coin3_bool = True
    for enemy in enemies3_2:
        if square.touches(enemy):
            square.x = 150
            square.y = 300
            lives -= 1
            coin1_bool = True
            coin2_bool = True
            coin3_bool = True
    for enemy in enemies3_bosses:
        if square.touches(enemy):
            square.x = 150
            square.y = 300
            lives -= 1
            coin1_bool = True
            coin2_bool = True
            coin3_bool = True


def move_enemies3():
    for enemy in enemies3_1:
        camera.draw(enemy)
        if enemy.y >= 480:
            enemy.yspeed *= -1
        if enemy.y <= 120:
            enemy.yspeed *= -1
        enemy.move_speed()
    for enemy in enemies3_1_1:
        camera.draw(enemy)
        for bound in course_obstacles_3:
            if enemy.top_touches(bound):
                enemy.yspeed *= -1
            if enemy.bottom_touches(bound):
                enemy.yspeed *= -1
        enemy.move_speed()
    for enemy in enemies3_2:
        camera.draw(enemy)
        if enemy.y >= 440:
            enemy.yspeed *= -1
        if enemy.y <= 160:
            enemy.yspeed *= -1
        enemy.move_speed()
    for enemy in enemies3_bosses:
        camera.draw(enemy)
    for enemy in enemies3_bosses:
        camera.draw(enemy)
        if enemy.x >= 1180:
            enemy.xspeed *= -1
        if enemy.x <= 820:
            enemy.xspeed *= -1
        if enemy.y <= 170:
            enemy.yspeed *= -1
        if enemy.y >= 430:
            enemy.yspeed *= -1
        enemy.move_speed()


# Global stuff
lives = 3
level = 'start'
save_point = False

# Level 1 code
for enemy in enemies1:
    enemy.xspeed = 6
level_one_display = gamebox.from_text(400, 50, 'Level 1', 40, 'black')
target_acquisition = False

# Level 2 code
pre_level_two_display = [gamebox.from_text(400, 250, 'Collect the key to open the gate', 40, 'black'),
                         gamebox.from_text(400, 100, 'Level 2', 40, 'black'),
                         gamebox.from_text(400, 520, 'Press space bar to continue', 40, 'black')]
level_two_display = gamebox.from_text(400, 50, 'Level 2', 40, 'black')
bound_10_bool = True
enemy11.xspeed = 5
enemy12.xspeed = -5
enemy13.xspeed = -5
enemy14.xspeed = 5
for enemy in enemies2_2_1:
    enemy.xspeed = 4
    enemy.yspeed = 5
for enemy in enemies2_2_2:
    enemy.xspeed = 4
    enemy.yspeed = -5

# Level 3 code
pre_level_three_display = [gamebox.from_text(400, 100, 'Level 3 - Final Level', 40, 'black'),
                           gamebox.from_text(400, 250, 'You have reached a save point', 40, 'black'),
                           gamebox.from_text(400, 520, 'Press space bar to continue', 40, 'black'),
                           gamebox.from_text(400, 550, 'Good Luck', 16, 'black'),
                           gamebox.from_text(400, 325, 'Collect all the coins in order to finish the level', 40, 'black'),
                           ]
for enemy in enemies3_1:
    enemy.yspeed = 10
for enemy in enemies3_1_1:
    enemy.yspeed = 7
for enemy in enemies3_2:
    enemy.yspeed = -5
enemy_boss_1.xspeed = -5
enemy_boss_1.yspeed = -5
enemy_boss_3.xspeed = 5
enemy_boss_3.yspeed = -5
coin1_bool = True
coin2_bool = True
coin3_bool = True


def tick(keys):
    global level, lives, target_acquisition, player1, player2, player3, bound_10_bool, save_point, coin1_bool, \
        coin2_bool, coin3_bool
    camera.clear('white')
    if level == 'start':
        player1 = gamebox.from_color(400, 475, 'blue', 20, 20)
        player2 = gamebox.from_color(110, 300, 'blue', 20, 20)
        player3 = gamebox.from_color(150, 300, 'blue', 20, 20)
        bound_10_bool = True
        coin1_bool = True
        coin2_bool = True
        coin3_bool = True
        camera.draw(gamebox.from_text(400, 135, "The Impossible Game", 64, 'blue'))
        camera.draw(gamebox.from_text(400, 280, 'Joseph Rock - jhr4qz & Rhyane Lowman - rll6bq', 28, 'black'))
        camera.draw(gamebox.from_text(400, 375, 'Use arrow keys to control blue square. Collect the purple circle',
                                      24, 'black'))
        camera.draw(gamebox.from_text(400, 400, 'without being hit by the red enemies to advance through levels.',
                                      24, 'black'))
        camera.draw(gamebox.from_text(400, 425, 'You have 3 lives', 24, 'black'))
        camera.draw(gamebox.from_text(400, 520, 'Press space bar to continue', 40, 'black'))
        if pygame.K_SPACE in keys:
            level = 1
    if lives == 0:
        camera.x = 400
        level = 'game over'
    if level == 'game over':
        camera.draw(gamebox.from_text(400, 200, 'GAME OVER', 48, 'black'))
        camera.draw(gamebox.from_text(400, 350, 'Press space bar to continue', 36, 'black'))
        if save_point:
            if pygame.K_SPACE in keys:
                level = 3
                lives = 3
        if not save_point:
            if pygame.K_SPACE in keys:
                level = 'start'
                lives = 3
    if level == 1:
        camera.draw(player1)
        camera.draw(level_one_display)
        for obstacle in course_obstacles_1:
            camera.draw(obstacle)
        camera.draw(target)
        move_player1(keys, player1)
        move_enemies1()
        if player1.touches(target):
            level = 'pre_level_2'
        camera.draw(gamebox.from_text(75, 50, 'Lives remaining: ' + str(lives), 24, 'blue'))
    if level == 'pre_level_2':
        for display in pre_level_two_display:
            camera.draw(display)
        if pygame.K_SPACE in keys:
            level = 2
    if level == 2:
        camera.draw(level_two_display)
        camera.draw(target2)
        camera.draw(gamebox.from_text(75, 50, 'Lives remaining: ' + str(lives), 24, 'blue'))
        for obstacle in course_obstacles_2:
            camera.draw(obstacle)
        if bound_10_bool:
            camera.draw(bound_gate)
            camera.draw(key)
            player2.move_to_stop_overlapping(bound_gate)
        camera.draw(player2)
        move_player2(keys, player2)
        move_enemies2()
        if player2.touches(target2):
            level = 'pre_level_3'
    if level == 'pre_level_3':
        for display in pre_level_three_display:
            camera.draw(display)
        if pygame.K_SPACE in keys:
            level = 3
    if level == 3:
        save_point = True
        move_player3(keys, player3)
        camera.draw(target3)
        camera.draw(player3)
        if coin1_bool:
            camera.draw(coin1)
        if player3.touches(coin1):
            coin1_bool = False
        if coin2_bool:
            camera.draw(coin2)
        if player3.touches(coin2):
            coin2_bool = False
        if coin3_bool:
            camera.draw(coin3)
        if player3.touches(coin3):
            coin3_bool = False
        move_enemies3()
        if player3.x >= 700:
            camera.x = 1000
            camera.draw(gamebox.from_text(1000, 50, 'Level 3 - Final Level', 40, 'black'))
            camera.draw(gamebox.from_text(675, 50, 'Lives remaining: ' + str(lives), 24, 'blue'))
        if player3.x < 700:
            camera.draw(gamebox.from_text(400, 50, 'Level 3 - Final Level', 40, 'black'))
            camera.draw(gamebox.from_text(75, 50, 'Lives remaining: ' + str(lives), 24, 'blue'))
            camera.x = 400
        for obstacle in course_obstacles_3:
            camera.draw(obstacle)
        camera.draw(open_door1)
        camera.draw(open_door2)
        if player3.touches(target3) and not coin1_bool and not coin2_bool and not coin3_bool:
            camera.x = 400
            level = 'end screen'
        if player3.touches(target3) and (coin1_bool or coin2_bool or coin3_bool):
            camera.draw(gamebox.from_text(1000, 520, 'You must collect all the coins first', 36, 'red'))
    if level == 'end screen':
        save_point = False
        camera.draw(gamebox.from_text(400, 250, 'Congratulations', 40, 'black'))
        camera.draw(gamebox.from_text(400, 350, 'You Win', 40, 'black'))
        camera.draw(gamebox.from_text(400, 520, 'Press space bar to play again', 40, 'black'))
        lives = 3
        if pygame.K_SPACE in keys:
            level = 'start'

    camera.display()


gamebox.timer_loop(30, tick)

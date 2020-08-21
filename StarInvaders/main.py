import pygame
import math
import random
import gameScreen


def bulletFire(x, y):
    gameScreen.charge = 'fire'
    gameScreen.screen.blit(gameScreen.bullet, (x + 20, y - 12))

def game_over_text():
    gameScreen.over_text = gameScreen.over_font.render("GAME OVER", True, (255, 255, 255))
    gameScreen.screen.blit(gameScreen.over_text, (200, 250))

def show_score():
    score = gameScreen.font.render("Score : " + str(gameScreen.score_value), True, (255, 255, 255))
    gameScreen.screen.blit(score, (20, 20))

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))
    if distance < 32:
        return True
    False

gameScreen.enemies()

check = True

# Game loop
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gameScreen.player_x_change -= gameScreen.player_speed

            if event.key == pygame.K_RIGHT:
                gameScreen.player_x_change += gameScreen.player_speed

            if event.key == pygame.K_SPACE:
                if gameScreen.charge is 'ready':
                    gameScreen.charge = 'fire'
                    gameScreen.bullet_x = gameScreen.player_x
                    gameScreen.bullet_y = gameScreen.player_y
                    bulletFire(gameScreen.bullet_x, gameScreen.bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                gameScreen.player_x_change = 0

    gameScreen.screen.blit(gameScreen.background, (0, 0))

    gameScreen.player_x += gameScreen.player_x_change

    if gameScreen.score_value % 10 == 0 and gameScreen.score_value > 0 and gameScreen.score_value / 2 > gameScreen.num_of_enemies:
        gameScreen.num_of_enemies += 2
        gameScreen.enemy_speed += 1
        gameScreen.bullet_y_change *= 1.5
        gameScreen.player_speed *= 1.2
        gameScreen.enemies()

    if gameScreen.player_x < 0:
        gameScreen.player_x = 0
    if gameScreen.player_x > 1216:
        gameScreen.player_x = 1216

    # Enemy Movement
    for i in range(gameScreen.num_of_enemies):

        # Game Over
        if gameScreen.enemy_y[i] > 535:
            for j in range(gameScreen.num_of_enemies):
                gameScreen.enemy_y[j] = 2000
            game_over_text()
            break

        gameScreen.enemy_x[i] += gameScreen.enemy_x_change[i]
        if gameScreen.enemy_x[i] < 0:
            gameScreen.enemy_x_change[i] *= -1
            gameScreen.enemy_y[i] += gameScreen.enemy_y_change[i]
        elif gameScreen.enemy_x[i] >= 1215:
            gameScreen.enemy_x_change[i] *= -1
            gameScreen.enemy_y[i] += gameScreen.enemy_y_change[i]

        # Collision
        collision = isCollision(gameScreen.enemy_x[i], gameScreen.enemy_y[i], gameScreen.bullet_x, gameScreen.bullet_y)
        if collision:
            gameScreen.bulletY = 700
            gameScreen.bullet_state = "ready"
            gameScreen.score_value += 1
            gameScreen.enemy_x[i] = random.randint(0, 1216)
            gameScreen.enemy_y[i] = random.randint(0, 250)
        gameScreen.enemyShow(gameScreen.enemy_x[i], gameScreen.enemy_y[i], i)

    if gameScreen.bullet_y < 0:
        gameScreen.bullet_y = 0
        gameScreen.charge = 'ready'

    if gameScreen.charge is 'fire':
        bulletFire(gameScreen.bullet_x, gameScreen.bullet_y)
        gameScreen.bullet_y -= gameScreen.bullet_y_change

    show_score()
    gameScreen.screen.blit(gameScreen.player, (gameScreen.player_x, gameScreen.player_y))
    pygame.display.update()
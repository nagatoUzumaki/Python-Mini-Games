import pygame
import math
import random

#Screen
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Game Screen")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player
player = pygame.image.load('spaceship.png')
player_x = 370
player_y = 300
player_x_change = 0
player_y_change = 0

# Enemy
enemy = pygame.image.load("monster.png")
enemy_x = 100
enemy_y = 100
enemy_x_change = 0.1
enemy_y_change = 0.1


check = True

# Game loop
while check:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      check = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_x_change -= 0.1
      if event.key == pygame.K_RIGHT:
        player_x_change += 0.1
    if event.type == pygame.KEYUP:
        player_x_change = 0

  player_x += player_x_change
  screen.fill((255, 255, 0))

  enemy_x += enemy_x_change
  screen.blit(enemy, (enemy_x, enemy_y))

  screen.blit(player, (player_x, player_y))


  pygame.display.update()


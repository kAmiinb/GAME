import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Моя Гра")

background_color = (255, 255, 255)
player_color = (0, 128, 255)

player_x, player_y = width // 2, height // 2
player_width, player_height = 50, 50
player_speed = 5

enemy_width, enemy_height = 50, 50
enemy_speed = 3

def create_enemy():
    enemy_x = random.randint(0, width - enemy_width)
    enemy_y = 0 - enemy_height
    enemy_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return enemy_x, enemy_y, enemy_color

enemies = [create_enemy()]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_height:
        player_y += player_speed

    for i in range(len(enemies)):
        enemy_x, enemy_y, enemy_color = enemies[i]
        enemy_y += enemy_speed
        enemies[i] = (enemy_x, enemy_y, enemy_color)

    if random.random() < 0.02:
        enemies.append(create_enemy())

    for enemy in enemies:
        enemy_x, enemy_y, enemy_color = enemy
        if (
            player_x < enemy_x + enemy_width
            and player_x + player_width > enemy_x
            and player_y < enemy_y + enemy_height
            and player_y + player_height > enemy_y
        ):
            print("Гра завершена!")
            running = False

    screen.fill(background_color)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    for enemy in enemies:
        pygame.draw.rect(screen, enemy[2], (enemy[0], enemy[1], enemy_width, enemy_height))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
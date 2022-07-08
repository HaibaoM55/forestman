import pygame
import random
import math
x = 400
y = 400
width = 70
height = 70
vel = 3

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

    
pygame.display.set_caption("Forestman")

player = pygame.sprite.Sprite()
player.image = pygame.image.load("player.png")



player.rect = player.image.get_rect()
player.rect.x = x
player.rect.y = y



trees = 18
tree_x = [
    0, 100, 200 , 500, 600, 700,
    0, 100, 200, 500, 600, 700,
    0, 100, 200 , 500, 600, 700
]
tree_y = [
    0, 0, 0, 0, 0, 0, 200 , 200, 200, 200, 
    200, 200, 400, 400, 400, 400, 400, 400
]
tree = pygame.sprite.Sprite()
tree.image = pygame.image.load("tree.png")


enemy = pygame.sprite.Sprite()
enemy.image = pygame.image.load("enemy.png")
enemy.rect = enemy.image.get_rect()
enemy.rect.x = 300
enemy.rect.y = 300


l = 0

gun = pygame.sprite.Sprite()
gun.image = pygame.image.load("gun.png")
gun.rect = gun.image.get_rect()
gun.rect.x = x + width
gun.rect.y = y

bullet = pygame.sprite.Sprite()
bullet.image = pygame.image.load("bullet.png")
bullet.rect = bullet.image.get_rect()
bullet.rect.x = x + width
bullet.rect.y = y

clock = pygame.time.Clock()


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                xas = 0
                bullet.rect.x = x + width
                bullet.rect.y = y
                for xas in range(100):
                    if l == 0:
                        bullet.rect.x += 10
                        screen.blit(bullet.image, bullet.rect)  
                        pygame.display.update()
                    else:
                        bullet.rect.x -= 10
                        screen.blit(bullet.image, bullet.rect)
                        pygame.display.update()
                    if(bullet.rect.x < enemy.rect.x + enemy.rect.width and bullet.rect.x > enemy.rect.x and bullet.rect.y < enemy.rect.y + enemy.rect.height and bullet.rect.y > enemy.rect.y):
                        caca = random.randint(1, 2)
                        if caca == 1:
                            enemy.rect.x = random.randint(230, 400)
                            enemy.rect.y = 70
                        elif caca == 2:
                            enemy.rect.x = random.randint(230, 400)
                            enemy.rect.y = 500
                        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel
    if keys[pygame.K_LSHIFT]:
        vel = 6
    else:
        vel = 3
    clock.tick(60)
    screen.fill((255, 255, 255))
    screen.blit(player.image, (x, y))
    mouse_pos = pygame.mouse.get_pos()
    gun.rect.y = y
    if(mouse_pos[0] < gun.rect.x):
        gun.rect.x = x - width - 27
        if l == 0:
            gun.image = pygame.transform.flip(gun.image, True, False)
            l = 1
    if(mouse_pos[0] == gun.rect.x):
        pass
    if(mouse_pos[0] > gun.rect.x):
        gun.rect.x = x + width
        if l == 1:
            gun.image = pygame.transform.flip(gun.image, True, False)
            l = 0
    for i in range(trees):
        screen.blit(tree.image, (tree_x[i], tree_y[i]))
    screen.blit(enemy.image, enemy.rect)
    screen.blit(gun.image, (gun.rect.x, gun.rect.y))
    screen.blit(enemy.image, enemy.rect)
    pygame.display.update()
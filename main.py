import pygame
import random
x = 400
y = 400
width = 70
height = 70
vel = 3

screen = pygame.display.set_mode((800, 600))

    
pygame.display.set_caption("Forestman beta")

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
gun_type = 1

bullet = pygame.sprite.Sprite()
bullet.image = pygame.image.load("bullet.png")
bullet.rect = bullet.image.get_rect()
bullet.rect.x = x + width
bullet.rect.y = y

bunny = pygame.sprite.Sprite()
bunny.image = pygame.image.load("bunny.png")
bunny.rect = bunny.image.get_rect()
bunny.rect.x = 100
bunny.rect.y = 100


inventory = pygame.sprite.Sprite()
inventory.image = pygame.image.load("inventory.png")
inventory.rect = inventory.image.get_rect()
inventory.rect.x = 644
inventory.rect.y = 0

clock = pygame.time.Clock()
bunny_nr = 5
bunny_x = []
bunny_y = []
for i in range(bunny_nr):
    bunny_x.append(random.randint(0, 800))
    bunny_y.append(random.randint(0, 600))
def jump(i, force, direction):
    if direction == "left":
        sar = random.randint(force - (force *2), 0)
    elif direction == "right":
        sar = random.randint(0, force) 
    bunny_x[i] += sar
    bunny_y[i] += sar

bush = pygame.sprite.Sprite()
bush.image = pygame.image.load("bush.png")
bush.rect = bush.image.get_rect()
bush_show = False

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if gun_type == 1:
                    xas = 0
                    bullet.rect.x = x + width
                    bullet.rect.y = y
                    for xas in range(100):
                        if l == 0:
                            bullet.rect.x += 10
                            screen.blit(bullet.image, bullet.rect)  
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
                if gun_type == 2:
                    for i in range(bunny_nr):
                        if(gun.rect.x < bunny_x[i] + 50 and gun.rect.x > bunny_x[i] and gun.rect.y < bunny_y[i] + 50 and gun.rect.y > bunny_y[i]):
                            bunny_nr -= 1
                            bunny_x.remove(bunny_x[i])
                            bunny_y.remove(bunny_y[i])
                            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bush_show == True:
                    bush_show = False
                else:
                    bush_show = True
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
    if keys[pygame.K_1]:
        gun.image = pygame.image.load("gun.png")
        gun_type = 1
    if keys[pygame.K_2]:
        gun.image = pygame.image.load("axe.png")
        gun_type = 2
    clock.tick(60)
    screen.fill((255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    gun.rect.y = y
    if(mouse_pos[0] < gun.rect.x):
        if(gun_type == 1):
            gun.rect.x = x - width - 27
        if(gun_type == 2):
            gun.rect.x = x - width + 27
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
    screen.blit(inventory.image, (inventory.rect.x, inventory.rect.y))
    for i in range(bunny_nr):
        if bunny_x[i] >= 800:
            bunny_x[i] = 0
        if bunny_x[i] <= 0:
            bunny_x[i] = 800
        if bunny_y[i] >= 600:
            bunny_y[i] = 0
        if bunny_y[i] <= 0:
            bunny_y[i] = 600
        speed = 1
        if(bunny_x[i] - x < 0 and bunny_x[i] - x > -100 and bunny_y[i] - y < 0 and bunny_y[i] - y > -100):
            speed = 10
        if(bunny_x[i] - x > 0 and bunny_x[i] - x < 100 and bunny_y[i] - y > 0 and bunny_y[i] - y < 100):
            speed = 10
        if(bush_show):
            speed = 1
        screen.blit(bunny.image, (bunny_x[i], bunny_y[i]))
        jump(i, speed, "left")
    screen.blit(enemy.image, enemy.rect)
    screen.blit(gun.image, (gun.rect.x, gun.rect.y))
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, (x, y))
    if bush_show:
        bush.rect.x = x 
        bush.rect.y = y + 20
        screen.blit(bush.image, bush.rect)
    pygame.display.update()
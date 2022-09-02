from tkinter.tix import Tree
import pygame
import random
import sys
import source.game_functions as gf
pygame.init()

x = 400
y = 400
width = 70
height = 70
vel = 3
if len(sys.argv) > 1:
    if sys.argv[1] == "-f" or sys.argv[1] == "--fullscreen":
        screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Available commands:")
        print(
        """
        |--------------------------------------------|
        |-h or --help: Prints this message and exits |
        |-f or --fullscreen: Runs the game fullscreen|
        |-t or --tutorial: Prints a tutorial message |
        |--------------------------------------------|
        """)
        exit()
    if sys.argv[1] == "-t" or sys.argv[1] == "-tutorial":
        print("""
        Tutorial
        """)
        exit()
else:
    screen = pygame.display.set_mode((800, 600))
    
pygame.display.set_caption("Forestman Alpha")

player = pygame.sprite.Sprite()
player.image = pygame.image.load("assets/player.png")



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
tree.image = pygame.image.load("assets/tree.png")


enemy = pygame.sprite.Sprite()
enemy.image = pygame.image.load("assets/enemy.png")
enemy.rect = enemy.image.get_rect()
enemy.rect.x = 300
enemy.rect.y = 300


l = 0

gun = pygame.sprite.Sprite()
gun.image = pygame.image.load("assets/gun.png")
gun.rect = gun.image.get_rect()
gun.rect.x = x + width
gun.rect.y = y
gun_type = 1

bullet = pygame.sprite.Sprite()
bullet.image = pygame.image.load("assets/bullet.png")
bullet.rect = bullet.image.get_rect()
bullet.rect.x = x + width
bullet.rect.y = y

bunny = pygame.sprite.Sprite()
bunny.image = pygame.image.load("assets/bunny.png")
bunny.rect = bunny.image.get_rect()
bunny.rect.x = 100
bunny.rect.y = 100


inventory = pygame.sprite.Sprite()
inventory.image = pygame.image.load("assets/inventory.png")
inventory.rect = inventory.image.get_rect()
inventory.rect.x = 644
inventory.rect.y = 0

clock = pygame.time.Clock()
bunny_nr = random.randint(1, 10)
bunny_x = []
bunny_y = []
bunny_dir = []
bunny_phase = 1
for i in range(bunny_nr):
    bunny_x.append(random.randint(0, 800))
    bunny_y.append(random.randint(0, 600))
    direc = random.randint(1, 2)
    if direc == 1:
        bunny_dir.append("left")
    else:
        bunny_dir.append("right")
bunny_phase = False
font = pygame.font.SysFont(None, 36)
text = font.render("Bunny phase!", True, (0, 119, 255))
"""
bunny_nr = random.randint(1, 10)
bunny_x = []
bunny_y = []
bunny_dir = []
bunny_phase += 1
for i in range(bunny_nr):
    bunny_x.append(random.randint(0, 800))
    bunny_y.append(random.randint(0, 600))
    direc = random.randint(1, 2)
    if direc == 1:
        bunny_dir.append("left")
    else:
        bunny_dir.append("right") 
"""
def jump(i, force, direction):
    if direction == "left":
        sar = random.randint(force - (force *2), 0)
    elif direction == "right":
        sar = random.randint(0, force) 
    bunny_x[i] += sar
    bunny_y[i] += sar

bush = pygame.sprite.Sprite()
bush.image = pygame.image.load("assets/bush.png")
bush.rect = bush.image.get_rect()
bush_show = False

bunny_killed = int(0)
bunny_killed_text = font.render(str(bunny_killed), True, (125, 125, 125))
game = False

class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def isclicked(self):
        action = False

        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

start_btn = button(290, 200, pygame.image.load("assets/start_btn.png").convert_alpha())
exit_btn = button(290, 300, pygame.image.load("assets/exit_btn.png").convert_alpha())

forestman = font.render("FORESTMAN", True, (65, 91, 161))

author = font.render("by HaibaoM55", True, (65, 91, 161))

class hunger_system():
    def __init__(self, x, y,image0, image1, image2, image3, image4):
        self.x = x
        self.y = y

        self.image0 = image0
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4

    level = int(4)

    def getHungerLevel(self):
        return self.level

    def setHungerLevel(self, level):
        self.level = level

    def draw(self):
        if self.level == 4:
            screen.blit(self.image4, (self.x, self.y))
        if self.level == 3:
            screen.blit(self.image3, (self.x, self.y))
        if self.level == 2:
            screen.blit(self.image2, (self.x, self.y))
        if self.level == 1:
            screen.blit(self.image1, (self.x, self.y))
        if self.level == 0:
            screen.blit(self.image0, (self.x, self.y))

h_img0 = pygame.image.load("assets/hunger/0.png").convert_alpha()
pygame.transform.scale(h_img0,(210, 210))

h_img1 = pygame.image.load("assets/hunger/1.png").convert_alpha()

h_img2 = pygame.image.load("assets/hunger/2.png").convert_alpha()

h_img3 = pygame.image.load("assets/hunger/3.png").convert_alpha()

h_img4 = pygame.image.load("assets/hunger/4.png").convert_alpha()

hunger = hunger_system(0, 0, h_img0, h_img1, h_img2, h_img3, h_img4)

del h_img0
del h_img1
del h_img2
del h_img3
del h_img4

gf.onload()
while(game == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((202, 228, 241))
    start_btn.draw()
    exit_btn.draw()
    if(start_btn.isclicked()):
        game = True
    if(exit_btn.isclicked()):
        exit()
    screen.blit(forestman, (300, 30))
    screen.blit(author, (400, 50))
    pygame.display.update()

while(game):
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
                            bunny_dir.remove(bunny_dir[i])
                            bunny_killed += 1
                            bunny_killed_text = font.render(str(bunny_killed), True, (125, 125, 125))
                            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bush_show == True:
                    bush_show = False
                else:
                    bush_show = True
                    vel = 1
    
    screen.fill((202, 228, 241))
    
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
        if bush_show:
            vel = 2
        else:
            vel = 6
    else:
        if bush_show:
            vel = 1
        else:
            vel = 3
    if keys[pygame.K_1]:
        gun.image = pygame.image.load("assets/gun.png")
        gun_type = 1
    if keys[pygame.K_2]:
        gun.image = pygame.image.load("assets/axe.png")
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
        jump(i, speed, bunny_dir[i])
    screen.blit(enemy.image, enemy.rect)
    screen.blit(gun.image, (gun.rect.x, gun.rect.y))
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, (x, y))
    if bush_show:
        bush.rect.x = x 
        bush.rect.y = y + 20
        screen.blit(bush.image, bush.rect)
    if bunny_phase:
        screen.blit(text, (300, 100))
    screen.blit(bunny_killed_text, (775, 25))
    hunger.draw()
    pygame.display.update()
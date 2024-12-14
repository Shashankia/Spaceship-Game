import pygame
import random

pygame.init()

w_width = 660 
w_height = 600
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Spaceship")

#loading images
bg = pygame.image.load("media/bg.png")
bg = pygame.transform.scale(bg, (w_width, w_height))
spaceship_img = pygame.image.load("media/spaceship.png")
bullet = pygame.image.load("media/bullet.png")
enemy_img = [pygame.image.load(f'media/alien{i}.png') for i in range (1,6)]
enemy = []

# game varibles
clock = pygame.time.Clock()
bullets = []
shoot_counter = 0
rows = 4
cols = 5

#spaceship class
class Spaceship():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 75
        self.height = 75
        self.vel = 8
        self.rect = (self.x, self.y, self.width, self.height)
        self.health = 5
        self.alive = True 

    def draw(self, window):
        window.blit(spaceship_img, (self.x, self.y))
        pygame.draw.rect(window, "red", (self.x, self.y+self.height, self.width, 10))
        pygame.draw.rect(window, "green", (self.x, self.y+self.height, round(self.width * (self.health/5)), 10))
        self.rect = (self.x, self.y, self.width, self.height)

class Projectile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 3

    def draw(self, window):
        self.y -= self.vel
        window.blit(bullet, (self.x, self.y))

class Enemies():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = enemy_img[random.randint(0,4)]
        self.move_counter = 0
        self.direction = 1

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        self.x += self.direction
        self.move_counter += 1
        if abs(self.move_counter) > 100:
            self.direction *= -1
            self.move_counter *= self.direction

#creating game objects
for row in range(rows):
    for col in range(cols):
        enemy.append((Enemies(100 + col*100, 100 + row*70)))       
           

#game variables 2
spaceship = Spaceship(round(w_width/2) - 34, w_height - 100)

#drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.blit(bg, (0,0))
    spaceship.draw(window)
    for i in enemy:
        i.draw(window)
    for projectile in bullets:
        projectile.draw(window)
    pygame.display.flip()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if shoot_counter > 0:
        shoot_counter += 1
    if shoot_counter > 10:
        shoot_counter = 0
    for projectile in bullets:
        if projectile.y > 0:
            projectile.y -= projectile.vel
        else:
            bullets.remove(projectile)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and spaceship.x>0:
        spaceship.x -= spaceship.vel

    elif keys[pygame.K_RIGHT] and spaceship.x<w_width - spaceship.width:
        spaceship.x += spaceship.vel

    if keys[pygame.K_SPACE] and shoot_counter == 0:
        if len(bullets) < 5:
            bullets.append(Projectile(spaceship.x + round(spaceship.width/2), spaceship.y))

        shoot_counter = 1
    DrawInGameLoop()

pygame.quit()

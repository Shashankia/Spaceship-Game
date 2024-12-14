import pygame
pygame.init()

w_width = 660 
w_height = 600
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Spaceship")

#loading images
bg = pygame.image.load("media/bg.png")
bg = pygame.transform.scale(bg, (w_width, w_height))
spaceship_img = pygame.image.load("media/spaceship.png")

#game variables
clock = pygame.time.Clock()

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

#game objects
spaceship = Spaceship(round(w_width/2)- 34, w_height- 100)

#drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.blit(bg, (0,0))
    spaceship.draw(window)
    pygame.display.flip()


#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and spaceship.x>0:
        spaceship.x -= spaceship.vel

    elif keys[pygame.K_RIGHT] and spaceship.x<w_width - spaceship.width:
        spaceship.x += spaceship.vel

    DrawInGameLoop()

pygame.quit()

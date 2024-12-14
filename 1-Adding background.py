import pygame
pygame.init()

w_width = 660 
w_height = 600
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Spaceship")

#loading images
bg = pygame.image.load("media/bg.png")
bg = pygame.transform.scale(bg, (w_width, w_height))

# game varibles
clock = pygame.time.Clock()

#drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.blit(bg, (0,0))
    pygame.display.flip()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    DrawInGameLoop()

pygame.quit()

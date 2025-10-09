import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
green = (0, 255, 0)
pygame.draw.circle(screen, green, (700, 300), 75)
pygame.draw.circle(screen, green, (100, 300), 75,5)
pygame.display.update()
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
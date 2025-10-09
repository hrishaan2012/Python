import pygame
pygame.init()
screen= pygame.display.set_mode((640, 440))
done= False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done= True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(20,20,600,400))
    pygame.display.flip()
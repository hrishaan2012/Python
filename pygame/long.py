import pygame
pygame.init()
screen_length, screen_width= 726,414
surface = pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption("Add image")
background = pygame.transform.scale("back.png").convert, (screen_length, screen_width)
steve=pygame.transform.scale("download.png").convert_alpha(), (200,200)
penguin_rect=pygame.Get_rect(100,100,200,200)
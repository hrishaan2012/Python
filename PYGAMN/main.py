import pygame 
import random
screen_width, screen_height = 800, 600
movement_speed = 5
font_size = 32

pygame.init()
bg_image=pygame.transform.scale(pygame.image.load("bg.jpg"),
                                (screen_width, screen_height))

font=pygame.font.Font(None, font_size)
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.color("dogerblue"))
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect=self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x= max(0, min(screen_width - self.rect.width, self.rect.x + x_change))
        self.rect.y= max(0, min(screen_height - self.rect.height, self.rect.y + y_change))

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dodge the Falling Objects!")
all_sprites_list=pygame.sprite.Group()
player=Player(pygame.color("dogerblue"),50,50)
player.rect.x,player.rect.y=random.randint(0, screen_width - player.rect.width), random.randint(0, screen_height - player.rect.height)
all_sprites_list.add(player)
player2=Player(pygame.color("red"),50,50)
player2.rect.x,player2.rect.y=random.randint(0, screen_width - player2.rect.width), random.randint(0, screen_height - player2.rect.height)
all_sprites_list.add(player2)

running_won = True, False
clock=pygame.time.Clock()
for event in pygame.event.get():
    if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
        running=False

if not running_won:
    keys=pygame.key.get_pressed()
    x_change=keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]*movement_speed
    y_change=keys[pygame.K_DOWN] - keys[pygame.K_UP]*movement_speed

    if player.rect.colliderect(player2.rect):
        all_sprites_list.remove(player2)
        running_won = True
screen.blit(bg_image, (0, 0))
all_sprites_list.draw(screen)
if running_won:
    text=font.render("You Won!", True, pygame.color("white"))
    screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2 - text.get_height()//2))

pygame.display.flip()
clock.tick(60)
pygame.quit()
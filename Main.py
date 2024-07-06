import pygame
from time import sleep

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

width, height = 700, 500
speed = 5

fi=0
mo="l"
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze")
background = pygame.transform.scale(pygame.image.load("background.webp"), (width, height))

player = GameSprite('hero.png', 20, 408, 4)
monster = GameSprite('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)
 
game = True
clock = pygame.time.Clock()
a = 1
pygame.mixer.init()
pygame.mixer.music.load('jungle.mp3')
pygame.mixer.music.play()
kick = pygame.mixer.Sound("kick.ogg")
money = pygame.mixer.Sound("money.ogg")
color_wall = 99,11,111
wall1 = pygame.Rect(200,220,20,350)
wall2 = pygame.Rect(270,300,240,20)
wall3 = pygame.Rect(-20,300,130,20)
wall4 = pygame.Rect(10,2,800,20)
wall5 = pygame.Rect(400,170,500,20)
wall6 = pygame.Rect(220,300,230,20)
wall7 = pygame.Rect(340,270,20,50)
wall8 = pygame.Rect(200,140,20,150)
wall9 = pygame.Rect(220,140,75,20)
wall10 = pygame.Rect(180,140,75,20)
pens = [wall1,wall2,wall3,wall4,wall4,wall5,wall6,wall7,wall8,wall9,wall10]
while game:
   
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 5:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT] and player.rect.x < 630:
        player.rect.x += 5
    if keys[pygame.K_UP] and player.rect.y > 5:
        player.rect.y -= 5
    if keys[pygame.K_DOWN] and player.rect.y < 430:
        player.rect.y += 5
    if keys[pygame.K_n]:
        monster.rect.y += 50
    
    if fi!=80 and mo=="l":
        monster.rect.x-=2.5
        fi+=1
    if fi!=-80 and mo=="r":
        monster.rect.x+=1.5
        fi-=1
    
    if fi==80:
        fi=0
        mo="r"
    if fi==-80:
        fi=0
        mo="l"
        
    


    window.blit(background,(0, 0))
    player.draw()
    monster.draw()
    final.draw()
    for i in pens:
        pygame.draw.rect(window, color_wall, i)
        if player.rect.colliderect(i):
            kick.play()
            sleep(1)
            game = False
        if player.rect.colliderect(monster):
            kick.play()
            sleep(0.1)
            game = False
        if player.rect.colliderect(final):
            money.play()
            sleep(0.25)
            game = False
    pygame.display.update()
    clock.tick(60)

import pygame

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
background = pygame.transform.scale(pygame.image.load("jungle.png"), (width, height))

player = GameSprite('hero.png', 318, 218, 4)
monster = GameSprite('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)
 
game = True
clock = pygame.time.Clock()
a = 1
pygame.mixer.init()
pygame.mixer.music.load('jungle.mp3')
pygame.mixer.music.play()
 
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

    pygame.display.update()
    clock.tick(60)
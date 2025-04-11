from pygame import *
from random import *
mixer.init()
clock=time.Clock()
font.init()

class GameSprite(sprite.Sprite):

   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):       
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y 
       self.size_x = size_x
       self.size_y = size_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - playersizey:
            self.rect.y += self.speed
    
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - playersizey:
            self.rect.y += self.speed

playersizex = 40
playersizey = 90

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((0, 0, 255))
display.set_caption("pingpong")


player1 = Player("racket.png", 3, win_height/2, 5, playersizex, playersizey)
player2 = Player("racket.png", win_width - 3 - playersizex, win_height/2, 5, playersizex, playersizey)

finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        player1.reset()
        player2.reset()





        player1.update1()
        player2.update2()

        display.update()
        clock.tick(60)
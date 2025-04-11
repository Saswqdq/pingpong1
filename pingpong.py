from pygame import *
from random import *
mixer.init()
clock=time.Clock()
font.init()

points = 0

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

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
        self.speed_y = self.speed
        self.speed_x = self.speed

    def update(self):
        global points
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        elif self.rect.y >= win_height - self.size_x:
            self.speed_y *= -1
        elif sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            self.speed_x *= -1
            points+=1

        
font = font.SysFont('Arial', 60)
lose = font.render('YOU LOSE', 1, (255, 0, 0))
win = font.render('YOU WIN', 1, (0, 255, 0))



playersizex = 30
playersizey = 100

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((0, 0, 255))
display.set_caption("pingpong")


player1 = Player("racket.png", 3, win_height/2, 5, playersizex, playersizey)
player2 = Player("racket.png", win_width - 3 - playersizex, win_height/2, 5, playersizex, playersizey)

ball = Ball('ball.png', win_width/2, win_height/2, 3, 30, 30)

finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill((0, 0, 255))

        player1.reset()
        player2.reset()
        ball.reset()


        if ball.rect.x <= 0 or ball.rect.x >= win_width - ball.size_x:
            window.blit(lose, (200, 200))
            finish = True

        if points == 20:
            window.blit(win, (200, 200))
            finish = True


        player1.update1()
        player2.update2()
        ball.update()

        display.update()
        clock.tick(60)

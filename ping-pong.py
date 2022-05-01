from pygame import *
from random import randint 


class Gamseprite(sprite.Sprite):
    def __init__(self, img1, x, y, speed, width, height):
        self.image = transform.scale(image.load(img1),(width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamseprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_left(self):

        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


window = display.set_mode((600,500))
back = (randint(0,255),randint(0,255),randint(0,255))
window.fill(back)
fst_img = ("a.png")
game = True
racket_right = Player(fst_img,520,200,9,50,150)
racket_left = Player(fst_img,20,200,9,50,150)
ball = Gamseprite("ball.png",200,200,7,50,50)
speed_x = 7
speed_y = 7
font.init()
font1 = font.Font(None, 35)
lose = font1.render("Game over",1,(180,0,0))

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    racket_right.update_right()
    racket_left.update_left()

    racket_right.reset()
    racket_left.reset()
    ball.reset()

    ball.rect.x += speed_x
    ball.rect.y -= speed_y
    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1
    if sprite.collide_rect(racket_right, ball) or sprite.collide_rect(racket_left,ball):
        speed_x *= -1
    if ball.rect.x < 0 or ball.rect.x > 500:
        game = False
        window.blit(lose, (200,200))
    display.update()
    time.delay(50)
    window.fill(back)
    

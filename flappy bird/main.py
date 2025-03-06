#remember collision of pipes if pygame.sprite.groupcollide(bird_group, pipe_group, False, False)
import pygame
from pygame.locals import *
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH = 864
HEIGHT = 936

#variables
highscore = 10
game_over = False
pipe_gap = 200
pipe_frequency = 1000
last_pipe = pygame.time.get_ticks()-pipe_frequency
flying = False
ground_scroll = 0
scroll_speed = 5
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('impact',50)
score = 0
CAPTION = pygame.display.set_caption('Floppy Chicken')

backround = pygame.image.load('flappy bird/images/flappy bird bg.png')
ground = pygame.image.load('flappy bird/images/flappy bird ground.png')

def draw_text(text,font,color,x,y):
    ing = font.render(text,True,color)
    screen.blit(ing,(x,y))

def reset_game():
    chicken.v = 0
    chicken.rect.y = HEIGHT/2
    drainss.empty()
    score = 0
    game_over = False
    flying = False

class Chicken(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.v = 0
        self.clicked = False
        self.max_v = 20
        self.counter = 0
        for num in range (1,5):
            img = pygame.image.load(f'flappy bird/images/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        global game_over, flying
        if flying == True:
            self.v += 1
            if self.v > self.max_v:
                self.v = self.max_v
            if self.rect.bottom < HEIGHT - 168:
                self.rect.y += int(self.v)

        if game_over == False:
            if pygame.mouse.get_pressed()[0] != 1:
                self.clicked == False            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.rect.top > 0:
                    self.clicked == True
                    self.v = -7

            self.counter += 1
            flap = 10
            if self.counter > flap:
                self.counter = 0
                self.index += 1 
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

        if chicken.rect.bottom > HEIGHT - 168 or pygame.sprite.groupcollide(chicken_group,drainss,False,False):
            if game_over == False:
                game_over = True
                self.v = 5

        if chicken.rect.bottom > HEIGHT - 168:
            self.rect.bottom = HEIGHT - 168

class Drains(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.passed = False
        self.image = pygame.image.load('flappy bird/images/pipe.png')
        self.rect = self.image.get_rect()

        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - pipe_gap/2]

        if pos == -1:
             self.rect.topleft = [x,y + pipe_gap/2]   

    def update(self):
        self.rect.x -= 5 
        if self.rect.right < 0:
            self.kill()

class Button:
    global game_over, flying
    def __init__(self,x,y):
        self.image = pygame.image.load('flappy bird/images/restart.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
       
chicken = Chicken(100,int(HEIGHT/2))
chicken_group = pygame.sprite.Group()
chicken_group.add(chicken)
drainss = pygame.sprite.Group()

running = True
while running:
    clock.tick(60)
    screen.fill('black')
    screen.blit(backround,(0,0))
    chicken_group.draw(screen)
    chicken_group.update()
    drainss.draw(screen)
    screen.blit(ground,(ground_scroll,HEIGHT - 168))

    if len(drainss)>0:
        if drainss.sprites()[0].rect.left < chicken_group.sprites()[0].rect.left:
            if drainss.sprites()[0].passed == False:
                score += 1
                drainss.sprites()[0].passed = True
    draw_text(f'Score{str(score)}',font,'black',50,25)
    draw_text(f'Highscore:{str(highscore)}',font,'black',50,100)
    time = pygame.time.get_ticks()
    if time - last_pipe > pipe_frequency:
        pipe_height = randint(-150,150)
        top_pipe = Drains(WIDTH,int(HEIGHT/2) + pipe_height,1)
        bottom_pipe = Drains(WIDTH,int(HEIGHT/2) + pipe_height,-1)
        drainss.add(top_pipe)
        drainss.add(bottom_pipe)
        last_pipe = time
    if game_over == False:
        drainss.update()
    if game_over == False:
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()
pygame.quit()

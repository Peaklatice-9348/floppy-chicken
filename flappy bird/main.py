import pygame
from pygame.locals import *
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH = 864
HEIGHT = 936

#variables
game_over = False
flying = False
ground_scroll = 0
scroll_speed = 5
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('impact',200)
CAPTION = pygame.display.set_caption('Floppy Chicken')

backround = pygame.image.load('flappy bird/images/flappy bird bg.png')
ground = pygame.image.load('flappy bird/images/flappy bird ground.png')

class Chicken(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.v = 0
        self.clicked = False
        self.max_v = 15
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
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True
                self.v = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
            self.counter += 1
            flap = 10
            if self.counter > flap:
                self.counter = 0
                self.index += 1 
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
        if chicken.rect.bottom > HEIGHT - 168:
            self.rect.bottom = HEIGHT - 168
            game_over = True
            flying = False
            self.v = 0

         
chicken = Chicken(100,int(HEIGHT/2))
chicken_group = pygame.sprite.Group()
chicken_group.add(chicken)





running = True
while running:
    clock.tick(60)
    screen.fill('black')
    screen.blit(backround,(0,0))
    chicken_group.draw(screen)
    chicken_group.update()
    screen.blit(ground,(ground_scroll,HEIGHT - 168))
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

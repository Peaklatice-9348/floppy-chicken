import pygame
from pygame.locals import *
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH = 864
HEIGHT = 936

#variables
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
        self.counter = 0
        for num in range (1,4):
            img = pygame.image.load(f'flappy bird/images/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        pass
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
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()

import pygame 
from random import *
import numpy as np

color = (255, 255, 255)
windowWidth = 400
windowHeight = 300

class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, angle, tank_indicator):
        super().__init__()
        print("Creating surface")
        self.image = pygame.Surface([5,5])
        self.image.fill(color)


        self.x = init_x
        self.y = init_y
        self.angle = angle
        self.tank_indicator = tank_indicator
        self.speed = randint(5, 15)

        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y


    def move(self):

        print("speed: " + str(self.speed))
        self.x += self.speed * np.cos(np.deg2rad(self.angle))
        self.y += self.speed * np.sin(np.deg2rad(self.angle))
        print("new x: ", self.x)
        print("new y: ", self.y)

        if self.x >= windowWidth:
            self.angle = 180
        if self.x <= 0:
            self.angle = 0
        if self.y >= windowHeight:
            self.angle = 270
        if self.y <= 0:
            self.angle = 90

        self.rect.x = self.x
        self.rect.y = self.y

'''pygame.init()

screen = pygame.display.set_mode((windowWidth, windowHeight))
done = False
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
bullet = Bullet(50, 50, 270, 0)
all_sprites_list.add(bullet)

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    all_sprites_list.update()
    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    for sprite in all_sprites_list:
        sprite.move()
    clock.tick(60)
    pygame.display.flip()'''

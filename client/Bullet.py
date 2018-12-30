import pygame 
from random import *
import math
from client.Settings import *
import client.util


class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, angle, tank_indicator):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(color)

        self.x = init_x
        self.y = init_y
        self.angle = angle
        self.tank_indicator = tank_indicator
        self.id = randint(100, 10000)
        self.speed = 10

        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.move()

    def move(self):
        angle_rad = self.angle*math.pi/180
        self.x += self.speed * math.cos(angle_rad)
        self.y -= self.speed * math.sin(angle_rad)

        if self.x >= windowWidth:
            self.angle = 180 - self.angle
        if self.x <= 0:
            self.angle *= -1
        if self.y >= windowHeight:
            self.angle = 270
        if self.y <= 0:
            self.angle = 90

        self.rect.x = self.x
        self.rect.y = self.y

        return not client.util.out_of_bounds(self.x, self.y)

    def to_json(self):
        bullet_json = {
            "type": "bullet",
            "id": self.id,
            "tank_id": self.tank_indicator,
            "angle": self.angle,
            "speed": self.speed,
            "rect x": self.rect.x,
            "rect y": self.rect.y
        }
        return bullet_json

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

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

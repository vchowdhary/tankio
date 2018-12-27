import pygame
import math
from Bullet import Bullet

color = (255, 255, 255)
windowWidth = 400
windowHeight = 300


class Tank(pygame.sprite.Sprite):
    # Constructor for tank, pass in position and state
    # state = 0 if not shooting, 1 if shooting
    def __init__(self, x, y, angle, id):
        super().__init__()

        self.image = pygame.Surface([x, y], pygame.SRCALPHA)
        self.image.fill(color)
        self.original = self.image
        self.orientation = angle
        self.x = x
        self.y = y
        self.id = id

        pygame.draw.rect(self.image, color, [x-20, y-30, x, y])

        self.rect = self.image.get_rect()
        self.bullets = []

    def move(self, pixels):
        self.rect.x += pixels*math.cos(self.orientation)
        self.rect.y += pixels*math.sin(self.orientation)

        if self.rect.x > windowWidth:
            self.rect.x = 0
        if self.rect.y > windowHeight:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = windowWidth
        if self.rect.y < 0:
            self.rect.y = windowHeight

        print("move called")

    def rotate(self, angle):
        center = self.rect.center
        self.orientation += angle
        print("Rotating", angle, self.orientation)
        self.image = pygame.transform.rotate(self.original, self.orientation)
        self.rect = self.image.get_rect(center=center)

    def shoot(self):
        return Bullet(self.x, self.y, self.orientation, self.id)




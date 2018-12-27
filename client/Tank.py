import pygame
import math

color = (255, 255, 255)
windowWidth = 400
windowHeight = 300

class Tank(pygame.sprite.Sprite):
    #Constructor for tank, pass in position and state
    #state = 0 if not shooting, 1 if shooting
    def __init__(self, x, y, angle):
        super().__init__()

        self.image = pygame.Surface([x, y])
        self.image.fill(color)
        self.angle = angle
        self.x = x
        self.y = y

        pygame.draw.rect(self.image, color, [x-20, y-30, x, y])

        self.rect = self.image.get_rect()

    def move(self, pixels):
        self.rect.x += pixels*math.cos(self.angle)
        self.rect.y += pixels*math.sin(self.angle)

        if self.rect.x > windowWidth:
            self.rect.x = 0
        if self.rect.y > windowHeight:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = windowWidth
        if self.rect.y < 0:
            self.rect.y = windowHeight

    def rotate(self, delta):
        new_img = pygame.transform.rotate(self.image, delta)

        self.rect = new_img.get_rect(center=self.rect.center)
        self.image = new_img

        '''x = self.rect.center[0]
        y = self.rect.center[1]

        pivotx = self.rect.x - x
        pivoty = self.rect.y - y

        newx = pivotx*math.cos(delta) - pivoty*math.sin(delta)
        newy = pivotx*math.sin(delta) + pivoty*math.cos(delta)
        self.rect.x = newx + x
        self.rect.y = newy + y'''





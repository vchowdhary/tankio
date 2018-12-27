import pygame
import math
from Tank import Tank

color = (255, 255, 255)
BLACK = (0, 0, 0)
windowWidth = 400
windowHeight = 300

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
done = False
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

tank1 = Tank(20, 30, 0, 0)
tank1.rect.x = 100
tank1.rect.y = 100


all_sprites_list.add(tank1)

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        tank1.move(10)
    if pressed[pygame.K_DOWN]:
        tank1.move(-10)
    if pressed[pygame.K_LEFT]:
        tank1.rotate(10)
    if pressed[pygame.K_RIGHT]:
        tank1.rotate(-10)
    if pressed[pygame.K_SPACE]:
        all_sprites_list.add(tank1.shoot())

    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()

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

tank1 = Tank(20, 30, 0)
tank1.rect.x = 100
tank1.rect.y = 100


all_sprites_list.add(tank1)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	all_sprites_list.update()
	tank1.rotate(90)

	screen.fill(BLACK)
	all_sprites_list.draw(screen)

	
	clock.tick(60)

	pygame.display.flip()

pygame.quit()
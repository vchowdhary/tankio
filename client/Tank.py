import pygame 
import math

color = (255, 0, 0)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, init_x, init_y, angle):
		super().__init__()
		self.image = pygame.Surface([windowWidth, windowHeight])
		self.init_x = init_x
		self.init_y = init_y

		pygame.draw.circle(self.image, color, (init_x, init_y), 10)
		self.rect = self.image.get_rect()
	def move(self):
		

pygame.init()
windowWidth = 400
windowHeight = 300
screen = pygame.display.set_mode((windowWidth, windowHeight))
done = False
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
bullet = Bullet(20, 30, 0)
all_sprites_list.add(bullet)

while not done: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	all_sprites_list.update()
	screen.fill((0, 0, 0))
	all_sprites_list.draw(screen)
	clock.tick(60)
	pygame.display.flip()
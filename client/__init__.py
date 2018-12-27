import pygame
import math

color = (255, 255, 255)
BLACK = (0, 0, 0)
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

		pygame.draw.rect(self.image, color, [x, y, x+20, y+30])
		
		self.rect = self.image.get_rect()

	def move(self, pixels):
		self.rect.x += pixels*math.cos(self.angle)
		self.rect.y += pixels*math.sin(self.angle)

		if(self.rect.x > windowWidth):
			self.rect.x = 0
		if(self.rect.y > windowHeight):
			self.rect.y = 0
		if(self.rect.x < 0):
			self.rect.x = 0
		if(self.rect.y < 0):
			self.rect.y = 0

	def rotate(self, delta):
		



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

	screen.fill(BLACK)
	all_sprites_list.draw(screen)

	
	clock.tick(60)

	pygame.display.flip()

pygame.quit()


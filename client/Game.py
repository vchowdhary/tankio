import pygame
import random
from threading import Thread
from client.Tank import Tank
from common.GameMessage import GameMessage

color = (255, 255, 255)
BLACK = (0, 0, 0)
windowWidth = 400
windowHeight = 300


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((windowWidth, windowHeight))
        self.done = False
        self.clock = pygame.time.Clock()

        self.all_sprites_list = pygame.sprite.Group()

        self.tank = Tank(20, 30, 0, 0)
        self.tank.set_position(random.randint(0, windowWidth), random.randint(0, windowHeight))

        self.all_sprites_list.add(self.tank)

        self.master_loop = Thread(target=self.loop)
        # self.master_loop.start()

    def start(self):
        self.master_loop.start()

    def loop(self):
        while not self.done:
            self.clock.tick(60)
            # print("running")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.tank.move(10)
            if pressed[pygame.K_DOWN]:
                self.tank.move(-10)
            if pressed[pygame.K_LEFT]:
                self.tank.rotate(10)
            if pressed[pygame.K_RIGHT]:
                self.tank.rotate(-10)
            if pressed[pygame.K_SPACE]:
                self.all_sprites_list.add(self.tank.shoot())

            self.all_sprites_list.update()
            self.screen.fill(BLACK)
            self.all_sprites_list.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def get_data(self):
        return GameMessage(self.tank, []).get()

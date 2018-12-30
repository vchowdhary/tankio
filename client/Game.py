import pygame
import random
from client.Tank import Tank
from client.Bullet import Bullet
from common.GameMessage import GameMessage

color = (255, 255, 255)
BLACK = (0, 0, 0)
windowWidth = 800
windowHeight = 800


class Game:
    def __init__(self):

        self.screen = pygame.display.set_mode((windowWidth, windowHeight))
        self.done = False
        self.clock = pygame.time.Clock()

        self.all_sprites_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        self.tank = Tank(20, 30, 0, random.randint(0, 100))
        self.tank.set_position(random.randint(0, windowWidth), random.randint(0, windowHeight))

        self.all_sprites_list.add(self.tank)

    def start(self):
        self.loop()

    def loop(self):
        while not self.done:
            try:
                self.clock.tick(60)
                # print("running")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        b = self.tank.shoot()
                        self.bullet_list.add(b)

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]:
                    self.tank.move(3)
                if pressed[pygame.K_DOWN]:
                    self.tank.move(-3)
                if pressed[pygame.K_LEFT]:
                    self.tank.rotate(5)
                if pressed[pygame.K_RIGHT]:
                    self.tank.rotate(-5)

                self.all_sprites_list.update()
                for bullet in self.bullet_list:
                    if bullet.move():
                        self.bullet_list.remove(bullet)

                self.tank.check_hit(self.bullet_list)

                self.screen.fill(BLACK)
                self.all_sprites_list.draw(self.screen)
                self.bullet_list.draw(self.screen)

                pygame.display.flip()
            except KeyboardInterrupt:
                self.done = True

        pygame.quit()

    def get_data(self):
        return GameMessage(self.tank, self.bullet_list).get()

    def update_game(self, msg):
        for ip in msg:
            for m in msg[ip]:
                if m["type"] == "tank":
                    self.update_tank(m)

    def update_tank(self, m):
        found = False
        for sprite in self.all_sprites_list:
            if sprite.id == m["id"]:
                sprite.set_position(m["rect x"], m["rect y"])
                sprite.rotate(m["orientation"] - sprite.orientation)
                found = True
        if not found:
            t = Tank(m["center x"], m["center y"], m["orientation"], m["id"])
            self.all_sprites_list.add(t)

    def update_bullets(self, m):
        found = False
        for sprite in self.bullet_list:
            if sprite.id == m["id"]:
                sprite.set_position(m["rect x"], m["rect y"])
                found = True
        if not found:
            t = Bullet(m["rect x"], m["rect y"], m["angle"], m["tank_id"])
            t.id = m["id"]
            t.speed = m["speed"]
            self.bullet_list.add(t)

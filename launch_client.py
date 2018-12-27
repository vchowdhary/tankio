from client.Client import Client
import pygame

pygame.init()

c = Client()
c.connect()
c.start()

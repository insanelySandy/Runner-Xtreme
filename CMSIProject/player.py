import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, walkspeed, jumpheight):
        self.walkspeed = walkspeed
        self.jumpheight = jumpheight
        self.position = (50,100)
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('Images', 'jumpor_sprite.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect()

    def right(self):
        self.position = (self.position[0] + self.walkspeed, self.position[1])
    def up(self):
        self.position = (self.position[0], self.position[1] - self.jumpheight)
    def down(self):
        self.position = (self.position[0], self.position[1] + self.jumpheight)
    def left(self):
        self.position = (self.position[0] - self.walkspeed, self.position[1])


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, walkspeed, image, spawn, distancetraveled):
        self.distancetraveled = distancetraveled
        self.walkspeed = walkspeed
        self.position = spawn
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('Images', image)).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = img.get_rect()

    def update(self):
        self.walk()
        self.distancetraveled = self.distancetraveled + self.walkspeed

    def walk(self):
        self.position = (self.position[0] - self.walkspeed, self.position[1])




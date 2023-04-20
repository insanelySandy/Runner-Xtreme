import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, walkspeed, jumpheight):
        self.walkspeed = walkspeed
        self.jumpheight = jumpheight
        self.position = (100,100)
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('Images', 'chris_pratt_cringe_tiny.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    
    def update(self):
        self.walk()
        print(self.position)

    def walk(self):
        self.position = (self.position[0] + self.walkspeed, self.position[1])
    def jump(self):
        self.position = (self.position[0], self.position[1] + self.jumpheight)
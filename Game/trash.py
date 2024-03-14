# Trash class 
import pygame
import random
class Trash(pygame.sprite.Sprite):
    def __init__(self, picturePath, x, y, width, height, value):
        super().__init__()
        ogImage = pygame.image.load("spriteSheets/trash1.png").convert_alpha()
        self.angle = random.randint(0, 360)
        self.image = pygame.transform.scale(ogImage, (width, height))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.value = value
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 1

    def update(self):
        self.rect.right -= self.vel
        if self.rect.right < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

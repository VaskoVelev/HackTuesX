import pygame
import random

class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, trashGroup):
        super().__init__()

        self.frameIndex = 0
        self.animationSpeed = 15
        self.frameCount = 0 
        self.desiredWidth = width
        self.desiredHeight = height
        self.trashGroup = trashGroup

        self.frames = []

        for i in range(1, 4):
            shark_image = pygame.image.load(f"spriteSheets/shark/blacksharkSS_{i}.png").convert_alpha()
            self.frames.append(shark_image)

        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
       
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screenWidth = 1400
        self.frameCount += 1
        if self.frameCount >= self.animationSpeed:
            self.frameCount = 0
            self.frameIndex += 1 
            if self.frameIndex >= len(self.frames):
                self.frameIndex = 0
            self.image = self.frames[self.frameIndex]
        if self.rect.right < -200:
            randomX = random.randrange(screenWidth+300, screenWidth * 2 )
            randomY = random.randrange(80, 420)
            self.rect.x = randomX
            self.rect.y = randomY
        else:
            self.rect.x -= 8
        trashCollide = pygame.sprite.spritecollide(self, self.trashGroup, False)
        for trash in trashCollide:
            trash.kill()
            

    def draw(self, surface):
        scaled_image = pygame.transform.scale(self.image, (self.desiredWidth, self.desiredHeight))
        surface.blit(scaled_image, self.rect)


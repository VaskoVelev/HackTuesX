import pygame
from bullets import Bullet

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, trashGroup, bulletGroup, bulletHitGroup, life, score):
        super().__init__()

        # Loading the sprite sheet img
        fishSS = pygame.image.load("spriteSheets/bluefishSS.jpg").convert_alpha()
        self.frameIndex = 0
        self.animationSpeed = 15
        self.frameCount = 0 
        self.desiredWidth = width
        self.desiredHeight = height
        self.trashGroup = trashGroup
        self.bulletGroup = bulletGroup
        self.bulletHitGroup = bulletHitGroup
        self.life = life
        self.score = score
        # List to store the individual frames of the animation

        self.frames = []

        # Obtain indivdual frames from the sheet
        frameWidth = 33
        frameHeight = 30
        numFrames = 3

        for i in range(numFrames):
            rect = pygame.Rect(i * frameWidth, 0, frameWidth, frameHeight)
            image = pygame.Surface(rect.size, pygame.SRCALPHA)
            image.blit(fishSS, (0, 0), rect)
            self.frames.append(image)

        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
        self.bulletDelay = 300
        self.bulletTimer = 0 
        # Set inital position
        self.rect.x = x
        self.rect.y = y

    def shoot(self):
        bullet = Bullet(self.rect.x + self.desiredWidth, self.rect.y + (self.desiredHeight // 2), 50, 50, self.trashGroup, self.bulletHitGroup, self)
        self.bulletGroup.add(bullet)
        

    def update(self):
        self.frameCount += 1
        if self.frameCount >= self.animationSpeed:
            self.frameCount = 0
            self.frameIndex += 1 
            if self.frameIndex >= len(self.frames):
                self.frameIndex = 0
            self.image = self.frames[self.frameIndex]
        

        trashCollide = pygame.sprite.spritecollide(self, self.trashGroup, False)
        for trash in trashCollide:
            self.life -= 1
            trash.kill()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.y != 64:
                self.rect.y -= 4
        if keys[pygame.K_s]:
            if self.rect.y != 588:
                self.rect.y += 4
        if keys[pygame.K_a]:
            if self.rect.x != 2:
                self.rect.x -= 4
        if keys[pygame.K_d]:
            if self.rect.x != 1202:
                self.rect.x += 4
        if keys[pygame.K_SPACE]:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.bulletTimer >= self.bulletDelay:
                self.shoot()
                self.bulletTimer = currentTime

    def draw(self, surface):
        scaledImage = pygame.transform.scale(self.image, (self.desiredWidth, self.desiredHeight))
        surface.blit(scaledImage, self.rect)
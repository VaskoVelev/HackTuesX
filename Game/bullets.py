import pygame
from bulletHit import BulletHit
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, trashGroup, bulletHitGroup, fish):
        super().__init__()

        self.images = []
        self.frameCount = 0
        self.frameIndex = 0
        self.animationSpeed = 7
        self.desiredHeight = 70
        self.desiredWidth = 70
        self.trashGroup = trashGroup
        self.bulletHitGroup = bulletHitGroup
        self.fish = fish
        self.loadAnimation()
        

        self.image = self.images[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def loadAnimation(self):
        numFrames = 6
        for i in range(1, numFrames+1):
            framePath = f'spriteSheets/playerShoot/ps{i}.png'
            frame = pygame.image.load(framePath).convert_alpha()
            frameScaled = pygame.transform.scale(frame, (self.desiredWidth, self.desiredHeight))
            self.images.append(frameScaled)
    
    def update(self):
        self.frameCount += 1
        if self.frameCount >= self.animationSpeed:
            self.frameCount = 0
            self.frameIndex += 1 
            if self.frameIndex >= len(self.images):
                self.frameIndex = 0
        self.image = self.images[self.frameIndex]
        self.rect.x += 8    
        trashBulletCollide = pygame.sprite.spritecollide(self, self.trashGroup, False)
        for trash in trashBulletCollide:
            self.fish.score += trash.value
            self.kill()
            trash.kill()
            bulletHit = BulletHit(trash.rect.centerx, trash.rect.centery, 30, 30)
            self.bulletHitGroup.add(bulletHit)
        if self.rect.left > 1440:
            self.kill()
    
    def draw(self, surface):

        surface.blit(self.image, self.rect)
import pygame
class BulletHit(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        super().__init__()
        self.images = []
        self.frameCount = 0
        self.frameIndex = 0
        self.animationSpeed = 10
        self.desiredWidth = 70
        self.desiredHeight = 70
        self.loadAnimation()

        self.image = self.images[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def loadAnimation(self):
        numFrames = 7
        for i in range(1, numFrames+1):
            framePath = f'Game/spriteSheets/playerHit/playerHit{i}.png'
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
                self.kill()
        self.image = self.images[self.frameIndex]
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
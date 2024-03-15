import pygame
from bullets import Bullet

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, trashGroup, bulletGroup, bulletHitGroup, life, score, boss_mode):
        super().__init__()

        self.frameIndex = 0
        self.animationSpeed = 10
        self.frameCount = 0 
        self.desiredWidth = width
        self.desiredHeight = height
        self.trashGroup = trashGroup
        self.boss_mode = boss_mode

        self.bulletGroup = bulletGroup
        self.bulletHitGroup = bulletHitGroup
        self.life = life
        self.score = score

        # Load frames for all directions
        self.frames_up = []
        self.frames_down = []
        self.frames_left = []
        self.frames_right = []

        for i in range(1, 4):
            fish_image = pygame.image.load(f"spriteSheets/fish/basic_fish/up/fish{i}.png").convert_alpha()
            self.frames_up.append(fish_image)

            fish_image = pygame.image.load(f"spriteSheets/fish/basic_fish/down/fish{i}.png").convert_alpha()
            self.frames_down.append(fish_image)

            fish_image = pygame.image.load(f"spriteSheets/fish/basic_fish/left/fish{i}.png").convert_alpha()
            self.frames_left.append(fish_image)

            fish_image = pygame.image.load(f"spriteSheets/fish/basic_fish/right/fish{i}.png").convert_alpha()
            self.frames_right.append(fish_image)

        self.image = self.frames_up[self.frameIndex]
        self.rect = self.image.get_rect()
        self.bulletDelay = 300
        self.bulletTimer = 0 
        self.rect.x = x
        self.rect.y = y
        self.direction = "up"  # Initial direction

    def shoot(self):
        bullet = Bullet(self.rect.x + self.desiredWidth, self.rect.y + (self.desiredHeight // 2), 50, 50, self.trashGroup, self.bulletHitGroup, self)
        self.bulletGroup.add(bullet)
        
    def update(self):
        self.frameCount += 1
        if self.frameCount >= self.animationSpeed:
            self.frameCount = 0
            self.frameIndex += 1 
            if self.frameIndex >= len(self.frames_up):
                self.frameIndex = 0

            # Update image based on direction
            if self.direction == "up":
                self.image = self.frames_up[self.frameIndex]
            elif self.direction == "down":
                self.image = self.frames_down[self.frameIndex]
            elif self.direction == "left":
                self.image = self.frames_left[self.frameIndex]
            elif self.direction == "right":
                self.image = self.frames_right[self.frameIndex]

        trashCollide = pygame.sprite.spritecollide(self, self.trashGroup, False)
        for trash in trashCollide:
            self.life -= 1
            trash.kill()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.y != 64:
                self.rect.y -= 4
                self.direction = "up"
        if keys[pygame.K_s]:
            if self.rect.y != 588:
                self.rect.y += 4
                self.direction = "down"
        if keys[pygame.K_a]:
            if self.rect.x != 2:
                self.rect.x -= 4
                self.direction = "left"
        if keys[pygame.K_d]:
            if self.rect.x != 1202:
                self.rect.x += 4
                self.direction = "right"
        if keys[pygame.K_SPACE]:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.bulletTimer >= self.bulletDelay:
                self.shoot()
                self.bulletTimer = currentTime

    def draw(self, surface):
        scaledImage = pygame.transform.scale(self.image, (self.desiredWidth, self.desiredHeight))
        surface.blit(scaledImage, self.rect)

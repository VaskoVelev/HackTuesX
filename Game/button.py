import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, gameState):
        super().__init__()

        self.images = {
            'normal': pygame.image.load('Game/spriteSheets/button/blueButton.png'),
            'hover': pygame.image.load('Game/spriteSheets/button/blueButtonHover.png'),
            'pressed': pygame.image.load('Game/spriteSheets/button/blueButtonPressed.png')
        }
        self.state = 'normal'
        self.image = self.images[self.state]
        self.rect = self.image.get_rect()
        self.desiredWidth = width
        self.desiredHeight = height
        self.rect.center = (x, y)
        self.text = text
        self.font = pygame.font.Font('Game/font/Pixeltype.ttf', 50)
        self.collisionRect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.gameState = gameState

    def handleHover(self, mousePOS):
        if self.collisionRect.collidepoint(mousePOS):
            self.state = 'hover' 
        else:
            self.handleDefault()
        self.image = self.images[self.state]

    def handleClick(self,  mousePOS):
        if self.collisionRect.collidepoint(mousePOS):
            self.state = 'pressed'
            self.image = self.images[self.state]

            if self.text == 'Start':
                self.gameState = 'running'

            if self.text == 'Quit':
                pygame.quit()
                exit()

    def handleDefault(self):
        self.state = 'normal'
        self.image = self.images[self.state]

    def draw(self, surface):
        scaledImage = pygame.transform.scale(self.image, (self.desiredWidth, self.desiredHeight))
        image_rect = scaledImage.get_rect(center=self.rect.center)
        surface.blit(scaledImage, image_rect)
        
        textSurface = self.font.render(self.text, True, (255, 255, 255))
        textRect = textSurface.get_rect(center=self.rect.center)
        surface.blit(textSurface, textRect)

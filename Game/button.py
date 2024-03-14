import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, gameState):
        super().__init__()

        self.images = {
            'normal': pygame.image.load('spriteSheets/button/blueButton.png'),
            'hover': pygame.image.load('spriteSheets/button/blueButtonHover.png'),
            'pressed': pygame.image.load('spriteSheets/button/blueButtonPressed.png')
        }
        self.state = 'normal'
        self.image = self.images[self.state]
        self.rect = self.image.get_rect()
        self.desiredWidth = width
        self.desiredHeight = height
        self.rect.center = (x, y)
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        self.collisionRect = pygame.Rect(x, y, width, height)
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
        surface.blit(scaledImage, self.rect)
        textSurface = self.font.render(self.text, True, (255, 255, 255))
        textRect = textSurface.get_rect(center=self.rect.center)
        textRect.y += (self.desiredHeight - textRect.height) // 2
        textRect.x += (self.desiredWidth - 125) // 2
        surface.blit(textSurface, textRect)
import pygame

class Fighter():  
    def __init__(self, x, y):  
        self.rect = pygame.Rect((x, y, 80, 280))  
        self.SPEED = 10 
    
    def draw(self, surface): 
        pygame.draw.rect(surface, (255, 0, 0), self.rect) 

    def move(self): 
        dx = 0 
        dy = 0

        #get key pressed
        key = pygame.key.get_pressed() 

        #movement
        if(key[pygame.K_a] and self.rect.left - self.SPEED > 0):
            dx = dx-self.SPEED 

        if(key[pygame.K_d] and self.rect.right + self.SPEED < 1000): 
            dx = dy + self.SPEED   
        
        
        #update player position 
        self.rect.x += dx 
        self.rect.y += dy
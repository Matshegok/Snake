import random
class Apple:
    def __init__(self, image, display): 
        self.image = image
        self.display = display
        self.x = 250
        self.y = 250
        self.image_rect = self.image.get_rect(center =(self.x, self.y))
    
    #creating random coordinates for the apple
    def Randomise(self):
        self.x =  random.randint(0, 15)
        self.y = random.randint(0, 15)
      
    #drawing the apple  
    def drawApple(self): 
        self.image_rect = self.image.get_rect(topleft =(self.x*32, self.y*32))
        self.display.blit(self.image, self.image_rect)
        
    def get_apple_rect(self):
        return self.image_rect
    
    
        
            
        
        
        
        
        
        
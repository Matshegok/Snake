from pygame.math import Vector2
import pygame
import copy
class Player:

    def __init__(self, head_img, body_img, display):
        self.head_img = head_img
        self.body_img = body_img
        self.display = display
        self.head_rect = head_img.get_rect()
        self.body_rect = body_img.get_rect()
        self.whole_player = [Vector2(1,1), Vector2(2,1), Vector2(3,1)]
    
    def draw(self):
        
        self.head_rect.topleft = (self.whole_player[0].x * 32, self.whole_player[0].y * 32)
        self.display.blit(self.head_img, self.head_rect) 
        
        for body_parts in self.whole_player[1:]: 
            self.body_rect.topleft = (body_parts.x * 32, body_parts.y * 32)
            self.display.blit(self.body_img, self.body_rect)  
    #moving down 
    def move_down(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].y += 1
        for i in range(1,3): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
            
    #moving up
    def move_up(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].y -= 1
        for i in range(1,3): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        
    #moving left
    def move_left(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].x -= 1
        for i in range(1,3): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
    
    #moving right
    def move_right(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].x += 1
        for i in range(1,3): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        
    def collision(self, score_rect): 
        if self.head_rect.colliderect(score_rect):
            return True
        else:
            return False
        
    def get_head_rect(self):
        return self.head_rect
            
        
        
        
        
    
        
        
        
        
        
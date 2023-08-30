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
        self.whole_player = [Vector2(1,1)]
        self.head_direction = None; 
    
    
    #drawing snake
    def draw(self):
        #drawing the hea
        self.head_rect.topleft = (self.whole_player[0].x * 32, self.whole_player[0].y * 32)
        self.display.blit(self.head_img, self.head_rect) 
        for body_parts in self.whole_player[1:]: 
            self.body_rect.topleft = (body_parts.x * 32, body_parts.y * 32)
            self.display.blit(self.body_img, self.body_rect)  
    #moving down 
    def move_down(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].y += 1       
        for i in range(1,len(self.whole_player)): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        self.head_direction = "down"
    #moving up
    def move_up(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].y -= 1
        for i in range(1,len(self.whole_player)): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        self.head_direction = "up"
        
    #moving left
    def move_left(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].x -= 1
        for i in range(1,len(self.whole_player)): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        self.head_direction = "left"
    
    #moving right
    def move_right(self): 
        self.whole_player_copy = copy.deepcopy(self.whole_player)
        self.whole_player_copy[0].x += 1
        for i in range(1,len(self.whole_player)): 
            self.whole_player_copy[i] = self.whole_player[i-1] 
        self.whole_player = self.whole_player_copy
        self.head_direction = "right"
        
    def addBody(self): 
        self.whole_player.append(Vector2(2,2))
        
    def collision(self, score_rect): 
        if self.head_rect.colliderect(score_rect):
            return True
        else:
            return False
        
    def get_head_rect(self):
        return self.head_rect
    
    
    def getBody(self):
        return self.whole_player
    
    def rot_center(image, angle, x, y):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
        return rotated_image, new_rect
    
    def head_rotate(self): 
        if self.head_direction == "down": 
            player_down, player_down_rect = self.rot_center(self.head_img, 0, self.head_rect.centerx, self.head_rect.centery)
        if self.head_direction == "right": 
            player_down, player_down_rect = self.rot_center(self.head_img, 90, self.head_rect.centerx, self.head_rect.centery)
        if self.head_direction == "up": 
            player_down, player_down_rect = self.rot_center(self.head_img, 180, self.head_rect.centerx, self.head_rect.centery)
        if self.head_direction == "left": 
            player_down, player_down_rect = self.rot_center(self.head_img, 270, self.head_rect.centerx, self.head_rect.centery)

        self.head_img = player_down
        self.head_rect = player_down_rect
    
    def addNewTail(self): 
        # #When the tail is just the head.
        if (len(self.whole_player)):
            if (self.head_direction == "up"):
                self.whole_player.append(Vector2(self.whole_player[0].x, self.whole_player[0].y + 1))
            if (self.head_direction == "down"):
                self.whole_player.append(Vector2(self.whole_player[0].x, self.whole_player[0].y - 1))
            if (self.head_direction == "right"):
                self.whole_player.append(Vector2(self.whole_player[0].x-1, self.whole_player[0].y))
            if (self.head_direction == "left"): 
                self.whole_player.append(Vector2(self.whole_player[0].x+1, self.whole_player[0].y))
        
        
        
            
        
        
        
        
    
        
        
        
        
        
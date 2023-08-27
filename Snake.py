import pygame
from player import Player
from apple import Apple
pygame.init()

display = pygame.display.set_mode((480,480))
pygame.display.set_caption("SkyCraft")
clock = pygame.time.Clock()

#Importing the snake head and body
head = pygame.image.load("Graphics/Head_3.png")
body = pygame.image.load("Graphics/body_2.png")
snake = Player(head, body, display)

#loading the background 
bg = pygame.image.load("Graphics/bg.png")


#apple
apple_image = pygame.image.load("Graphics/apple.png")
apple = Apple(apple_image, display)
apple.Randomise()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        
        if event.type == pygame.KEYDOWN:
            print(snake.collision(apple.get_apple_rect()))     
            print(apple.get_apple_rect())
            print(snake.get_head_rect())
            if event.key == pygame.K_DOWN:
                snake.move_down()
            if event.key == pygame.K_RIGHT:
                snake.move_right()
            if event.key == pygame.K_LEFT:
                snake.move_left()
            if event.key == pygame.K_UP:
                snake.move_up() 
               
    keys = pygame.key.get_pressed()
    display.blit(bg, (0,0))
    apple.drawApple()
    snake.draw()
    pygame.display.flip()
    clock.tick(60)
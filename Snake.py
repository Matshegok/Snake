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
            if event.key == pygame.K_DOWN:
                snake.move_down()
                print("down")
                print(snake.getBody())  
            if event.key == pygame.K_RIGHT:
                snake.move_right()
                print("right")
                print(snake.getBody())
            if event.key == pygame.K_LEFT:
                snake.move_left()
                print("left")
                print(snake.getBody())
            if event.key == pygame.K_UP:
                snake.move_up() 
                print("up")
                print(snake.getBody())
            if event.key == pygame.K_a:
                snake.addNewTail()
               
    keys = pygame.key.get_pressed()
    display.blit(bg, (0,0))
    apple.drawApple()
    snake.draw()
    pygame.display.flip()
    clock.tick(60)
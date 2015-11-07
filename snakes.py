#this is the snake game 

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (163,235,253)
red  = (255,0,0)
green = (0,155,0)

display_width  = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))  #surface object
pygame.display.set_caption('Snakes')                                   #name of the game

clock = pygame.time.Clock()                                             #clock object controls FPS
block_size = 20
FPS = 10  # define frames per second --- try not to modify this very often as it can put a lot of pressure on the processor

font  = pygame.font.SysFont(None, 20)

def snake(block_size,snakelist):
      for XnY in snakelist :        #list of lists
          pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])
      
def text_objects(text,color):
      textSurface  = font.render(text,True,color)
      return textSurface, textSurface.get_rect()

def message_to_screen(msg,color):               #display message msg to the screen

      
    textSurf,textRect= text_objects(msg,color)
##    screen_text = font.render(msg,True,color)
##    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(textSurf,textRect)


    
def gameLoop():                                #this is where the logic of the game is written. 
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10

    snakeList =[]
    snakeLength =  1
    while not gameExit :
        while gameOver ==True :                 #the main loop 
            gameDisplay.fill(white)
            message_to_screen("Game Over! Press C to play again or Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                      gameOver = False
                      gameExit = True
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     lead_x_change = -block_size
                     lead_y_change = 0
                 elif event.key == pygame.K_RIGHT:
                     lead_x_change= block_size
                     lead_y_change = 0

                 elif event.key == pygame.K_UP:
                     lead_y_change = -block_size
                     lead_x_change = 0
                 elif event.key == pygame.K_DOWN:
                     lead_y_change= block_size
                     lead_x_change = 0

            '''
            this can be used when you want the object to stop when you stop pressing the left / right  key 
             if event.type == pygame.KEYUP:    
                if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0

            '''
        if lead_x >=display_width or lead_x < 0 or lead_y >=display_height or lead_y<0:
            gameOver = True
                
        lead_x += lead_x_change
        lead_y += lead_y_change
        
                 
        
        gameDisplay.fill(blue)   # background color is blue
        AppleThickness = 30
        pygame.draw.rect(gameDisplay,red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
    
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        

        if len(snakeList) > snakeLength :  #snakes length should stay constant till it eats another apple
            del snakeList[0]

        for eachSegment in snakeList[:-1]:   # checking if the snake has hit itself
            if eachSegment == snakeHead :
                gameOver=True

        snake(block_size,snakeList)
        
        pygame.display.update()
##     
##        if lead_x >= randAppleX and lead_x<= randAppleX+AppleThickness:
##            if lead_y >= randAppleY and lead_y<= randAppleY+AppleThickness:
##                randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10
##                randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10
##                snakeLength+=1

        
        if lead_x > randAppleX and lead_x < randAppleX  + AppleThickness or lead_x+ block_size>randAppleX and lead_x + block_size <randAppleX + AppleThickness:
           if lead_y > randAppleY and lead_y < randAppleY  + AppleThickness or lead_y+ block_size>randAppleY and lead_y + block_size <randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10
                randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10
                snakeLength+=1   
         
              

        clock.tick(FPS) 
        
        
    pygame.quit()
    quit()
gameLoop()

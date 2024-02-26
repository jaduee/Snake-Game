import pygame, sys, random, time
from pygame.locals import *

pygame.init()

#define color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (105,105,105)

# define window surface
WIDTH = 800
HEIGHT = 800
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
textArea = pygame.draw.rect(windowSurface,GRAY,pygame.Rect(0,0,800,80))
pygame.display.set_caption('Snake Game')

# control game speed
gameSpeed = pygame.time.Clock()

snakeHead = [100,100]
snakeBody = [[80,100],[60,100],[40,100], [20,100]]
foodPosition = [300,300]
foodEat = 1
score = 0

direction = 'right'
directionChange = direction

def drawSnake(snakeBody, snakeHead):
    #print("draw snake")
    #pygame.draw.rect(windowSurface,BLUE,Rect(snakeHead[0],snakeHead[1],20,20))
    for i in snakeBody:
        pygame.draw.rect(windowSurface,WHITE,Rect(i[0],i[1],20,20))

def drawFood(foodPosition):
    pygame.draw.rect(windowSurface,BLUE,Rect(foodPosition[0],foodPosition[1],20,20))




def gameover():
    windowSurface.fill(BLACK)
    font = pygame.font.SysFont(None, 38)
    text = font.render("Game is over. Do you want to play again(Y/N)?", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    windowSurface.blit(text, text_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_y:
                    game()
                elif event.key == K_n or event.type == QUIT:
                    pygame.quit()
                    sys.exit()

def game():
    # control game speed
    gameSpeed = pygame.time.Clock()
  

    snakeHead = [100,100]
    snakeBody = [[80,100],[60,100],[40,100], [20,100]]
    foodPosition = [300,300]
    foodEat = 1
    score = 0
    

    direction = 'right'
    directionChange = direction
    #direction = ''
    #directionChange = direction
    windowSurface.fill(BLACK)
    
    while True:
        windowSurface.fill(BLACK)
        drawSnake(snakeBody, snakeHead)
        drawFood(foodPosition)
        textArea = pygame.draw.rect(windowSurface,GRAY,pygame.Rect(0,0,800,80))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    directionChange = 'right'
                if event.key == K_LEFT or event.key == K_a:
                    directionChange = 'left'
                if event.key == K_UP or event.key == K_w:
                    directionChange = 'up'
                if event.key == K_DOWN or event.key == K_s:
                    directionChange = 'down'
                if event.key == KSCAN_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if directionChange == 'right' and not direction == 'left':
            direction = directionChange
        if directionChange == 'left' and not direction == 'right':
            direction = directionChange
        if directionChange == 'up' and not direction == 'down':
            direction = directionChange
        if directionChange == 'down' and not direction == 'up':
            direction = directionChange

        
        if direction == 'right':
            #tmpheadx = snakeHead[0]
            #tmpheady = snakeHead[1]
            snakeHead[0] += 20
            #for i in snakeBody:
        if direction == 'left':
            snakeHead[0] -= 20
        if direction == 'up':
            snakeHead[1] -= 20
        if direction == 'down':
            snakeHead[1] += 20

        #print((snakeHead[0], snakeHead[1]))
        
        snakeBody.insert(0,list(snakeHead))
        

        if snakeHead[0] == foodPosition[0] and snakeHead[1] == foodPosition[1]:
            foodEat = 0
            score += 1
            print(score)
            
            #snakeBody.insert(0,list(snakeHead))
        else:
            snakeBody.pop()
        
        if foodEat == 0:
            x = random.randrange(1,32)
            y = random.randrange(5,32)
            foodPosition = [int(x * 20),int(y * 20)]
            foodEat = 1

    


        if snakeHead[0] > 800 or snakeHead[0] < 0:
            #print("1")
            gameover()
        elif snakeHead[1] > 800 or snakeHead[1] < 80:
            #print("2")
            gameover()
        for body in snakeBody[1:]:
            #print((body[0], body[1]))
            if (snakeHead[0] == body[0]) and (snakeHead[1] == body[1]):
                print(3)
                gameover()

               #pygame.display.update()
        #speedChange(gameSpeed, windowSurface)
        if 0 <= len(snakeBody) - 2 < 6:
            gameSpeed.tick(5)
            font = pygame.font.SysFont(None, 38)
            text = font.render("Level 1", True, WHITE)
            text_rect = text.get_rect(topleft=(20, 20))
            windowSurface.blit(text, text_rect)
            textScore = "Score: "+ str(score)
            text2 = font.render(textScore, True, WHITE)
            text2_rect = text2.get_rect(topright=(600, 20))
            windowSurface.blit(text2, text2_rect)
            
            pygame.display.flip()
        if 6 <= len(snakeBody) - 2 < 16:
            gameSpeed.tick(10)
            font = pygame.font.SysFont(None, 38)
            text = font.render("Level 2", True, WHITE)
            text_rect = text.get_rect(topleft=(20, 20))
            windowSurface.blit(text, text_rect)
            pygame.display.flip()
        if 15 <= len(snakeBody) - 2 < 50:
            gameSpeed.tick(20)
            font = pygame.font.SysFont(None, 38)
            text = font.render("Level 3", True, WHITE)
            text_rect = text.get_rect(topleft=(20, 20))
            windowSurface.blit(text, text_rect)
            pygame.display.flip()
        if 50 <= len(snakeBody) -2:
            gameSpeed = len(snakeBody)//1.5
            font = pygame.font.SysFont(None, 38)
            text = font.render("Level 4", True, WHITE)
            text_rect = text.get_rect(topleft=(20, 20))
            windowSurface.blit(text, text_rect)
            pygame.display.flip()

game()

        



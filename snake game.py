import pygame
import random

pygame.init()
x = 0
y = 0
width = 800
height = 500
red = 255,0,0
white = 255,255,255
black = 0,0,0
moveX = 0
moveY = 0
penguin = pygame.image.load("penguin.png")
screen = pygame.display.set_mode((width,height))
random_x = random.randrange(0,width-50)
random_y = random.randrange(0,height-50)

snakelist = []
snakelenght = 1
clock = pygame.time.Clock()
FPS = 90
#sound_1 = pygame.mixer.Sound('game_over.wav')
#sound_2 = pygame.mixer.Sound('point.wav')
def snake(snakelist):
    for i in range (len(snakelist)):
        pygame.draw.rect(screen,black,[snakelist[i][0],snakelist[i][1],50,50])
def GameOver():
    font = pygame.font.SysFont(None, 80)
    text = font.render("GamOver", True, black)
    screen.blit (text,(200,200))
def Score(counter):
    font = pygame.font.SysFont(None, 50)
    text = font.render("score = " + str(counter),True, white)
    screen.blit(text,(30,20))
counter = 0
game = True
while game:

    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 2
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -2
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 2
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -2
                moveX = 0
                
    screen.fill(red)
    #rect_1 = pygame.draw.rect(screen,black,[x,y,50,50])
    #rect_2 = pygame.draw.rect(screen,black,[random_x,random_y,50,50])
    rect_1 = pygame.Rect(x,y,50,50)
    rect_2 = pygame.Rect(random_x,random_y,70,70)
    screen.blit(penguin, (random_x,random_y))
    x += moveX
    y += moveY
    snakehead = []
    snakehead.append(x)
    snakehead.append(y)

    snakelist.append(snakehead)
    if len (snakelist)  > snakelenght:
        del snakelist[0]

    snake(snakelist)
    Score(counter)
    if rect_1.colliderect(rect_2):
        random_x = random.randrange(0,width-50)
        random_y = random.randrange(0,height-50)
        snakelenght += 5
        counter += 1
        #sound_2.play()
    for each in snakelist[:-1]:
        if snakelist[-1] == each:
            #print("Game Over")
            #sound_1.play()
            GameOver()
            game = False
        if x > width :
           x = -50
        elif y > height :
            y = -50
        elif x < -50:
           x = width
        elif y < -50:
           y = height
           
    pygame.display.update()
    clock.tick(FPS)
    

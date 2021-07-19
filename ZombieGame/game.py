import pygame
import random
pygame.init()

width = 1000
height = 500
black = 255,255,255

zombielist = []


screen = pygame.display.set_mode((width,height))

bg_img= pygame.image.load("images/background.png")

sound_2 = pygame.mixer.Sound('shot.wav')

for i in range(5):
    zombie = pygame.image.load("images/zombie_{}.png".format(i+1))
    zombielist.append(zombie)

zombieImage = random.choice(zombielist)
zombieheight = zombieImage.get_height()
zombiewidth = zombieImage.get_width()

random_x = random.randrange(0,width-zombiewidth)
random_y = random.randrange(0,height-zombieheight)

def Score(counter):
    font = pygame.font.SysFont(None, 30)
    text = font.render("score = "+str (counter),True, white)
    screen.blit(text,(10,10))

counter = 0
game = True

gun_aim = pygame.image.load("images/aim_pointer.png")

gun_image = pygame.image.load("images/gun_1.png")
gun_y = height - 200

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_1.colliderect(rect_2):
                zombieImage = random.choice(zombielist)
                random_x = random.randrange(0, width - zombiewidth)
                random_y = random.randrange(0, height - zombieheight)
                counter+=1
                sound_2.play()

    pos_x,pos_y = pygame.mouse.get_pos()
    screen.blit(bg_img,(0,0))
    screen.blit(zombieImage,(random_x,random_y))
    screen.blit(gun_aim,(pos_x-gun_aim.get_width()/2,pos_y-gun_aim.get_height()/2))
    screen.blit(gun_image,(pos_x,pos_y))

    rect_1 = pygame.Rect(pos_x,pos_y,gun_aim.get_width(),gun_aim.get_height())
    rect_2 = pygame.Rect(random_x,random_y,zombieImage.get_width(),zombieImage.get_height())


    pygame.display.update()

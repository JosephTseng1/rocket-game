import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 1000

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

darkblue = (0,0,139)
yellow = (177,244,7)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rocket Game')
clock = pygame.time.Clock()

rocketImg = pygame.image.load('rocket.png')
rocketwidth = 168
fireballImg = pygame.image.load('fireball.png')
bulletImg = pygame.image.load('bullet.png')
pause = False

def fireballs_dodged(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
    
def rocket(x,y):
    gameDisplay.blit(rocketImg,(x,y))

def message_display(text):
    font = pygame.font.Font('freesansbold.ttf', 115)
    gameDisplay.blit(font.render(text, True, (0,0,0)), (0,0))
    pygame.display.update()
    time.sleep(2)
    pygame.event.clear()
    game_loop()
   
def fireballs(firex, firey, firew, fireh):
    gameDisplay.blit(fireballImg,(firex, firey, firew, fireh))

def bullets(bulletx, bullety, bulletw, bulleth):
    gameDisplay.blit(bulletImg, (bulletx, bullety, bulletw, bulleth))
    
def crash():
   
    font = pygame.font.Font('freesansbold.ttf', 60)
    gameDisplay.blit(font.render("Game Over", True, (0,0,0)), (300,350))
    
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

       # gameDisplay.fill(white)
        

        button("Play Again",100,650,140,50,green,bright_green,game_loop)
        button("Quit",500,650,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
    pygame.event.clear()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    font = pygame.font.Font('freesansbold.ttf', 20)
    gameDisplay.blit(font.render(msg, True, (0,0,0)), (x-30+(w/2),y-6+(h/2)))
   
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
def paused():
    font = pygame.font.Font('freesansbold.ttf', 60)
    gameDisplay.blit(font.render("Paused", True, (0,0,0)), (300,350))
    
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

       # gameDisplay.fill(white)
        

        button("Continue",100,650,140,50,green,bright_green,unpause)
        button("Quit",500,650,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

    
def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        gameDisplay.fill(white)
        font = pygame.font.Font('freesansbold.ttf', 60)
        gameDisplay.blit(font.render("ROCKET GAME", True, (0,0,0)), (150,350))

        button("START",150,650,100,50,green,bright_green,game_loop)
        button("Quit",500,650,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)


        
def game_loop():
    global pause
    x = (display_width * 0.4)
    y = (display_height * 0.5)
    indicator = False
    
    x_change = 0

    fire_startx = random.randrange(-80, display_width-50)
    fire_starty = -600
    fire_speed = 7
    fire_width = 100
    fire_height = 100
    bullet_speed = -7
    bullet_x = x
    bullet_y = y
    
    dodged = 0
    gameExit = False

    while not gameExit:
        gameDisplay.fill(darkblue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -5
                if event.key == pygame.K_RIGHT:
                    x_change += 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_SPACE:
                    indicator = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change += 5
                if event.key == pygame.K_RIGHT:
                    x_change += -5
                
        x += x_change

        #gameDisplay.fill(darkblue)

        fireballs(fire_startx, fire_starty, fire_width, fire_height)
        fire_starty += fire_speed
        
        if indicator == True:
            bullets(bullet_x, bullet_y, 10, 10)
            bullet_y += bullet_speed
            
            
        rocket(x,y)
        fireballs_dodged(dodged)

        if bullet_y < -200:
            bullet_x = x
            bullet_y = y
            indicator = False
        if x > display_width - 50 or x < -80:
            crash()
            pygame.event.clear()

        if fire_starty > display_height:
            fire_starty = 0 - fire_height
            fire_startx = random.randrange(-80, display_width-50)
            dodged += 1
            if dodged % 10 == 0:
                fire_speed += 0.5
        
            fire_width += (dodged * 1.2)
        #Penis
        if bullet_y < fire_starty+fire_height+100 and bullet_y > fire_starty-100:
            if bullet_x + rocketwidth > fire_startx + 120 and bullet_x < fire_startx + 220:
                fire_starty = 800
                fire_startx = 1000
        
        #Penis
        if y < fire_starty+fire_height+100 and y > fire_starty-100:
            if x + rocketwidth > fire_startx + 120 and x < fire_startx + 220:
                crash()
                pygame.event.clear()
        
            
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()


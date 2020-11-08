# import modules
import pygame
import time
import random

# start pygame module
pygame.init()

# width and height of game display
display_width = 600
display_height = 400

# define the Display of Game
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race Car')
clock = pygame.time.Clock()

#variables

# define colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)
red = (255, 0, 0)
bright_red = (150, 0, 0)
green = (0, 255, 0)
bright_green = (0, 150, 0)


# load image as car in game
carImg = pygame.image.load('Car.png')
car_width = 48

def intro_game():
    intro = True
    while intro:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Let's play", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("play", 100, 300, 100, 40, bright_green, green,"play")
        button("quit", 400, 300, 100, 40, bright_red, red, "quit")
        pygame.display.update()





def button (text, x, y, width, height, active_color, inactive_color, action = None):
    mouse = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))


    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(TextSurf, TextRect)

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score : "+str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def  stuff(stuffx, stuffy, stuffw, stuffh, color):
    pygame.draw.rect(gameDisplay, color, [stuffx, stuffy, stuffw, stuffh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects (text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash ():
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects("You crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Try again", 100, 300, 100, 40, bright_green, green, "play")
        button("quit", 400, 300, 100, 40, bright_red, red, "quit")
        pygame.display.update()


gameExit = False
# Game loop
def game_loop ():
    # variables
    # location of car image in display
    x = (display_width * 0.45)
    y = (display_height * 0.88)
    X_change = 0
    stuff_startx = random.randrange(0, display_width)
    stuff_starty = -600
    stuff_speed = 10
    stuff_width = 80
    stuff_height = 50
    counter = 0


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# control of car (left and right)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_change = -10
                elif event.key == pygame.K_RIGHT:
                    X_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    X_change = 0
        x += X_change
        gameDisplay.fill(gray)
# recall stuff function
# stuffx, stuffy, stuffw, stuffh, color
        stuff(stuff_startx, stuff_starty, stuff_width, stuff_height, red)
        stuff_starty += stuff_speed
        car(x, y)
        score(counter)
        if x > display_width:
            x = 0
        elif x < -(car_width):
            x = display_width - car_width

        if stuff_starty > display_height:
            stuff_starty = -stuff_height
            stuff_startx = random.randrange(0, display_width)
            counter +=1
            if counter % 10 == 0:
                stuff_speed +=3


        if stuff_starty + stuff_height > y:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                crash()


        pygame.display.update()
        clock.tick(60)


intro_game()
game_loop()
pygame.quit()
quit()









# Import Required Modules
import pygame
import time
import random

# Initilize Pygame
pygame.init()

# Create variables for colors
yellow = (255, 255, 102)
black =(0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Create variable for background image
background = pygame.image.load('background.jpg')

# Create variables for game width and height
game_width = 1000
game_height = 600

# Set up game screen
Display = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Snake Game')
background = pygame.transform.scale(background, (game_width, game_height))

# Create variable for time
clock = pygame.time.Clock()

# Create variables for snake block and snake speed
Snake_Block = 10
Snake_Speed = 15

# Create variables for fonts
msg_font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to show score
def ShowScore(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    Display.blit(value, [0, 0])

# Function for our snake
def OurSnake(Snake_Block, Snake_List):
    for x in Snake_List:
        pygame.draw.rect(Display, green, [x[0], x[1], Snake_Block, Snake_Block])

# Function to show Message when game over
def Message(msg, color):
    mesg = msg_font.render(msg, True, color)
    Display.blit(mesg, [game_width / 6, game_height / 3])

# Function for game loop
def GameLoop():
    game_over = False
    game_close = False
 
    x1 = game_width / 2
    y1 = game_height / 2
 
    new_x1 = 0
    new_y1 = 0
 
    Snake_List = []
    Length_of_snake = 1

    # location of food
    foodx = round(random.randrange(0, game_width - Snake_Block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_height - Snake_Block) / 10.0) * 10.0
 
    while not game_close:
 
        while game_over == True:
            Display.blit(background, (0, 0))
            Message("You Lost! Press C-Play Again or Q-Quit", red)
            ShowScore(Length_of_snake - 1)
            pygame.display.update()

            # Set up commands to quit and restart game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        GameLoop()
        
        # Set up controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -Snake_Block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = Snake_Block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -Snake_Block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = Snake_Block
                    new_x1 = 0
                    
        # Set up conditions to game over
        if x1 >= game_width or x1 < 0 or y1 >= game_height or y1 < 0:
            game_over = True
            
        x1 += new_x1
        y1 += new_y1
        Display.blit(background, (0, 0))
        pygame.draw.rect(Display, red, [foodx, foody, Snake_Block, Snake_Block]) # Set up color to food
        Snake_Head = []
        Snake_Head.append(x1)
        Snake_Head.append(y1)
        Snake_List.append(Snake_Head)
        if len(Snake_List) > Length_of_snake:
            del Snake_List[0]
 
        for x in Snake_List[:-1]:
            if x == Snake_Head:
                game_close = True
 
        OurSnake(Snake_Block, Snake_List)
        ShowScore(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            # Changing food location
            foodx = round(random.randrange(0, game_width - Snake_Block) / 10.0) * 10.0
            foody = round(random.randrange(0, game_height - Snake_Block) / 10.0) * 10.0
            Length_of_snake += 1 # Increase lenght of snake when it eats food

        # Set up speed
        clock.tick(Snake_Speed)
        
    # Quit the program    
    pygame.quit()
    quit()
  
GameLoop()

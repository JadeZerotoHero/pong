# Learning pygame with Pong
# youtube.com/watch?v=Qf3-aDXG8q4

#To make a game in pygame, you need to do the following:
#1. Set up the main window
#2. Set up the main game loop
#3. Handle events
#4. Add game logic
#5. Add visuals
#6. Update the window

import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Vertical and Horizontal to reverse the speed for them separately
    if ball.top <= 0 or ball.bottom >= screen_height: #checks if the ball has gone off the screen
        ball_speed_y *= -1 # to reverse speed
    
    # Collision with the paddles
    if ball.colliderect(player) or ball.colliderect(opponent): #checks if the ball collides with the player or the opponent
        ball_speed_x *= -1 # to reverse speed

    # Scoring
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks() # Timer
        ball_start()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks() # Timer
        ball_start()

    # Timer
    if score_time:
        if pygame.time.get_ticks() - score_time < 1000:
            ball_start()
        else:
            score_time = None


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# General Setup
pygame.init() #initializes all the pygame modules
clock = pygame.time.Clock() #creates a clock object to track time

#Setting up the main window for the game
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height)) #creates a display surface
pygame.display.set_caption("Pong") #sets the window title

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) #creates a rectangle for the ball
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140) #creates a rectangle for the player paddle
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140) #creates a rectangle for the opponent paddle

#Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

#Game Variables
ball_speed_x = 7 * random.choice((1,-1)) #ball speed in the x direction - random direction at the beginning of the game
ball_speed_y = 7 * random.choice((1,-1)) #ball speed in the y direction - random direction at the beginning of the game
player_speed = 0 #player speed in the y direction
opponent_speed = 7 #opponent speed in the y direction

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Timer
score_time = None

# Game Loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #checks if a key has been pressed
            if event.key == pygame.K_DOWN: #checks if the down arrow key has been pressed
                player_speed += 6 #adds 6 to the player speed
            if event.key == pygame.K_UP: #checks if the up arrow key has been pressed
                player_speed -= 6 #subtracts 6 from the player speed
        if event.type == pygame.KEYUP: #checks if a key has been released
            if event.key == pygame.K_DOWN: #checks if the down arrow key has been released
                player_speed -= 6 #subtracts 6 from the player speed
            if event.key == pygame.K_UP: #checks if the up arrow key has been released
                player_speed += 6 #adds 6 to the player speed

    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals (drawing the game objects on descending order)
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating the score
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)

import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW = (255, 215, 0)
BLUE = (65, 105, 225)
PURPLE = (102, 102, 255)

#données temps 0
WIDTH = 800
HEIGHT = 600       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0,0]
ball_rapidity = [0,0]
paddle1_rapidity = 0
paddle2_rapidity = 0
left_score = 0
right_score = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong game')

# helper function that spawns a ball, returns a position vector and a rapidity vector
def ball_init(right):
    global ball_pos, ball_rapidity 
    ball_pos = [WIDTH/2,HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_rapidity = [horz,-vert]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_rapidity, paddle2_rapidity,left_score,right_score 
    global score1, score2  
    paddle1_pos = [HALF_PAD_WIDTH - 1,HEIGHT/2]
    paddle2_pos = [WIDTH +1 - HALF_PAD_WIDTH,HEIGHT/2]
    left_score = 0
    right_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)


#draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_rapidity, left_score, right_score
           
    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_rapidity
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_rapidity > 0:
        paddle1_pos[1] += paddle1_rapidity
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_rapidity < 0:
        paddle1_pos[1] += paddle1_rapidity
    
    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_rapidity
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_rapidity > 0:
        paddle2_pos[1] += paddle2_rapidity
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_rapidity < 0:
        paddle2_pos[1] += paddle2_rapidity

    #update ball
    ball_pos[0] += int(ball_rapidity[0])
    ball_pos[1] += int(ball_rapidity[1])

    #draw paddles and ball
    pygame.draw.circle(canvas, RED, ball_pos, 20, 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

    #ball collision check on top and bottom walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_rapidity[1] = - ball_rapidity[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_rapidity[1] = -ball_rapidity[1]
    
    #ball collison check on gutters or paddles
    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,paddle1_pos[1] + HALF_PAD_HEIGHT,1):
        ball_rapidity[0] = -ball_rapidity[0]
        ball_rapidity[0] *= 1.1
        ball_rapidity[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        right_score += 1
        ball_init(True)
        
    hit_right_wall = int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH
    hit_paddle = paddle2_pos[1] - HALF_PAD_HEIGHT < ball_pos[1] < paddle2_pos[1] + HALF_PAD_HEIGHT
    
    if  hit_right_wall and hit_paddle:
        ball_rapidity[0] = -ball_rapidity[0]
        ball_rapidity[0] *= 1.1
        ball_rapidity[1] *= 1.1
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        left_score += 1
        ball_init(False)

    #update scores
    myfont1 = pygame.font.SysFont("MS", 20)
    label1 = myfont1.render("Score "+str(left_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("MS", 20)
    label2 = myfont2.render("Score "+str(right_score), 1, (255,255,0))
    canvas.blit(label2, (470, 20))  
    
    
#keydown handler
def keydown(event):
    global paddle1_rapidity, paddle2_rapidity
    
    if event.key == K_UP:
        paddle2_rapidity = -8
    elif event.key == K_DOWN:
        paddle2_rapidity = 8
    elif event.key == K_w:
        paddle1_rapidity = -8
    elif event.key == K_s:
        paddle1_rapidity = 8

#keyup handler
def keyup(event):
    global paddle1_rapidity, paddle2_rapidity
    
    if event.key in (K_w, K_s):
        paddle1_rapidity = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_rapidity = 0

init()


#game loop
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
    
pygame.quit()

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
r =10
padlf = [0,PAD_HEIGHT]
padrt = [0,PAD_HEIGHT]
padlf_vel, padrt_vel = 0,0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(3,4)
        ball_vel[1] = random.randrange(1,5)
    else:
        ball_vel[0] = -random.randrange(3,4)
        ball_vel[1] = -random.randrange(1,5)
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, r  # these are ints
    spawn_ball(RIGHT)
    score1,score2 = 0,0
    
def draw(canvas):
    global score1, score2, padlf, padrt, ball_pos, ball_vel,WIDTH,PAD_WIDTH,r
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), (250, 50), 40, 'White')
    canvas.draw_text(str(score2), (330, 50), 40, 'White')
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0]+r > WIDTH:
        score1 += 1
        spawn_ball(LEFT)
    elif ball_pos[0]-r <= 0:
        score2 += 1
        spawn_ball(RIGHT)
    if ball_pos[1]+r >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1]-r <= 0:
        ball_vel[1] = -ball_vel[1]
        
    
    # draw ball
    canvas.draw_circle(ball_pos,5, r, 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    padlf[0] += padlf_vel
    padlf[1] += padlf_vel
    padrt[0] += padrt_vel
    padrt[1] += padrt_vel
    
    if padlf[0] < 0:
        padlf[0] = 0
        padlf[1] = PAD_HEIGHT
    elif padlf[1] > HEIGHT:
        padlf[0] = HEIGHT - PAD_HEIGHT
        padlf[1] = HEIGHT
        
    if padrt[0] < 0:
        padrt[0] = 0
        padrt[1] = PAD_HEIGHT
    elif padrt[1] > HEIGHT:
        padrt[0] = HEIGHT - PAD_HEIGHT 
        padrt[1] = HEIGHT
        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH,padlf[0]],[HALF_PAD_WIDTH,padlf[1]],PAD_WIDTH,'White')
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH,padrt[0]],[WIDTH-HALF_PAD_WIDTH,padrt[1]],PAD_WIDTH,'White')
    
    # determine whether paddle and ball collide    
    if ball_pos[1] > padlf[0] and ball_pos[1] < padlf[1] and ball_pos[0]-r == PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] += 1
    elif ball_pos[1] > padrt[0] and ball_pos[1] < padrt[1] and ball_pos[0]+r == WIDTH-PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] += -1
    
    # draw scores

def keydown(key):
    global padlf_vel, padrt_vel
    if chr(key) == 'S':
        padlf_vel = 5
    elif chr(key) == 'W':
        padlf_vel = -5
        
    if key == simplegui.KEY_MAP['down']:
        padrt_vel = 5
    elif key == simplegui.KEY_MAP['up']:
        padrt_vel = -5
        
        
def keyup(key):
    global padlf_vel, padrt_vel
    if chr(key) == 'S':
        padlf_vel = 0
    elif chr(key) == 'W':
        padlf_vel = 0
        
    if key == simplegui.KEY_MAP['down']:
        padrt_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        padrt_vel = 0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()

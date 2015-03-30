# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global nums,state,exposed,turns
    nums = []
    state = 0
    turns = 0
    for x in range(8):
        nums.append(x)
    nums.extend(nums)
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(nums)

# define event handlers
def mouseclick(pos):
    global index, index1,index2,exposed,state,nums,turns,counter
    index = pos[0]//50
    if exposed[index] == True:
        return 0
    elif state == 0:
        state = 1
        index1 = index
        exposed[index1] = True
    elif state == 1:
        state = 2
        index2 = index
        exposed[index2] = True
    elif state == 2:
        state = 1
        turns += 1
        if nums[index1] != nums[index2]:
            exposed[index1] = False
            exposed[index2] = False
        index1 = index
        exposed[index] = True

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global nums,exposed,turns
    for x in range(len(nums)):
        canvas.draw_text(str(nums[x]), (10 + x*50, 70), 70, 'White')

    for x in range(len(exposed)):
        if exposed[x] == False :
            canvas.draw_line([25 + x *50, 1], [25 + x *50, 99], 48, 'Green')
    label.set_text('Turns = ' + str(turns))
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("")
#label.set_text('Turns = ' + str(turns))
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric

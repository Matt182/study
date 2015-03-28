# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global nums,state,exposed,turns
    nums = []
    for x in range(8):
        nums.append(x)
    nums.extend(nums)
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    print nums
    random.shuffle(nums)
    print nums
    state = 0
    turns = 0

     
# define event handlers
def mouseclick(pos):
    global index1,index2,exposed,state,nums,turns
    if state == 0:
        index1 = pos[0]//50
        if exposed[index1] == True:
            return 0
        state = 1
        exposed[index1] = True
    elif state == 1:
        index2 = pos[0]//50
        if exposed[index2] == True:
            return 0
        state = 2
        exposed[index2] = True
    else:
        turns += 1
        if nums[index1] != nums[index2]:
            exposed[index1] = False
            exposed[index2] = False
        index1 = pos[0]//50
        if exposed[index1] == True:
            return 0
        state = 1
        exposed[index1] = True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global nums,exposed,turns
    for x in range(len(nums)):
        canvas.draw_text(str(nums[x]), (10 + x*50, 70), 70, 'White')

    for x in range(len(exposed)):
        if exposed[x] == False :
            canvas.draw_line([25 + x *50, 1], [25 + x *50, 99], 48, 'Green')
        
            
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ")
label.set_text('Turns = ')
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

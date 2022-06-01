# implementation of card game - Memory

import simplegui
import random

#frame 800x100
canvas_width = 800
canvas_height = 100
# cards are logically 50x100 pixels in size  
rectangle_width = 50
rectangle_height = 100
line_width = 1
pos_left = pos_top = turns = 0
index1 = index2 = index =0

# helper function to initialize globals
def new_game():
    global state, cards, exposed, turns
    global letter_color, bottom_color
    turns =0
    label.set_text('Turns =' + str(turns)) 
    state = 0
    letter_color = 'Green'
    bottom_color = 'Green'
    cards=range(0,8)
    cards.extend(range(0,8))
    random.shuffle(cards)
    print cards
    exposed = [False, False,False,False,False,False,False,
               False,False,False,False,False,False,False,
               False,False]
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global bottom_color, letter_color, turns, index1, index2
    global state, exposed, cards,  save_card1, save_card2, first_card, sec_card
    index = pos[0]//50
    if exposed[index] == False:
        if state == 0:
            exposed[index] = True
            first_card = cards[index]
            index1 = index
            #print "first card", first_card
            state = 1

        elif state == 1:
            exposed[index] = True
            sec_card = cards[index]
            index2 = index
            #print "sec card", sec_card
            state = 2

        else:
            if first_card != sec_card: 
                #print "different cards", first_card, sec_card
                exposed[index1] = False 
                exposed[index2] = False 
            else: 
                #print "equal cards", first_card, sec_card
                exposed[index1] = True
                exposed[index2] = True
            exposed[index] = True
            index1= index
            first_card = cards[index]
            turns+=1
            state = 1
        label.set_text('Turns =' + str(turns)) 
    
    else: 
        print "ignore click"
        exposed[index] = True
                     
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed, state, turns
    global pos_left, pos_top, bottom_color, letter_color
    
    for i in range (len(cards)):
        card_pos = 50*i
        pos_left = 50*i
        pos_right= pos_left + rectangle_width
        pos_bottom = pos_top + rectangle_height
        
        if exposed[i] == True:
            bottom_color = 'White'
            letter_color = 'Red'       
        else: 
            bottom_color = 'Green'
            letter_color = 'Green'
            
        canvas.draw_polygon([(pos_left, pos_top), 
                             (pos_right, pos_top), 
                             (pos_right, pos_bottom),
                             (pos_left, pos_bottom)
                            ], line_width, 'Red', bottom_color)
       
        canvas.draw_text(str(cards[i]), [(card_pos) + 12,60], 50, letter_color)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory Play", canvas_width, canvas_height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

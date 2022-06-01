# Mini-project #6 - Blackjack
#Natasha Medina

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
outcome1 = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        #create Hand object
        self.hand = list()
        self.count = 0
        self.aces_eleven=0

    def __str__(self):
        # return a string representation of a hand  
        string_hand= ""
        for i in range(len(self.hand)): 
            string_hand += str(self.hand[i])
        return string_hand
        
        
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)	

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        count=0
        aces_eleven = 0 
        #print "LEN SELF HAND",len(self.hand)
        for i in range(len(self.hand)):
            if self.hand[i].get_rank() != 'A':
                for key, value in VALUES.items():
                    if self.hand[i].get_rank() == key:
                        if count + value > 21: 
                            if aces_eleven >= 1: 
                                count +=value
                                count -= 10*aces_eleven
                                aces_eleven=0                                       
                            else: 
                                count += value                          
                        else:
                            count += value                           
            else:
                if count + 10 < 21:
                    count +=11
                    aces_eleven +=1             
                else:
                    count +=1
        return count
                
        if len(self.hand) == 0:  
            return count
      
    
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
 
        for card in self.hand: 
            card.draw(canvas, pos)
            pos[0] += 110
       
     
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        # create a Deck object
        for suit in SUITS: 
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
                           
    def shuffle(self):
        random.shuffle(self.deck) 
        # use random.shuffle()

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(len(self.deck)-1)
      
    
    def __str__(self):
        # return a string representing the deck
        string_deck= ""
        for i in range(len(self.deck)): 
            string_deck += str(self.deck[i])
        return string_deck
   
#define event handlers for buttons
def deal():
    global outcome, in_play, outcome1, score
    global interrupt
    global new_player, dealer_hands,my_deck
    interrupt = False
    outcome = ""
    outcome1 = "Hit or Stand?"
    i=0
    new_player = Hand()
    dealer_hands = Hand()
    my_deck = Deck()
    #shuffle deck
    my_deck.shuffle()

    #adding two cards to each hand
    if in_play == False:
        while i < 2:
            new_player.add_card(my_deck.deal_card())
            dealer_hands.add_card(my_deck.deal_card())
            i+=1
        in_play = True
    else:         
        score -= 1
        outcome = "PLAYER lost the round for INTERRUPT"     
        interrupt = True
        in_play = False
 
    print "new player is ",new_player
    print "dealer_hands is ", dealer_hands
    
def hit():
    # replace with your code below
    global outcome, in_play, outcome1, score
    global new_player, dealer_hands,my_deck
    global interrupt

    # if the hand is in play, hit the player
    
    if in_play == True: 
        if interrupt == True: 
            outcome = ""
        # if busted, assign a message to outcome, update in_play and score
        if new_player.get_value() > 21: 
            print outcome + " " + "with next value ", new_player.get_value()
            outcome = "You have busted. New deal?"
            outcome1= ""
            in_play = False
        else:
            in_play = True
            new_player.add_card(my_deck.deal_card())
            if new_player.get_value() > 21:
                outcome = "You have busted. New deal?"
                outcome1 = ""
                in_play = False
                score -=1
            
        print new_player 
        print "el valor de new_player es",new_player.get_value()
        return new_player
        
    else: 
        pass
    
    if interrupt == True: 
        outcome = ""
        pass
        
        
def stand():
    global outcome, in_play, score
    global new_player, dealer_hands,my_deck
    
    if in_play == True:
        
        while dealer_hands.get_value() < 17: 
            dealer_hands.add_card(my_deck.deal_card())

        if new_player.get_value() <= dealer_hands.get_value(): 
            if dealer_hands.get_value() <= 21:
                print "Dealer Wins with ", dealer_hands.get_value()
                print "And PLAYER LOST with ",new_player.get_value()
                outcome = "DEALER WINS!! SORRY BUT YOU LOST "
                score -=1
                in_play= False
            else: 
                
                if new_player.get_value() <= 21:
                    outcome = "DEALER HAS BUSTED AND PLAYER WINS!"
                    score +=1
                    in_play = False
                    
                else: 
                    outcome = "BOTH HAS BUSTED!"
                    in_play = False
        else:
            if dealer_hands.get_value() <= 21:
                score +=1
                outcome = "PLAYER WINS!! TAKE YOUR TIE"
                print "Player WINS with ", new_player.get_value() 
                print "And Dealer LOST with ",dealer_hands.get_value()
                in_play = False
           
    else:
        in_play = False
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, outcome1
    global score, in_play
    canvas.draw_text("Dealer", (70, 180), 25, 'White')   
    canvas.draw_text("Player", (70, 380), 25, 'White')
    canvas.draw_text(outcome1, (250, 380), 25, 'White','monospace')
    canvas.draw_text('Score: ' + str(score), (430, 70), 30, 'White','monospace')
    canvas.draw_text("Blackjack", (60, 60), 40, 'Orange','monospace')
    canvas.draw_text(outcome, (50, 560), 25, 'Orange','monospace')
    new_player.draw(canvas,[70, 400])
    dealer_hands.draw(canvas,[70, 200])
    if in_play==True:
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], 
                    CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1])
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [70 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            
    else:
        #canvas.draw_image(card_images, (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [70 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
         
        dealer_hands.draw(canvas,[70, 200])
        
  
   
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

import random

def play(player1, player2, deck):

        p1 = player1
        p2 = player2

        while(True):
                next_turn = raw_input("Type 'Next' to start next turn\n")
                if (next_turn == 'Next'):
                        
                        # Draw Cards
                        p1_card = p1[0]
                        p2_card = p2[0]
                        
                        # Retrieve value of cards from deck
                        p1_val = deck[p1_card]
                        p2_val = deck[p2_card]

                        print '\nPlayer 1: ', p1_card, ' <===> Player 2: ', p2_card

                        # Add cards to hand of winner (append to list)
                        if(p1_val > p2_val):
                                winner = 'Player 1'
                                p1.remove(p1_card)
                                p2.remove(p2_card)
                                p1.append(p1_card)
                                p1.append(p2_card)
                        else:
                                winner = 'Player 2'
                                p2.remove(p2_card)
                                p1.remove(p1_card)
                                p2.append(p2_card)
                                p2.append(p1_card)

                        print winner, 'wins'

                        # Calcuate score (maybe use len of list)
                        p1_score = len(p1)
                        p2_score = len(p2)

                        print 'Scoreboard: Player 1 has ', p1_score, ' points and Player 2 has ', p2_score, ' points'

                        if(p1_score == 0 or p2_score == 0):
                                print winner, 'has won the game!'
                        
                elif(next_turn == 'Quit'):
                     exit()
                        
        
        
        

# Handles dealing of the deck
def deal(deck):
	p1 = []
	p2 = []

	deck_keys = list(deck.keys())
	
	# Distribute Cards
	for i in range(52):
		whichHand = random.randint(1,2)
		if(whichHand == 1 and len(p1) < 26):
			p1.append(deck_keys[i])
		elif(len(p2) < 26):
			p2.append(deck_keys[i])
		elif(whichHand == 2 and len(p2) < 26):
			p2.append(deck_keys[i])
		elif(len(p1) < 26):
			p1.append(deck_keys[i])
	
	# Randomize hand
	random.shuffle(p1)
	random.shuffle(p2)
		

	return p1, p2
			

# Driver for the program
def game():
	
	start = raw_input("Type 'Play' to begin or 'Quit' to quit at anytime\n")
	
	deck = {'A-D':13,'2-D':1,'3-D':2,'4-D':3,'5-D':4,'6-D':5,'7-D':6,'8-D':7,'9-D':8,'10-D':9,'J-D':10,'Q-D':11,'K-D':12,'A-H':13,'2-H':1,'3-H':2,'4-H':3,'5-H':4,'6-H':5,'7-H':6,'8-H':7,'9-H':8,'10-H':9,'J-H':10,'Q-H':11,'K-H':12,'A-S':13,'2-S':1,'3-S':2,'4-S':3,'5-S':4,'6-S':5,'7-S':6,'8-S':7,'9-S':8,'10-S':9,'J-S':10,'Q-S':11,'K-S':12,'A-C':13,'2-C':1,'3-C':2,'4-C':3,'5-C':4,'6-C':5,'7-C':6,'8-C':7,'9-C':8,'10-C':9,'J-C':10,'Q-C':11,'K-C':12}
	p1, p2 = deal(deck)

	if(start == 'Play'):
                play(p1, p2, deck)
	elif(start == 'Quit'):
                exit()
	

game()


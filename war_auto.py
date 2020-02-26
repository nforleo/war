import random

#
#   Logic for when a war occurs
#   @params:
#   p1 - hand for player 1, p2 - hand for player 2, deck - the deck, n - which instance of war we are on
#
def war(p1, p2, deck, n):

    p1_len = len(p1)
    p2_len = len(p2)

    hand_size = 4*n

    if(p1_len > hand_size and p2_len > hand_size):
        p1_card = p1[hand_size]
        p2_card = p2[hand_size] 
        
        if(deck[p1_card] > deck[p2_card]):
            for i in range(1 + hand_size):
                p1.append(p1[0])
                p1.append(p2[0])
                p1.remove(p1[0])
                p2.remove(p2[0])
        elif(deck[p1_card] == deck[p2_card]):
            war(p1, p2, deck, n+1)
        else:
            for i in range(1 + hand_size):
                p2.append(p2[0])
                p2.append(p1[0])
                p2.remove(p2[0])
                p1.remove(p1[0])
    else:
        # Handle each of the players' hand individually?
        # Idk what to do here, so for now the cards will just be removed and appended
        #   to the end of each players' hand respectively.
        p1.append(p1[0])
        p1.remove(p1[0])
        p2.append(p2[0])
        p2.remove(p2[0])

def play(p1, p2, deck):
    p1_wins = 0
    p2_wins = 0
    game_running = True
    while(game_running):
        # Draw Cards
        p1_card = p1[0]
        p2_card = p2[0]
        
        # Retrieve value of cards from deck
        p1_val = deck[p1_card]
        p2_val = deck[p2_card]
        

        # Add cards to hand of winner (append to list)
        if(p1_val > p2_val):
            p1.remove(p1_card)
            p2.remove(p2_card)
            p1.append(p1_card)
            p1.append(p2_card)
        elif(p1_val == p2_val):
            war(p1, p2, deck, 1)
        else:
            p2.remove(p2_card)
            p1.remove(p1_card)
            p2.append(p2_card)
            p2.append(p1_card)

        # Calculate score (maybe use len of list)
        p1_score = len(p1)
        p2_score = len(p2)

        if(p1_score == 0 or p2_score == 0):
            game_running = False
            if(p1_score == 0):
                # False == Player 2
                winner = False
            else:
                # True == Player 1
                winner = True

    return winner
        
        

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

    start = raw_input("Type 'start' to begin or 'quit' to exit\n")
    
    deck = {'A-D':13,'2-D':1,'3-D':2,'4-D':3,'5-D':4,'6-D':5,'7-D':6,'8-D':7,'9-D':8,'10-D':9,'J-D':10,'Q-D':11,'K-D':12,'A-H':13,'2-H':1,'3-H':2,'4-H':3,'5-H':4,'6-H':5,'7-H':6,'8-H':7,'9-H':8,'10-H':9,'J-H':10,'Q-H':11,'K-H':12,'A-S':13,'2-S':1,'3-S':2,'4-S':3,'5-S':4,'6-S':5,'7-S':6,'8-S':7,'9-S':8,'10-S':9,'J-S':10,'Q-S':11,'K-S':12,'A-C':13,'2-C':1,'3-C':2,'4-C':3,'5-C':4,'6-C':5,'7-C':6,'8-C':7,'9-C':8,'10-C':9,'J-C':10,'Q-C':11,'K-C':12}
    p1, p2 = deal(deck)

    if(start == 'start'):
                play(p1, p2, deck)
    elif(start == 'quit'):
                exit()
    p1_wins = 0
    p2_wins = 0

    for n in range(1000):
        p1, p2 = deal(deck)
        winner = play(p1, p2, deck)
        if(winner):
            p1_wins += 1
        else:
            p2_wins += 1

    print 'P1\tP2\n'
    print p1_wins, '\t', p2_wins

game()

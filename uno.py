from deck import Deck, COLOURS
from player import Player


current_deck:Deck = Deck()
player_count:int = 3
players:list = []
player_index:int = 0
turn_order:int = 1
scoring:dict = {}
round_counter = 0
current_colour = None
current_player = None

# for card in current_deck.cards:
# 	print(f"{card}-{card.id}")

def next_player():
	return(player_index + turn_order) % player_count

def prev_player():
	return(player_index - turn_order) % player_count

def press_key_to_cont():
	input("Press key to continue....")
	print("")

def choose_colour():
	response = ""
	while response not in COLOURS:
		response = input(f"{current_player} - what colour do you want: ")
	return response

def choose_card():
	while True:
		option = input(f"What card do you want to play? (give index or 'pickup'):  ")
		match = next((card for card in current_player.hand if str(card) == option),None)
		if match or option == 'pickup':
			break

	if option == "pickup":
		return option
	return match,match.id


# #Initalise Game
# if len(players) == 0:
# 	player_count :int = int(input(f"How many players are there?:  "))
# 	for counter in range(player_count):
# 		players.append(Player(input(f"Player {counter+1} - what is your name?:  "),current_deck,7))


players.append(Player("John",current_deck,7))
players.append(Player("Anna",current_deck,7))
players.append(Player("Dave",current_deck,7))

for player in players:
	scoring[player.name] = 0

#Start Round!

def uno_round():
	# Declare that these variables belong to the global scope
	global player_index, turn_order, current_colour, current_player, round_counter

	current_player = players[player_index]


	while True : #and (round_counter < 2)

		print("")
		print("Current Player: ")
		print(current_player)
		print("")

		print(f"{current_player}'s Hand:")
		current_player.show_hand()
		print("")

		print("Active Card: ")
		current_deck.show_active_card()
		if current_deck.active_card().colour != "Wild":
			current_colour = current_deck.active_card().colour
		else:
			print(current_colour)
		print("")

		#Pick Card to Play
		response = choose_card()

		#Add card if player carn't go
		if response == "pickup":
			print("")
			new_card = current_player.pickup_card()
			print(f"Uh oh - {current_player} had to pick up a card ({new_card})! They now have {len(current_player.hand)} cards.")
			print("")
			press_key_to_cont()
			print("")

		#Otherwise play the card onto the discard pile
		else:
			played_card = current_player.play_card(int(response[1]),current_colour)
			print("")
			print("Active Card: ")
			current_deck.show_active_card()
			print("")

			#Resolve any card effects
			if played_card is not None:
				card_type = played_card.special
				print(card_type)
				if card_type == 'Skip':
					player_index = next_player()
					current_player = players[player_index]
					print("")
					print(f"{current_player} - sorry, you miss your go this time around")
					press_key_to_cont()
					print("")

				elif card_type == 'Reverse':
					turn_order *= -1
					print("")
					print(f"Turn order reversed!")
					press_key_to_cont()
					print("")

				elif card_type == 'Draw 2':
					player_index = next_player()
					current_player = players[player_index]
					print("")
					print(f"{current_player} - sorry, you have to pickup two cards!")
					current_player.pickup_card()
					current_player.pickup_card()
					press_key_to_cont()
					print("")

				elif card_type == 'Wild Card':
					current_colour = choose_colour()

				elif card_type == 'Wild Draw 4':
					player_index = next_player()
					victim = players[player_index]
					print("")
					print(f"{victim} - sorry, you have to pickup four cards!")
					print("")
					victim.pickup_card()
					victim.pickup_card()
					victim.pickup_card()
					victim.pickup_card()
					current_colour = choose_colour()
					current_player = victim
					print("")

		#Check if no cards left and therefore current player is the winner
		if len(current_player.hand) == 0:
			break
		
		#Move to Next Player
		player_index = next_player()
		current_player = players[player_index]
		round_counter += 1

		#LOOP REPEATS HERE

	#Someone has no cards left, tally up the score and assign it to them
	print(f"{current_player} - You are the winner of this round!")
	print("counting up the scores!")

	score = 0
	for player in players:
		if player == current_player:
			continue
		#print(f"{player}-{player.hand_score()}")
		score += player.hand_score() 
		print("")

	scoring[current_player.name] += score

	print(scoring)

game_options = "asdf"

while game_options not in ["one round","points total"]:
	game_options = input("Do you want to play 'one round' or upto a 'points total': ")

if game_options == 'one round':
	uno_round()
else:
	points_total = int(input("What points total do you want to go to? "))
	points_total_reached = False
	while not points_total_reached:
		uno_round()
		for score in scoring.values():
			if score > points_total:
				points_total_reached = True
				print("")
				print(f"Congratulations {name} - you are the winner")
				print("""
                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
------------------------------------------------

This ASCII pic can be found at
https://asciiart.website/art/1710
				
				""")
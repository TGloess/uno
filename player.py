from deck import Deck,COLOURS,VALUES,Card

class Player:
	def __init__(self,name:str,deck:Deck,num_cards):
		self.hand = []
		self.name = name
		self.deck = deck
		self.deal_cards(num_cards)

	def __str__(self):
		return self.name
		
	def deal_cards(self,num_cards:int):
		for i in range(num_cards):
			self.hand.append(self.deck.draw_card())
			self.order_hand()

	def pickup_card(self):
			new_card = self.deck.draw_card()
			self.hand.append(new_card)
			self.order_hand()
			return new_card

	def order_hand(self):
		self.hand = sorted(self.hand, key=lambda x: (x.colour, x.value,x.special))

	def uno_status(self) -> bool:
		if len(self.hand) == 1:
			return True
		return False

	def show_hand(self):
		for card in self.hand:
			print(card)

	def play_card(self,card_id,colour):
		id = 0
		for card in self.hand:
			if card.id == card_id:
				player_card = card
				break
			id += 1
		active_card = self.deck.active_card()
		
		# print(f"PLAYER CARD = {player_card}")
		# print(f"ACTIVE CARD = {active_card}")

		if player_card.colour == colour or player_card.value == active_card.value or player_card.colour == 'Wild':
			print('can play card')
			print('')
			self.hand.pop(id)
			self.deck.discard.append(player_card)

			if player_card.colour == 'Wild' or player_card.special is not None:
				return player_card
			return None

	def hand_score(self):
		score:int = 0
		for card in self.hand:
			score += card.value
		return score
import random

COLOURS = ["Red","Blue","Green","Yellow"]
VALUES = [0,1,2,3,4,5,6,7,8,9]

class Deck:
	

	def __init__(self) -> None:
		self.cards = []
		self.discard = []
		card_id = 1
		#Add in regular cards (1x 0 and 2x 1 through 9)
		for c in COLOURS:
			for n in VALUES:
				self.cards.append(Card(c,n,None,card_id))
				card_id +=1
				if n > 0:
					#Add additional card if >0
					self.cards.append(Card(c,n,None,card_id))
					card_id +=1

			#Add in special cards
			self.cards.append(Card(c,20,'Skip',card_id))
			self.cards.append(Card(c,20,'Skip',card_id+1))
			self.cards.append(Card(c,20,'Reverse',card_id+2))
			self.cards.append(Card(c,20,'Reverse',card_id+3))
			self.cards.append(Card(c,20,'Draw 2',card_id+4))
			self.cards.append(Card(c,20,'Draw 2',card_id+5))

			card_id += 6

		#Add in Wild Cards
		self.cards.append(Card('Wild',50,'Wild Draw 4',card_id))
		self.cards.append(Card('Wild',50,'Wild Draw 4',card_id+1))
		self.cards.append(Card('Wild',50,'Wild Draw 4',card_id+2))
		self.cards.append(Card('Wild',50,'Wild Draw 4',card_id+3))
		self.cards.append(Card('Wild',50,'Wild Card',card_id+4))
		self.cards.append(Card('Wild',50,'Wild Card',card_id+5))
		self.cards.append(Card('Wild',50,'Wild Card',card_id+6))
		self.cards.append(Card('Wild',50,'Wild Card',card_id+7))

		card_id += 8

		self.shuffle_deck()

	def shuffle_deck(self):
		random.shuffle(self.cards)

	def draw_card(self):
		#If deck is empty, reuse discard pile
		if len(self.cards) == 0:
			print('Draw pile empty - Reshuffling discard pile before drawing a card')
			self.cards = self.discard
			self.discard = []
			self.shuffle_deck()
		return self.cards.pop()

	def active_card(self):
		if len(self.discard) == 0:
			#print('Playing first card')
			self.discard.append(self.draw_card())

		return self.discard[-1]
		

	def show_active_card(self):
		print(self.active_card())


class Card:
	def __init__(self,colour,value,special,id):
		self.colour:str = colour
		self.value:int = value
		self.special:str|None = special
		self.id = id

	def __str__(self):
		if self.colour in COLOURS and self.value<10:
			return self.colour + " " + str(self.value)
		elif self.colour != "Wild":
			return self.colour + " " + str(self.special)
		else:
			return self.special
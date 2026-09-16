import random
class Card:
    """ A class to describe cards in a pack """
    cards_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    cards_suits = ["S","H","D","C"]
    cards_long_values = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    cards_long_suits = ["of Spades", "of Hearts", "of Diamonds", "of Clubs"]
    def __init__(self, number: int):
        self._card_number = number


    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        return Card.cards_suits[self._card_number//13]

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        return Card.cards_values[self._card_number%13]

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return self.get_value()+self.get_suit()

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        return Card.cards_long_values[self._card_number%13] , Card.cards_long_suits[self._card_number//13]
        


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        return len(self._card_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        return self._card_list.pop(0)

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)


card = Card(1)
print(card.get_suit())
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card: Card = deck.take_top_card()
    print(card.get_long_name())
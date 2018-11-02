# Author: Joseph Laos
"""  Models a traditional playing card
"""


class Card:
    """One object of class Card stores one card's rank and suit."""
    # valid values for rank and suit
    suits = ('d', 'c', 'h', 's')
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    def __init__(self, rank, suit):
        """Card constructor. Executed every time a new Card object is created."""
        if rank in Card.ranks:
            self.rank = rank
        else:
            self.rank = Card.ranks[0]
        if suit in Card.suits:
            self.suit = suit
        else:
            self.suit = Card.suits[0]

    def getRank(self):
        """returns rank of Card object"""
        return self.rank

    def getSuit(self):
        """returns suit of Card object"""
        return self.suit

    def bjValue(self):
        """returns blackjack value of Card object (1 - 10)"""
        if self.rank < 10:
            val = self.rank
        else:
            val = 10
        return val

    def __str__(self):
        """the __str__( ) method is used to convert a Card object into a string"""
        rankStr = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                   10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
        suitStr = {'d': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades'}
        return rankStr.get(self.rank) + ' of ' + suitStr.get(self.suit)


if __name__ == "__main__":
    def cardData(card):
        """returns string of all card data"""
        return "Card rank: " + str(card.getRank()) + "\nCard suit: " + card.getSuit() + "\nCard blackjack value: " \
            + str(card.bjValue()) + "\nCard string value: " + str(card) + "\n"
    cardList = []
    for suit in Card.suits[:]:
        for rank in Card.ranks[6:Card.ranks.__len__()]:
            cardList.append(Card(rank, suit))
    for card in cardList[:]:
        print(cardData(card))




"""---OUTPUT---
Card 1:

Card rank: 13
Card suit: d
Card blackjack value: 10
Card string value: King of Diamonds

Card 2:

Card rank: 1
Card suit: s
Card blackjack value: 1
Card string value: Ace of Spades

Card 3:

Card rank: 5
Card suit: h
Card blackjack value: 5
Card string value: Five of Hearts

Card 4:

Card rank: 10
Card suit: c
Card blackjack value: 10
Card string value: Ten of Clubs

------Default values below due to intentional errors------

Card 5:

Card rank: 1
Card suit: d
Card blackjack value: 1
Card string value: Ace of Diamonds

Card 6:

Card rank: 1
Card suit: d
Card blackjack value: 1
Card string value: Ace of Diamonds

------Test methods individually just in case------

13
s
10
Ace of Spades

Process finished with exit code 0
"""
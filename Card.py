# Author: Joseph Laos
"""  Models a traditional playing card, handles exceptions
"""


class Card:
    """One object of class Card stores one card's rank and suit."""
    # valid values for rank and suit
    suits = ('d', 'c', 'h', 's')

    def __init__(self, rank, suit):
        """Card constructor. Executed every time a new Card object is created."""
        # throws TypeErrot if rank is not an int
        if not isinstance(rank, int):
            raise TypeError("Rank should be an integer\n")
        # throw TypeError if suit is not a string
        elif not isinstance(suit, str):
            raise TypeError("Suit should be a string: " + str(Card.suits) + "\n")
        # hrows ValueError if rank int outside of expeccted range
        elif rank < 1 or rank > 13:
            raise ValueError("Rank should be in the range 1 - 13\n")
        # throws valueError if suit string not contained in Card.suita
        elif suit not in Card.suits:
            raise ValueError("Suit should be one of the following: " + str(Card.suits) + "\n")
        else:
            self.rank = rank
            self.suit = suit

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
            + str(card.bjValue()) + "\nCard string value: " + str(card) + "\n\n"

    def cardListToString(cardList):
        """returns string of cardData for list of cards"""
        retString = ''
        if cardList.__len__() == 0:
            retString = "EMPTY LIST"
        for card in cardList[:]:
            try:
                retString += cardData(card)
            except:
                retString += "Invalid card in list\n"
        return retString

    def addCardToList(rank, suit, cardList):
        """Given a rank, a suit and a list, attempts to instantiate a card and add it to a list"""
        print("Attempting to create and add rank " + str(rank) + " of " + str(suit) + " to list")
        try:
            cardList.append(Card(rank, suit))
            print("Card successfully added to list\n")
        except TypeError as e:
            print("CARD CREATION FAILED: " + str(e.__class__) + "\n" + str(e))
        except ValueError as e:
            print("CARD CREATION FAILED: " + str(e.__class__) + "\n" + str(e))

    # Some cards have rank outside range 1-13
    print("Add only cards with good values to list, range includes several BAD RANKS (greater than 13 or less than 1):"
          "\n")
    cardList = []

    for suit in Card.suits[:]:
        for rank in range(-1, 16):
            addCardToList(rank, suit, cardList)

    print("----------List of valid cards---------:\n\n" + cardListToString(cardList))

    # Some cards have bad suit strings.
    print("Add only cards with good values to list, range includes several BAD SUITS:\n")
    cardList = []

    testSuits = ('a', 'b', 'c', 'd')
    for suit in testSuits:
        addCardToList(1, suit, cardList)

    # Wrong types for rank and/or suit
    print("---Valid cards in list---\n\n" + cardListToString(cardList))

    print("Add only cards with good values to list, range includes several RANKS AND SUITS THAT ARE IN WRONG FORMAT:\n")
    cardList = []
    addCardToList(1, 1, cardList)
    addCardToList("c", "c", cardList)
    addCardToList(1, 1.83, cardList)
    addCardToList(1.55, 'd', cardList)
    addCardToList(13, 'cat', cardList)

    print("---Valid cards in list---\n\n" + cardListToString(cardList))

"""
Add only cards with good values to list, range includes several BAD RANKS (greater than 13 or less than 1):

Attempting to create and add rank -1 of d to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 0 of d to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 1 of d to list
Card successfully added to list

Attempting to create and add rank 2 of d to list
Card successfully added to list

Attempting to create and add rank 3 of d to list
Card successfully added to list

Attempting to create and add rank 4 of d to list
Card successfully added to list

Attempting to create and add rank 5 of d to list
Card successfully added to list

Attempting to create and add rank 6 of d to list
Card successfully added to list

Attempting to create and add rank 7 of d to list
Card successfully added to list

Attempting to create and add rank 8 of d to list
Card successfully added to list

Attempting to create and add rank 9 of d to list
Card successfully added to list

Attempting to create and add rank 10 of d to list
Card successfully added to list

Attempting to create and add rank 11 of d to list
Card successfully added to list

Attempting to create and add rank 12 of d to list
Card successfully added to list

Attempting to create and add rank 13 of d to list
Card successfully added to list

Attempting to create and add rank 14 of d to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 15 of d to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank -1 of c to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 0 of c to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 1 of c to list
Card successfully added to list

Attempting to create and add rank 2 of c to list
Card successfully added to list

Attempting to create and add rank 3 of c to list
Card successfully added to list

Attempting to create and add rank 4 of c to list
Card successfully added to list

Attempting to create and add rank 5 of c to list
Card successfully added to list

Attempting to create and add rank 6 of c to list
Card successfully added to list

Attempting to create and add rank 7 of c to list
Card successfully added to list

Attempting to create and add rank 8 of c to list
Card successfully added to list

Attempting to create and add rank 9 of c to list
Card successfully added to list

Attempting to create and add rank 10 of c to list
Card successfully added to list

Attempting to create and add rank 11 of c to list
Card successfully added to list

Attempting to create and add rank 12 of c to list
Card successfully added to list

Attempting to create and add rank 13 of c to list
Card successfully added to list

Attempting to create and add rank 14 of c to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 15 of c to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank -1 of h to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 0 of h to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 1 of h to list
Card successfully added to list

Attempting to create and add rank 2 of h to list
Card successfully added to list

Attempting to create and add rank 3 of h to list
Card successfully added to list

Attempting to create and add rank 4 of h to list
Card successfully added to list

Attempting to create and add rank 5 of h to list
Card successfully added to list

Attempting to create and add rank 6 of h to list
Card successfully added to list

Attempting to create and add rank 7 of h to list
Card successfully added to list

Attempting to create and add rank 8 of h to list
Card successfully added to list

Attempting to create and add rank 9 of h to list
Card successfully added to list

Attempting to create and add rank 10 of h to list
Card successfully added to list

Attempting to create and add rank 11 of h to list
Card successfully added to list

Attempting to create and add rank 12 of h to list
Card successfully added to list

Attempting to create and add rank 13 of h to list
Card successfully added to list

Attempting to create and add rank 14 of h to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 15 of h to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank -1 of s to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 0 of s to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 1 of s to list
Card successfully added to list

Attempting to create and add rank 2 of s to list
Card successfully added to list

Attempting to create and add rank 3 of s to list
Card successfully added to list

Attempting to create and add rank 4 of s to list
Card successfully added to list

Attempting to create and add rank 5 of s to list
Card successfully added to list

Attempting to create and add rank 6 of s to list
Card successfully added to list

Attempting to create and add rank 7 of s to list
Card successfully added to list

Attempting to create and add rank 8 of s to list
Card successfully added to list

Attempting to create and add rank 9 of s to list
Card successfully added to list

Attempting to create and add rank 10 of s to list
Card successfully added to list

Attempting to create and add rank 11 of s to list
Card successfully added to list

Attempting to create and add rank 12 of s to list
Card successfully added to list

Attempting to create and add rank 13 of s to list
Card successfully added to list

Attempting to create and add rank 14 of s to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

Attempting to create and add rank 15 of s to list
CARD CREATION FAILED: <class 'ValueError'>
Rank should be in the range 1 - 13

----------List of valid cards---------:

Card rank: 1
Card suit: d
Card blackjack value: 1
Card string value: Ace of Diamonds

Card rank: 2
Card suit: d
Card blackjack value: 2
Card string value: Two of Diamonds

Card rank: 3
Card suit: d
Card blackjack value: 3
Card string value: Three of Diamonds

Card rank: 4
Card suit: d
Card blackjack value: 4
Card string value: Four of Diamonds

Card rank: 5
Card suit: d
Card blackjack value: 5
Card string value: Five of Diamonds

Card rank: 6
Card suit: d
Card blackjack value: 6
Card string value: Six of Diamonds

Card rank: 7
Card suit: d
Card blackjack value: 7
Card string value: Seven of Diamonds

Card rank: 8
Card suit: d
Card blackjack value: 8
Card string value: Eight of Diamonds

Card rank: 9
Card suit: d
Card blackjack value: 9
Card string value: Nine of Diamonds

Card rank: 10
Card suit: d
Card blackjack value: 10
Card string value: Ten of Diamonds

Card rank: 11
Card suit: d
Card blackjack value: 10
Card string value: Jack of Diamonds

Card rank: 12
Card suit: d
Card blackjack value: 10
Card string value: Queen of Diamonds

Card rank: 13
Card suit: d
Card blackjack value: 10
Card string value: King of Diamonds

Card rank: 1
Card suit: c
Card blackjack value: 1
Card string value: Ace of Clubs

Card rank: 2
Card suit: c
Card blackjack value: 2
Card string value: Two of Clubs

Card rank: 3
Card suit: c
Card blackjack value: 3
Card string value: Three of Clubs

Card rank: 4
Card suit: c
Card blackjack value: 4
Card string value: Four of Clubs

Card rank: 5
Card suit: c
Card blackjack value: 5
Card string value: Five of Clubs

Card rank: 6
Card suit: c
Card blackjack value: 6
Card string value: Six of Clubs

Card rank: 7
Card suit: c
Card blackjack value: 7
Card string value: Seven of Clubs

Card rank: 8
Card suit: c
Card blackjack value: 8
Card string value: Eight of Clubs

Card rank: 9
Card suit: c
Card blackjack value: 9
Card string value: Nine of Clubs

Card rank: 10
Card suit: c
Card blackjack value: 10
Card string value: Ten of Clubs

Card rank: 11
Card suit: c
Card blackjack value: 10
Card string value: Jack of Clubs

Card rank: 12
Card suit: c
Card blackjack value: 10
Card string value: Queen of Clubs

Card rank: 13
Card suit: c
Card blackjack value: 10
Card string value: King of Clubs

Card rank: 1
Card suit: h
Card blackjack value: 1
Card string value: Ace of Hearts

Card rank: 2
Card suit: h
Card blackjack value: 2
Card string value: Two of Hearts

Card rank: 3
Card suit: h
Card blackjack value: 3
Card string value: Three of Hearts

Card rank: 4
Card suit: h
Card blackjack value: 4
Card string value: Four of Hearts

Card rank: 5
Card suit: h
Card blackjack value: 5
Card string value: Five of Hearts

Card rank: 6
Card suit: h
Card blackjack value: 6
Card string value: Six of Hearts

Card rank: 7
Card suit: h
Card blackjack value: 7
Card string value: Seven of Hearts

Card rank: 8
Card suit: h
Card blackjack value: 8
Card string value: Eight of Hearts

Card rank: 9
Card suit: h
Card blackjack value: 9
Card string value: Nine of Hearts

Card rank: 10
Card suit: h
Card blackjack value: 10
Card string value: Ten of Hearts

Card rank: 11
Card suit: h
Card blackjack value: 10
Card string value: Jack of Hearts

Card rank: 12
Card suit: h
Card blackjack value: 10
Card string value: Queen of Hearts

Card rank: 13
Card suit: h
Card blackjack value: 10
Card string value: King of Hearts

Card rank: 1
Card suit: s
Card blackjack value: 1
Card string value: Ace of Spades

Card rank: 2
Card suit: s
Card blackjack value: 2
Card string value: Two of Spades

Card rank: 3
Card suit: s
Card blackjack value: 3
Card string value: Three of Spades

Card rank: 4
Card suit: s
Card blackjack value: 4
Card string value: Four of Spades

Card rank: 5
Card suit: s
Card blackjack value: 5
Card string value: Five of Spades

Card rank: 6
Card suit: s
Card blackjack value: 6
Card string value: Six of Spades

Card rank: 7
Card suit: s
Card blackjack value: 7
Card string value: Seven of Spades

Card rank: 8
Card suit: s
Card blackjack value: 8
Card string value: Eight of Spades

Card rank: 9
Card suit: s
Card blackjack value: 9
Card string value: Nine of Spades

Card rank: 10
Card suit: s
Card blackjack value: 10
Card string value: Ten of Spades

Card rank: 11
Card suit: s
Card blackjack value: 10
Card string value: Jack of Spades

Card rank: 12
Card suit: s
Card blackjack value: 10
Card string value: Queen of Spades

Card rank: 13
Card suit: s
Card blackjack value: 10
Card string value: King of Spades


Add only cards with good values to list, range includes several BAD SUITS:

Attempting to create and add rank 1 of a to list
CARD CREATION FAILED: <class 'ValueError'>
Suit should be one of the following: ('d', 'c', 'h', 's')

Attempting to create and add rank 1 of b to list
CARD CREATION FAILED: <class 'ValueError'>
Suit should be one of the following: ('d', 'c', 'h', 's')

Attempting to create and add rank 1 of c to list
Card successfully added to list

Attempting to create and add rank 1 of d to list
Card successfully added to list

---Valid cards in list---

Card rank: 1
Card suit: c
Card blackjack value: 1
Card string value: Ace of Clubs

Card rank: 1
Card suit: d
Card blackjack value: 1
Card string value: Ace of Diamonds


Add only cards with good values to list, range includes several RANKS AND SUITS THAT ARE IN WRONG FORMAT:

Attempting to create and add rank 1 of 1 to list
CARD CREATION FAILED: <class 'TypeError'>
Suit should be a string: ('d', 'c', 'h', 's')

Attempting to create and add rank c of c to list
CARD CREATION FAILED: <class 'TypeError'>
Rank should be an integer

Attempting to create and add rank 1 of 1.83 to list
CARD CREATION FAILED: <class 'TypeError'>
Suit should be a string: ('d', 'c', 'h', 's')

Attempting to create and add rank 1.55 of d to list
CARD CREATION FAILED: <class 'TypeError'>
Rank should be an integer

Attempting to create and add rank 13 of cat to list
CARD CREATION FAILED: <class 'ValueError'>
Suit should be one of the following: ('d', 'c', 'h', 's')

---Valid cards in list---

EMPTY LIST

Process finished with exit code 0
"""


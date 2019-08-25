#tarot something
#https://github.com/dariusk/corpora/blob/master/data/divination/tarot_interpretations.json
import pycorpora # the data for tarot


#actualData = pycorpora.divination.tarot_interpretations['tarot_interpretations']
"""STRUCTURE
fortune_telling
keywords
meanings
    light
    shadow
name
rank
suit
"""

#map card name to index of the card
#
#print(actualData['tarot_interpretations'][0])

"""
class for fortune telling
class for card - model class
class for deck
class for the application
"""

class TarotCard(object):
    """docstring for TarotCard."""

    def __init__(self, dataObj):
        #self.dataObj = dataObj
        self.addData(dataObj);

    def addData(self, dataObj):
        self.fortune_telling = dataObj["fortune_telling"]
        self.keywords = dataObj["keywords"]
        #self.meanings = dataObj["meanings"]
        self.light = dataObj["meanings"]["light"]
        self.shadow = dataObj["meanings"]["shadow"]
        self.name = dataObj["name"]
        self.rank = dataObj["rank"]
        self.suit = dataObj["suit"]

    def print_card(self):
        print("Name : " + self.name)
        print("Suit : " + self.suit)

    def get_fortune():
        ## make a method that will spit out a random fortune

class TarotDeck(object):
    """docstring for TarotDeck."""
    def __init__(self):
        cardData = pycorpora.divination.tarot_interpretations['tarot_interpretations']
        self.cardList = []
        self.build_deck(cardData)

    def build_deck(self, cardData):
        for card in cardData:
            new_card = TarotCard(card)
            self.cardList.append(new_card)

    def top_card(self):
        return self.cardList[0]

    def bottom_card(self):
        return self.cardList[len(self.cardList) - 1]

    #def shuffle(self):

test = TarotDeck()
#test.top_card().print_card()
#print(test.top_card().light)

#fashion

from enum import Enum
from typing import List, Tuple

class Color(Enum):
    RED = 0
    REDVIOLET = 1
    VIOLET = 2
    BLUEVIOLET = 3
    BLUE = 4
    BLUEGREEN = 5
    GREEN = 6
    YELLOWGREEN = 7
    YELLOW = 8
    YELLOWORANGE = 9
    ORANGE = 10
    REDORANGE = 11
    NULL = -1

class ColorMatch(object):

    def __init__(self, color: str) -> None:
        self.colorMap = {"red": Color.RED,
        "red-violet":Color.REDVIOLET,
        "violet":Color.VIOLET,
        "blue-violet":Color.BLUEVIOLET,
        "blue":Color.BLUE,
        "blue-green":Color.BLUEGREEN,
        "green":Color.GREEN,
        "yellow-green":Color.YELLOWGREEN,
        "yellow":Color.YELLOW,
        "yellow-orange":Color.YELLOWORANGE,
        "orange":Color.ORANGE,
        "red-orange":Color.REDORANGE}
        #self.getAdjacent =
        self.init(color)

    def init(self, color: str) -> None:
        self.setColor(color)
        self.getCompliment()
        if(self.color.value == 0 or self.color.value >= 7):
            self.isWarm = True
        else:
            self.isWarm = False

    def setColor(self, color: str) -> None:
        self.color = self.colorMap[color]

    def getCompliment(self) -> None:
        value = self.color.value
        self.compliment = Color((value + 6) % 11)

class Piece(object):
    """A Piece is an article of clothing."""

    def __init__(self, definition: dict) -> None:
        self.type = definition["type"] # top / bottom / shoe
        self.name = definition["name"]
        self.p_color_match = self.getColorMatch(definition["p_color"])
        #self.s_color_match = self.getColorMatch(definition.s_color)
        #self.fit = definition.fit #loose or tight

    def getColorMatch(self, color: str) -> ColorMatch:
        return ColorMatch(color)

class Style(object):

    def __init__(self):
        self.dict = {}
        self.fill()

    def fill(self) -> None:
        #self.dict["styleNme"] = {"pieces": {"tops": [""], "bottoms": [""], dresses": [""], "shoes": [""]}, "colors": []}
        self.dict["BuisnessCasual"] = {"pieces": {"tops": ["blouse", "button-down", "polo-shirt"], "bottoms": ["pants", "jeans", "khakis", "skirt"], "shoes": ["loafers", "pumps", "booties", "flats"], "dresses": [""]}, "colors": [""]}
        self.dict["Buisness"] = {"pieces": {"tops": ["button-down", "blouse"], "bottoms": ["pencil-skirt", "slacks", "pants"], "dresses": [""], "shoes": ["pumps", "heels", "wing-tips", "dress-shoe", "oxfords", "loafers"]}, "colors": []}
        self.dict["Casual"] = {"pieces": {"tops": ["t-shirt", "graphic-tee", ], "bottoms": ["shorts", "jeans", "printed-pants", "leggings"], "dresses": ["maxi"], "shoes": ["sneakers", "sandals"]}, "colors": []}
        self.dict["Emo"] = {"pieces": {"tops": ["graphic-tee", "printed-tee"], "bottoms": ["jeans", "ripped-jeans"], "dresses": [""], "shoes": ["boots", "sneakers", "platforms"]}, "colors": ["black"]}

    def getStyleDef(self, name: str) -> dict:
        try:
            return self.dict[name]
        except Exception as e:
            return {"error": "Key does not exist : " + name}

class Outfit(object):

    def __init__(self, pieces: List):
        """ need a style, and at least 2 pieces (shoes-dress)/(top-bottom-shoes)  """
        self.pieces = pieces

    def fitsStyle(self, styleDef: dict) -> bool:
        isMatch = True
        for item in pieces:
            name = item.name
            type = item.type

            if type is 'top':
                tops = styleDef["pieces"]["tops"]
                if name not in tops:
                    print(name + " : " + str(tops))
                    return False

            if type is 'bottom':
                bottoms = styleDef["pieces"]["bottoms"]
                if name not in bottoms:
                    print(name + " : " + str(bottoms))
                    return False

            if type is 'shoe':
                shoes = styleDef["pieces"]["shoes"]
                if name not in shoes:
                    print(name + " : " + str(shoes))
                    return False

        return isMatch

#test = ColorMatch('blue')
#print(test.isWarm)


dress = {"type": "dress", "name": "maxi", "p_color": "red", "s_color": ""}
shirt = {"type": "top", "name": "blouse", "p_color":"yellow", "s_color":""}
tee = {"type": "top", "name": "t-shirt", "p_color":"yellow", "s_color":""}
jean = {"type": "bottom", "name": "jeans", "p_color":"blue", "s_color":""}

heels = {"type": "shoe", "name": "heel", "p_color":"blue", "s_color":"green"}
sneakers = {"type": "shoe", "name": "sneakers", "p_color":"red", "s_color":""}

top_piece = Piece(tee)
bottom = Piece(jean)
shoes = Piece(sneakers)

pieces = [top_piece, bottom, shoes]

style = Style()
casual = style.getStyleDef("Casual")
#print(casual)

outfit = Outfit(pieces)

print(outfit.fitsStyle(casual))

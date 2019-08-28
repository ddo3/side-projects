#pipes
from typing import List, Tuple

class Grid(object):

    def __init__(self, size: int):
        self.size = size
        #self.matrix = []
        self.init()

    def init(self) -> None:
        mat = []
        for i in range(0, self.size):
            row = []
            for j in range(0, self.size):
                row.append('_')
            mat.append(row)

        self.matrix = mat

    def getChar(self, row: int, col: int) -> str:
        return self.matrix[row][col]

    #def getRow(self, row: int) -> list:
        #return self.matrix

    def printGrid(self) -> None:
        for i in range(0, self.size):
            print(self.matrix[i])
            #for j in range(0, self.size):

    def stringRow(self, row:list):
        print("._____._____._____.\n|     |     |     |\n|  2  |  2  |  2  |\n._____._____._____.")
        #print("|     |     |     |")
        #print("|  2  |  2  |  2  |")
        #print("|     |     |     |")
        #print("._____._____._____.")


"""
class GameBoard(object):
    def __init__(self):
        #super(GameBoard, self).__init__()"""


test = Grid(4)
#test.printGrid()
test.stringRow([])

# markov chains
import json

class Word(object):
    """docstring for Word."""

    def __init__(self, word: str):
        self.arg = arg
        self.followingWordDict = {}
        self.word = word

    def get(self) -> str:
        return self.word

    def getFollowingWords(self) -> dict:
        return self.followingWordDict

    def addWord(self, followingWord: str) -> None:
        keyFound = False
        for key in self.followingWordDict:
            if followingWord == key:
                self.followingWordDict[key] == self.followingWordDict + 1
                keyFound = True

        if keyFound == False:
            self.followingWordDict[followingWord] = 1

    def toJson(self) -> dict:
        return { self.word : self.followingWordDict}

class MakeMarkovChain(object):
    """docstring for MakeMarkovChain."""

    def __init__(self, filename: str):
        self.arg = arg
        self.words = []
        self.readFile(fileName);


    def readFile(self, filename: str) -> None:
        file = open('alice-chain.txt', 'r')
        data = file.readLines()
        badChars = ["'", `"`, ".", ",", ";", ":", "(", ")", "&", "!"]
        for line in data:
            newLine = line
            for c in badChars:
                newLine = newLine.replace(c, "")

            wordList = newLine.split(" ")

            for index in range(0, len(wordList)):
                currentWord = wordList[index]


                for encounteredWord in self.words:
                    if encounteredWord.get() == word:
                        encounteredWord.


    def writeDictToFile(self) -> None:
        var jsonList = []
        for word in self.words:
            jsonList.append(word.toJson())

        with open('alice-chain.txt', 'w') as outfile:
            json.dump({'data': jsonList}, outfile)


"""
TODO turn textfile into single line 
"""

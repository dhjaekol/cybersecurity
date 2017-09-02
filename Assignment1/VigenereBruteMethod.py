import collections


class VigenereBruteMethod:
    _cipher = ""

    def __init__(self, cipherText):
        self._cipher = cipherText

    @staticmethod
    def runmethod():
        keywords = []
        with open("words.txt") as f:
            for line in f:
                line = line.replace('\n','')
                if len(line) == 5:
                    keywords.append(line)

        letterDict = {'A': 0, 'B': 1, 'C': 2, 'D' : 3, 'E': 4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, }

import collections

class VigenereBruteMethod:
    _cipher = ""

    def __init__(self, cipherText):
        self._cipher = cipherText

    def RunMethod(self):
        keywords = []
        with open("words.txt") as f:
            for line in f:
                line = line.replace('\n','')
                if len(line) == 5:
                    keywords.append(line)
        print(len(keywords))
        print(keywords)
        
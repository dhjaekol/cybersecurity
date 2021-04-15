import collections

class SubstitutionMethod:
    _cipher = ""
    
    def __init__(self, cipherText):
        self._cipher = cipherText

    def runMethod(self):
        
        cipher1 = self._cipher
        
        letterFreq = [["A", 8.2], ["B", 1.5], ["C", 2.8], ["D", 4.2], ["E", 12.7], ["F", 2.2],
                      ["G", 2.0], ["H", 6.1], ["I", 7.0], ["J", 0.1], ["K", 0.8], ["L", 4.0], ["M", 2.4],
                      ["N", 6.7], ["O", 7.5], ["P", 1.9], ["Q", 0.1], ["R", 6.0], ["S", 6.3], ["T", 9.0],
                      ["U", 2.8], ["V", 1.0], ["W", 2.4], ["X", 0.1], ["Y", 2.0], ["Z", 0.1], ]

        englishLetterDist = sorted(letterFreq, key=lambda x:x[1], reverse=True)

        englishBigramDist = [["TH", 3.15], ["AN", 1.72], ["ER", 1.54], ["ES", 1.45], ["EA", 1.31], ["AT", 1.24],
                      ["EN", 1.20], ["HE", 2.51], ["IN", 1.69], ["RE", 1.48], ["ON", 1.45], ["TI", 1.28], ["ST", 1.21],
                      ["ND", 1.18]]

        englishTrigramDist = [["THE", 0], ["ING", 1], ["AND", 2], ["HER", 3], ["ERE", 4], ["ENT", 5], ["THA", 6], ["NTH", 7],
                       ["WAS", 8], ["ETH", 9], ["FOR", 10]]

        # build bigram list
        bigramList = []
        i = 0
        for c in cipher1:
            if i == 0:
                firstChar = c
                i += 1
            else:
                bigram = firstChar + c
                bigramList.append(bigram)
                i = 0

        # build trigram list
        trigramList = []
        i = 0
        for c in cipher1:
            if i == 0:
                firstChar = c
                i += 1
            elif i == 1:
                secondChar = c
                i += 1
            else:
                trigram = firstChar + secondChar + c
                trigramList.append(trigram)
                i = 0

        #------------------------------------------------------------------------------------------------------------------
        #  Decrpypt cipher1
        # -----------------------------------------------------------------------------------------------------------------

        #   Letter distribution
        # 97-122 - a-z
        i = 97
        singleLetters = []
        while i < 123:
            letter = chr(i)
            letterCount = cipher1.count(letter)
            singleLetters.append([letter, letterCount])
            i += 1

        # Bigram distrubition
        totalLetterCount = len(cipher1)

        for c in singleLetters:
            c[1] = round(c[1] / totalLetterCount * 100,1)

        # Sort lists
        cipherLetterDist = sorted(singleLetters, key=lambda x:x[1], reverse=True)
        bigramDist = sorted(list(collections.Counter(bigramList).items()), key=lambda x:x[1], reverse=True)
        trigramDist = sorted(list(collections.Counter(trigramList).items()), key=lambda x:x[1], reverse=True)

        file = open("decrypt.txt", "w")
        file.write("Single letters")
        file.write("\n")
        file.write(str(cipherLetterDist))
        file.write("\n")
        file.write(str(englishLetterDist))
        file.write("\n")
        file.write("\n")

        file.write("Bigrams in cipher")
        file.write("\n")
        file.write(str(bigramDist))
        file.write("\n")
        file.write(str(englishBigramDist))
        file.write("\n")
        file.write("\n")

        file.write("Trigrams in cipher")
        file.write("\n")
        file.write(str(trigramDist))
        file.write("\n")
        file.write(str(englishTrigramDist))
        file.write("\n")
        file.write("\n")

        # first try
        # decrpytDict = {'t': 'E'}
        # decrpytDict.update({'p': 'N'})
        # decrpytDict.update({'j': 'T'})
        # decrpytDict.update({'g': 'H'})
        # decrpytDict.update({'o': 'A'})
        # decrpytDict.update({'a': 'R'})
        # decrpytDict.update({'z': 'D'})
        # decrpytDict.update({'c': 'I'})
        # decrpytDict.update({'r': 'O'})
        # decrpytDict.update({'n': 'S'})
        # decrpytDict.update({'l': 'G'})
        # decrpytDict.update({'m': 'D'})
        # decrpytDict.update({'a': 'R'})

        # second try
        # decrpytDict      = {'t': 'E'}
        # decrpytDict.update({'p': 'N'})
        # decrpytDict.update({'j': 'T'})
        # decrpytDict.update({'o': 'A'})
        # decrpytDict.update({'c': 'O'})
        # decrpytDict.update({'r': 'I'})
        # decrpytDict.update({'n': 'S'})
        # decrpytDict.update({'g': 'H'})
        # decrpytDict.update({'a': 'R'})
        # decrpytDict.update({'z': 'D'})

        # third try
        decrpytDict      = {'t': 'E'}
        decrpytDict.update({'p': 'N'})
        decrpytDict.update({'j': 'T'})
        decrpytDict.update({'o': 'I'})
        decrpytDict.update({'c': 'O'})
        decrpytDict.update({'r': 'A'})
        decrpytDict.update({'n': 'S'})
        decrpytDict.update({'g': 'H'})
        decrpytDict.update({'a': 'R'})
        decrpytDict.update({'z': 'G'})
        decrpytDict.update({'y': 'V'})
        decrpytDict.update({'i': 'Y'})
        decrpytDict.update({'d': 'U'})
        decrpytDict.update({'e': 'B'})
        decrpytDict.update({'m': 'D'})
        decrpytDict.update({'q': 'L'})
        decrpytDict.update({'h': 'C'})
        decrpytDict.update({'s': 'K'})
        decrpytDict.update({'k': 'W'})
        decrpytDict.update({'f': 'F'})
        decrpytDict.update({'l': 'P'})
        decrpytDict.update({'u': 'X'})
        decrpytDict.update({'w': 'M'})
        decrpytDict.update({'x': 'J'})
        decrpytDict.update({'b': 'Q'})

        # decrpytDict.update({'p': 'N'})
        # decrpytDict.update({'j': 'A'})
        # decrpytDict.update({'c': 'I'})

        # print (decrpytDict)

        file.write("Decrpyt dictionary")
        file.write("\n")

        file.write(str(decrpytDict))
        file.write("\n")
        file.write("\n")

        # decrypt message
        decryptMsg = []
        for c in cipher1:
            if c in decrpytDict:
                value = decrpytDict[c]
                decryptMsg.append(value)
            else:
                decryptMsg.append("_")

        file.write("Decryption")
        file.write("\n")
        file.write(cipher1)
        file.write("\n")
        file.write(''.join(decryptMsg))

        file.close()

        print("Decryption for problem 1: ")
        #print(cipher1)
        print(''.join(decryptMsg))

        #   Find trigram that starts or ends with letter E
        #   Build dictionaries of matches'
        #   Translate cipher

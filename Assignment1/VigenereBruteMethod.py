import collections

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class VigenereBruteMethod:
    _cipher = ""

    def __init__(self, cipherText):
        self._cipher = cipherText

    def runMethod(self):
        cipher = self._cipher

        keywords = []
        with open("words.txt") as f:
            for line in f:
                line = line.replace('\n','')
                line = line.replace('\r', '')
                # since we know the length of the keyword we can only use 5 letter words
                if len(line) == 5:
                    keywords.append(line)

        file = open("decrypt.txt", "w")

        # keyword is goofy!
        keywords = []
        keywords.append("goofy")

        for keyword in keywords:
            goodKeyword = 1

            for letter in keyword:
                # 97-122 - a-z
                # 65-90 - A-Z
                if (ord(letter) >= 97 and ord(letter) <= 122 ) or (ord(letter) >= 65 and ord(letter) <= 90):
                    continue
                else:
                    goodKeyword = 0
                    break

            if goodKeyword == 1:
                decrypedMessage = self.translateMessage(keyword, cipher)
                # First try - only look at translations where first 5 letters of a word contain a vowel or Y
                for letter in decrypedMessage[:5]:
                    if letter in ('a','e','i','o','u','y'):
                        message = keyword + "\t" + decrypedMessage   + "\n"
                        file.write(message)
                        break
                # print(message)

        file.close()

    # derived from http://inventwithpython.com/vigenereCipher.py
    def translateMessage(self, key, message):
        translated = [] # stores the encrypted/decrypted message string

        keyIndex = 0
        key = key.upper()

        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS

                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
                num %= len(LETTERS) # handle the potential wrap-around

                # add the encrypted/decrypted symbol to the end of translated.
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # The symbol was not in LETTERS, so add it to translated as is.
                translated.append(symbol)

        return ''.join(translated)
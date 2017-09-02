class ShiftMethod:
    cipher1 = ""

    def __init__(self, cipherText):
        self.cipher1 = cipherText

    def RunMethod(self):
        file = open("decrypt.txt", "w")
        file.write(self.cipher1)
        file.write("\n")
        i = 1
        while i < 26:
            # 97-122 - a-z
            file.write("Shift: " + str(i))
            file.write("\n")
            decrpytedText = []
            for c in self.cipher1:
                try:
                    charValue = ord(c)
                    shiftChar = charValue + i
                    if shiftChar > 122:
                        shiftChar = shiftChar - 26
                    decrpytedText.append(chr(shiftChar))
                except:
                    print("Unexpected error:")
                    raise
            for item in decrpytedText:
                file.write("%s" % item)
            file.write("\n")
            i += 1
        file.close
        #print(self.cipher1)
        #print(ord('a'))
        #print(chr(97))
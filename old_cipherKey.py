# Name: Natalie Lim Kit Ee
# ID: 2201845
# Class: DAAA/2B/03

from encryptDecrypt import CeasarCipher

class CipherKey:
    def __init__(self, message, referenceFile): 
        self.__message = message #keep message and reference file private to prevent others from finding out the secret message
        self.__ref = referenceFile

    def inferKey(self):
        bestKey = None
        minDiff = float('inf')  #a very large number so that diff < minDiff

        for key in range(26):
            decrypt = CeasarCipher(self.__message, key)
            decryptedText = decrypt.solveCipher()

            #count letters in decryptedText, set missing letters to 0
            decryptedLetterCount = {char: decryptedText.count(char) if char.isalpha() else 0 for char in self.__ref.keys()}        

            #count diff (btw observed & expected freq) for each key
            diff = self.compareExpectedFreq(decryptedLetterCount, self.__ref)

            #save value of smallest diff
            if diff < minDiff:
                bestKey = key
                minDiff = diff
        return bestKey

    def compareExpectedFreq(self, decryptedLetterCount, referenceFile):
        total_letters = sum(decryptedLetterCount.values())
        observed_frequencies = {char: count / total_letters * 100 for char, count in decryptedLetterCount.items()}

        #calcualte absolute values of diff (btw observed & expected freq) for each letter
        diffs = {char: abs(observed_frequencies[char] - expected) for char, expected in referenceFile.items()}

        #sum differences
        totalDiff = sum(diffs.values())
        return totalDiff
  
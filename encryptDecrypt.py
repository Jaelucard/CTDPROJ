#encryption and decryption functions for Enigma, Ceasar and Rail Fence Cipher
class Cipher:
    def __init__(self, message):
        self.__message = message

class EnigmaCipher(Cipher):
    def __innit__(self, message, m, c):
        super().__init__(message)
        self.__m = m
        self.__c = c

    def encryptEnigma(self):
        pass

    def decryptEnigma(self):
        pass

class CeasarCipher(Cipher):
    def __init__(self, message, shift, endecrypt='D'): #function overloading and assign endecrypt to D for options that just require decryption
        super().__init__(message) #keep message and shift private to prevent others from finding out the secret message
        self.__shift = shift
        self.endecrypt = endecrypt
  
    def solveCipher(self):
        decoded_text = ''
        shift = int(self.__shift)
        for letter in self._Cipher__message:
            if letter.isalpha():
                upper=0
                if letter.isupper():
                    upper=1 
                    letter=letter.lower()
                if self.endecrypt == 'E':
                    alphaform = chr(((ord(letter) + shift -97) % 26) + 97)
                else:
                    alphaform = chr(((ord(letter) - shift -97) % 26) + 97)

                if upper==1:
                    alphaform = alphaform.upper()
            else:
                alphaform = letter
            decoded_text = decoded_text + alphaform
        return decoded_text

class RailFenceCipher(Cipher):
    def __init__(self, message, railNum): #hide message & rail number to avoid others from deciphering message
        super().__init__(message)
        self.__railNum = railNum

    def encryptRailFence(self):
        #create list as fence
        fence = [['' for i in range(1)] for i in range(self.__railNum)] #only need one column since append letters to first column value only

        #initialise rail number (rail) & value to check if at first/last rail and need to change direction(updown)
        rail, updown = 0, 1

        for char in self._Cipher__message:
            fence[rail][0] += char
            rail += updown #go to next rail for next letter

            #change direction of zigzag when reach the first/last row
            if rail == 0 or rail == self.__railNum - 1:
                updown = -updown

        #join combine all rows into a 1D list -> joing 1D list to a string where values separated by ' '
        encrypted_text = ' '.join([''.join(row) for row in fence])
        return encrypted_text


    def decryptRailFence(self):
        #create list as fence (place letters into position on fence later)
        fence = [[' ' for _ in range(len(self._Cipher__message))] for _ in range(self.__railNum)]

        #initialise rail number (rail) & value to check if at first/last rail and need to change direction(updown)
        rail, updown = 0, 1

        #i indicates continually moving to next column
        for i in range(len(self._Cipher__message)):
            fence[rail][i] = '*' #place * for every position a letter would be
            rail += updown #go to next rail for next letter

            #change direction of zigzag when reach the first/last row (updown = 1(next row - go down 1)/-1(next row - go up 1))
            if rail == 0 or rail == self.__railNum - 1:
                updown = -updown

        #replacing * with corresponding letter in fence
        charNum = 0
        for i in range(self.__railNum): #iterate through every position in list
            for j in range(len(self._Cipher__message)):
                if fence[i][j] == '*' and charNum < len(self._Cipher__message): #find next *
                    fence[i][j] = self._Cipher__message[charNum] #replace * with letter
                    charNum += 1

        rail, updown = 0, 1
        decryptedText = ''
        #move up and down rows in fence to retrive values and append to decryptedText
        for i in range(len(self._Cipher__message)):
            decryptedText += fence[rail][i] #add letter to decryptedText
            rail += updown

            #change direction of zigzag when reach the first/last row (updown = 1(next row - go down 1)/-1(next row - go up 1))
            if rail == 0 or rail == self.__railNum - 1:
                updown = -updown

        return decryptedText

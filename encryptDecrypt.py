#encryption and decryption functions for Enigma, Ceasar and Rail Fence Cipher
import copy
class Cipher:
    def __init__(self, message):
        self.__message = message

class EnigmaCipher(Cipher):
    def __init__(self, message, m, c, endecrypt, alphabet): #hide message, m, c and alphabet to avoid others from deciphering message
        super().__init__(message)
        self.__m = m
        self.__c = c
        self.__endecrypt = endecrypt
        self.__alphabet = alphabet
    @property #zahin's edit
    def m(self): #zahin's edit - getter for m
        return self.__m
    @property #zahin's edit
    def c(self): #zahin's edit - getter for c
        return self.__c
    
    def encryptEnigma(self, choice):#zahin's edit - choice is included so that the function won't print the encryption details when in-game.
        #create new dictionary to save shifted alphabet which is shifted by (mx + c mod 21)
        shifted_alphabet = copy.deepcopy(self.__alphabet)
        if self.__endecrypt == 1: #shift alphabet for encryption
            if self.__m not in [1,2,4,5,8,10,11,13,16,17,19,20]:
                raise ValueError
            for key, value in self.__alphabet.items():
                shifted_alphabet[(self.__m * key + self.__c) % 21] = self.__alphabet[key]
            
            #show user how the shift has occurred
            if choice != '4': #zahin's edit - details won't be printed in-game
                print("Original Alphabet:")
                print(self.__alphabet)
                print("     |       |       |       |       |       |       |       |       |       |        |        |        |        |        |        |        |        |        |        |        |")
                print(shifted_alphabet)
                print("^ Shifted Alphabet ^")

        else: #shift alphabet for decryption
            modular_inverse_m = pow(self.__m, -1, 21)  #modular inverse always exists since m is coprime with 21

            for key, value in self.__alphabet.items():
                # Reverse the shift applied during encryption
                original_key = (modular_inverse_m * (key - self.__c)) % 21
                shifted_alphabet[original_key] = value
            #shift of letters cannot be shown for decryption as unknown number of times the shift has been applied

        #put together the encoded/decoded message
        text = self._Cipher__message[0] #keep first letter
        for letter in self._Cipher__message[1:-1]:
            if letter.isalpha(): #only shift letters
                upper=0
                if letter.isupper():
                    upper=1 #"save" the fact that the letter is uppercase
                    letter=letter.lower()

                if letter not in ['a','e','i','o','u']: #ignore vowels
                    key = next(k for k, v in self.__alphabet.items() if v == letter) #get the key of the letter in the alphabet dictionary
                    new_letter = shifted_alphabet.get(key) #get the shifted letter from the shifted alphabet dictionary
                    if upper==1:
                        text += new_letter.upper() #keep letter uppercase
                    else:
                        text += new_letter
                else:
                    if upper==1:
                        text += letter.upper() #keep vowel uppercase
                    else:
                        text += letter #keep vowels
            else:
                text += letter #keep non-letters
        text += self._Cipher__message[-1] #keep last letter
        if choice != '4': #zahin's edit - shifted alphabet will not be shown in-game
            return text, self.__alphabet,shifted_alphabet
        elif choice == '4': #zahin's edit - only encrypted message will be shown in-game
            return text
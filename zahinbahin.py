#List of variables:
"""Mode (1 or 2)
Levels 1 - 6 (progress)
Score
FailCounter 1(1 to 2) - inner question layer
FailCounter 2(1 to 2) - outer game layer
Time
Cipher
Cipher2
Answer
Encrypted
Encrypted2
Question Weightage List
List of Answers"""
import random 
from encryptDecrypt import EnigmaCipher as enig
''' - example for class creation
class EnigmaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Puzzle Game")
        self.level = 1
        self.score = 0
        self.hints_used = 0
        self.remaining_attempts = 2
        self.current_step = 1
        self.cipher = {}
        self.secret_message = ""
        self.encoded_message = ""
        self.scrambled_word = ""
        self.math_problem = ""
        self.math_solution = 0
        '''
#"Game" mode is selected
#Dictionary of 12 answers

band_dict = {'answer1':'band1', 
             'answer2':'band2', 
             'answer3':'band3', 
             'answer4':'band4', 
             'answer5':'band5', 
             'answer6':'band6', 
             'answer7':'band7', 
             'answer8':'band8', 
             'answer9':'band9', 
             'answer10':'band10', 
             'answer11':'band11', 
             'answer12':'band12'}

#--------------------LIST OF FUNCTIONS------------------------------------
class GameFunction:
    def __init__(self):

        #function to randomly pick from the dictionary [joseph side]
        #function to randomise the cipher??? [joseph side]

        #function to calculate score for each question
        def calculate_award(modechoice, remaining_time):
            if modechoice == '1':
                default_score = 10
            elif modechoice == '2':
                default_score = 20
            pointsgiven = (remaining_time/60)*default_score
            return pointsgiven
        #function to add score for each question
        def addscore(pointsgiven, score):
            score = score + pointsgiven
            return score
        
        #function encrypter
    def encrypter(message, m, c):
    #link to natalie&shannon's code
        alphabet = {
        0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
        8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
        15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
                   }
        cipher = enig(message, m, c, endecrypt=1, alphabet=alphabet)
        encrypted_message = cipher.encryptEnigma('4')
        print(f"\nEncrypted Message: {encrypted_message}")
        print(f"\nEncryption Cipher: {cipher.m}*key+{cipher.c}")

        #submit function: compare user input to answer
        def submit(userinput):
            if userinput == answer:
                return 1
            else: 
                return 0
            '''
        def failcheck_layer1(x):
        def failcheck_layer2(y):
            if y == 2: 

        #function to check answer 
        #function to accumulate points (joseph)
        #function for failcheck layer 1 
        #function for failcheck layer 2
        #function for hint button - subtracts time from timer (joseph)
        #Select Easy vs Hard mode
        print('\nPlease select your choice: 1, 2)')
        print('\tEasy')
        print('\tHard')
        modechoice = input('Enter choice: ')
        if modechoice == '1':
            print('Easy mode has been selected') 
            #running a function to pick a random answer
            (PickRandomAnswerFunction - joseph)
            #running a function to select a random cipher
            (PickRandomCipher - joseph)
            #answer obtained, running a function to encrypt the answer, returns "Encrypted" - input 
            #user sees Encrypted, waiting on input
            #user inputs answer
            #running a check function
        elif modechoice == '2':
            print('Hard mode has been selected')
            #running a function to pick a random answer
            #running a function to select a random cipher
            #answer obtained, running a function to encrypt the answer, returns "Encrypted"
            #running a function to select a 2nd random cipher
            #running a function to encrypt "Encrypted", returns "Encrypted2"
            #user sees Encrypted2, waiting on input
            #user inputs answer
            #running a check function
'''
print(GameFunction.encrypter('hello there joseph', 3, 11))
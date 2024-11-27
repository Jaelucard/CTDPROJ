import tkinter as tk
import random
from encryptDecrypt import EnigmaCipher as enig
from validation import Validation as val

class RunProgramme:
    def start(self):
        print('\nWelcome to the Enigma Puzzle Game!')
        while True: #continually ask until exit)
            print('\nPlease select your choice: (1,2,3,4,5,6,7,8)')
            print('\t1. Encrypt Message')
            print('\t2. Decrypt Message')
            print('\t3. Exit')
            choice = input('Enter choice: ').replace(" ", "") #remove whitespace characters

#------------------------------------------------- CHOICES -------------------------------------------------#
            #CHOICE 1/2: ENCRYPT MESSAGE OR DECRYPT MESSAGE
            if choice == '1' or choice == '2':
                #getting user input
                message = input("\nWhat is your message? ")

                #print instructions for user
                print("\nPlease input a linear function for your encryption!\nA linear function takes the form of mx + c, where m is the number of times we split the list and c is the translation to the left or right.")
                if choice == '2':
                    print("During decryption, please input the linear function values in reverse order compared to how they were entered during encryption.")
                    print("For example,\n    if message -> function 1 -> encrypted_once -> function 2 -> encrypted_twice -> ..., \n      enter: function 2 then function 1")

                #validate inputs for m and c
                gradientvalue = val.get_integer_input("Input a value for m: ",'m')
                interceptvalue = val.get_integer_input("Input a value for c: ",'c')
                print(f"This is your function: {gradientvalue}x + {interceptvalue}")

                #encrypt message
                if choice == '1':
                    message = enig(message, gradientvalue, interceptvalue).encryptEnigma()
                    print(f"\nYour encrypted message is: {message}")

                #decrypt message
                else:
                    message = enig(message, gradientvalue, interceptvalue).decryptEnigma()
                    print(f"\nYour decrypted message is: {message}")

            #CHOICE 3: EXIT
            elif choice == '3':
                print('Goodbye! Have a good day!\n')
                break

            #INVALID CHOICE
            else:
                print('Invalid choice. Please try again.')

run = RunProgramme()
run.start()

class EnigmaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Puzzle Game")
        self.level = 1
        self.score = 0
        self.hints_used = 0
        self.remaining_attempts = 3
        self.current_step = 1
        self.cipher = {}
        self.secret_message = ""
        self.encoded_message = ""
        self.scrambled_word = ""
        self.math_problem = ""
        self.math_solution = 0
        
    
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
                print("--------------------------USER GUIDE--------------------------")
                print("A linear function takes the form of mx + c, where m is the number of times we split the list and c is the translation to the left or right.")
                print("Please note the vowels and first and last letters of the message will not be encrypted.")

                #getting user input
                message = input("\nWhat is your message? ")

                #print instructions for user
                print("\nPlease input a linear function for your encryption!")
                if choice == '2':
                    print("During decryption, please input the linear function values in reverse order compared to how they were entered during encryption.")
                    print("For example,\n    if message -> function 1 -> encrypted_once -> function 2 -> encrypted_twice -> ..., \n      enter: function 2 then function 1")

                
                #initial alphabet without vowels
                alphabet = {
                    0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
                    8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
                    15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
                }

                while True:
                    #validate inputs for m and c
                    gradientvalue = val.get_integer_input("Input a value for m: ",'m')
                    interceptvalue = val.get_integer_input("Input a value for c: ",'c')
                    if choice == '1':
                        if interceptvalue >= 0:
                            print(f"This is your function: {gradientvalue}x + {interceptvalue}")
                        else:
                            print(f"This is your function: {gradientvalue}x - {-interceptvalue}")
                    else:
                        if interceptvalue >= 0:
                            print(f"This is your function: {gradientvalue}x + {interceptvalue}")
                        else:
                            print(f"This is your function: {gradientvalue}x - {-interceptvalue}")


                    #encrypt/decrypt message
                    message, shifted_alphabet = enig(message, gradientvalue, interceptvalue, endecrypt = int(choice), alphabet = alphabet).encryptEnigma()
                    alphabet = shifted_alphabet #update alphabet
                    if choice == '1':
                        print(f"\nYour encrypted message is: {message}")
                    else:
                        print(f"\nYour decrypted message is: {message}")

                    #does the message have multiple layers to encrypt/decrypt?
                    while True:
                        another = input("Would you like to encrypt the message again? (Y/N) ").strip().upper()
                        if another in {"Y", "N"}:
                            break 
                        print("Invalid input. Please enter 'Y' or 'N'.")

                    if another == "N":
                        break 
                
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
        
    
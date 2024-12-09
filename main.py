import tkinter as tk
import random
import time
from encryptDecrypt import EnigmaCipher as enig
from validation import Validation as val
from zahinbahin import GameFunction as game
from UI import UI as ui
class RunProgramme:
    def start(self):
        print('\nWelcome to the Enigma Puzzle Game!')
        while True: #continually ask until exit)
            print('\nPlease select your choice: 1,2,3,4')
            print('\t1. Encrypt Message')
            print('\t2. Decrypt Message')
            print('\t3. Exit')
            print('\t4. Game')
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
            #CHOICE 4: GAME
            elif choice == '4':
                print('Initializing Puzzle Game...')
                print('\nInstructions: Solve all 6 puzzles within the time limit to win! 60 seconds will be given for each question.')
                print('\nInstructions: Points will be awarded based on how fast you solve the question! Hard mode is tougher but gives twice the points!')
                print('\nInstructions: You can ask for a hint, but youll have time deducted!')

                modechoice = 0
                while modechoice == 0:
                    modechoice = game.get_user_choice()
                
                if modechoice == '1' or modechoice == '2':
                    band_dict = {'die with a smile':'bruno mars', 
                    'rolling in the deep':'adele', 
                    'love story':'taylor swift', 
                    'all i want for christmas is you':'mariah carey', 
                    'treasure':'bruno mars', 
                    'im yours':'jason mraz', 
                    'answer7':'band7', 
                    'answer8':'band8', 
                    'answer9':'band9', 
                    'answer10':'band10', 
                    'answer11':'band11', 
                    'answer12':'band12'}
                    failcheck1 = 0 #when failchecklayer1 == 2, increase failchecklayer2 by 1
                    failcheck2 = 0 #when failchecklayer2 == 2, trigger gameover function
                    progress = 0 #when progress reaches 6, trigger win function
                    accumulated_points = 0
                    remaining_time = 60   #run jarrod's timer function - when timer hits 0, increase failcheck1 by 1
                    hints_used = 0
                    answer = ''
                    resetbutton = 0
                    hintbutton = 0
                    while True: 
                        if modechoice == '1':
                            print("\n------------------------")
                            print("Mode Selected:  Easy\n")
                            if failcheck1 != 1:
                                answer = game.word_pick_random(band_dict)  #run joseph's random selector function
                                cipher = game.cipher_random() #run joseph's random cipher function
                            encryptmessage = game.encrypter(answer[0], cipher[0], cipher[1])
                            print(f"Encryption Cipher: {cipher[0]}*key+{cipher[1]}")
                            print(f"\nEncrypted Message: {encryptmessage}")
                            print("------------------------")

                        else: #hard mode selected
                            print("\n------------------------")
                            print("Mode Selected: Hard\n")
                            if failcheck1 != 1:
                                answer = game.word_pick_random(band_dict)  #run joseph's random selector function
                                cipher = game.cipher_random() #run joseph's random cipher function
                            encryptmessage = game.encrypter(answer[0], cipher[0], cipher[1])
                            print(f"Encryption Cipher 1: {cipher[0]}*key+{cipher[1]}")
                            cipher = game.cipher_random() #generate a second random cipher
                            encrypt2message = game.encrypter(encryptmessage, cipher[0], cipher[1])
                            print(f"Encryption Cipher 2: {cipher[0]}*key+{cipher[1]}")
                            print(f"\nEncrypted Message: {encrypt2message}")
                            print("------------------------")

                        userinputPlaceholder = input('Your Answer:')
                        #JARROD TO LINK SUBMIT BUTTON TO THIS:
                        if game.submit(userinputPlaceholder, answer[0]) == 1: #if user answer is correct
                            progress += 1
                            failcheck1 = 0
                            accumulated_points = accumulated_points + game.calculate_award(modechoice, remaining_time) #LINK TO JARRODS REMAINING TIME
                            if progress >= 6: #if user has correctly answered 6 questions
                                print("Congratulations! You've beat the game!")
                                print(f"\nYou scored {accumulated_points}!")
                                print(f"\nYou used {hints_used} hints.")
                                time.sleep(1)
                                break
                            else: #if user hasn't correctly answered 6 questions - game moves on to next question: new answer and cipher is run.
                                print("Good job you guessed it right!")
                                print(f"\nPoints scored: {accumulated_points}")
                                print(f"\nYou used {hints_used} hints.")
                        else: #if user answer is wrong
                            if failcheck1 == 1: #if user has failed a question twice
                                if failcheck2 == 1: #if user has LOST 2 questions twice
                                    print("You lost. Nice try")
                                    print(f"\nYou scored {accumulated_points} points. Try again?")
                                    print(f"\nYou used {hints_used} hints.")
                                    time.sleep(1)
                                    break
                                else: 
                                    failcheck2 += 1 #user has now LOST a question
                                    failcheck1 = 0 #resets failcheck1 to 0 as now the user is on a new question
 
                            else: #this checks if failcheck1 is 0 or 1, #user has not lost a question yet 
                                failcheck1 += 1
                                print("Try again, you have one more chance for this question!")
                                print(f"\nPoints scored: {accumulated_points}")
                        #JARROD TO LINK RESET BUTTON TO TRIGGER THIS
                        if resetbutton == 1:
                            progress = 0
                            failcheck1 = 0
                            failcheck2 = 0
                            accumulated_points = 0
                            hints_used = 0
                            answer = ''
                        #JARROD TO LINKK HINT BUTTON TO TRIGGER THIS
                        if hintbutton == 1:
                            if remaining_time > 15:
                            # JARROD's SIDE: SUBTRACT REMAINING_TIME BY 15
                                remaining_time = remaining_time - 15
                                hints_used += 1
                                print(f"/nHint's used: {hints_used}")
                                print(f"/nHint:{answer[1]}")

                        time.sleep(1)

                else:
                    print("Invalid choice. Please pick again. ")
                    print('\nPlease select your choice: 1,2')
                    print('\t1. Easy')
                    print('\t2. Hard')


            #INVALID CHOICE
            else:
                print('Invalid choice. Please try again.')

run = RunProgramme()
run.start()
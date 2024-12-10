import random 
from encryptDecrypt import EnigmaCipher as enig

#--------------------LIST OF FUNCTIONS------------------------------------
class GameFunction:
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
        alphabet = {
        0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
        8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
        15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
                   }
        cipher = enig(message, m, c, endecrypt=1, alphabet=alphabet)
        encrypted_message = cipher.encryptEnigma('4')
        message_and_cipher = encrypted_message
        return message_and_cipher

        #submit function: compare user input to answer
    def submit(userinput, answer):
        if userinput == answer:
            return 1
        else: 
            return 0

    def word_pick_random(dictionary):
        ### to pick a random key:value pairing:
        random_answer = random.choice(list (dictionary.keys()))
        random_hint = dictionary [random_answer]
        AnswerAndHint = [random_answer, random_hint]
        return AnswerAndHint
    
    def cipher_random():
        list_of_m_values = [1,2,4,5,8,10,11,13,16,17,19,20] # list of values of m that works, all of this are numbers that are odd and non co-prime to 21
        list_of_c_values = list(range(1,21)) #list of values for c 
        random_m = random.choice (list_of_m_values)
        random_c = random.choice (list_of_c_values)
        mclist = [random_m, random_c]
        return (mclist)
    
    def get_user_choice():
            print('\nPlease select your choice: 1,2')
            print('\t1. Easy')
            print('\t2. Hard')
            user_input = input("Enter '1' or '2': ")
            if user_input == '1' or user_input == '2':
                print(f"You selected option {user_input}.")
                return user_input
            else:
                print("Invalid choice. Please enter '1' or '2'.\n")
                return 0
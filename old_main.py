# Name: Natalie Lim Kit Ee
# ID: 2201845
# Class: DAAA/2B/03

import os
from old_encryptDecrypt import CeasarCipher
from old_alphabetList import AlphabetList
from old_alphabetList import SortedList
from old_cipherKey import CipherKey
from old_encryptDecrypt import RailFenceCipher
from old_account import Account

class RunProgramme:
    def start(self):
        print('********************************************************')
        print('* ST1507 DSAA: Welcome to:                             *')
        print('*                                                      *')
        print('*     ~ Caesar Cipher Encrypted Message Analyzer ~     *')
        print('*------------------------------------------------------*')
        print('*                                                      *')
        print('*  - Done by: Natalie Lim(2201845)                     *')
        print('*  - Class DAAA/2B/03                                  *')
        print('********************************************************')
        start = input ('Press enter key, to continue....')

        while True: #continually ask until exit (option 8)
            print('\nPlease select your choice: (1,2,3,4,5,6,7,8)')
            print('\t1. Encrypt/Decrypt Message')
            print('\t2. Encrypt/Decrypt File')
            print('\t3. Analyse letter frequency distribution')
            print('\t4. Infer caesar cipher key from file')
            print('\t5. Analyse, and sort encrypted file')
            print('\t6. Encrypt/Decrypt using Rail Fence Cipher')
            print('\t7. Creating & log into accounts')
            print('\t8. Exit')
            choice = input('Enter choice: ')

#------------------------------------------------- CHOICES -------------------------------------------------#
            #option 1, 2 and 6 together since 1st question asked is same (encrypt/decrypt)
            if choice == '1' or choice == '2' or choice == '6': 
                #explain how Rail Fence Cipher works
                if choice =='6':
                    print("\nHow does Rail Fence Cipher work?\n 1. Input a message & number of rails\n 2. Programme will distribute characters in message along the number of rails\n 3. Encrypt -> compile letters on first row to be first word, letters on second row to be second word, and so on..\n 4. Decrypt -> place words onto rows in fence and read the letters in a zig-zag manner to get back original word\n 5. Print final encrypted/decrypted message")
                    print("\nFor example:\n Encrypt: 'WE ARE DISCOVERED. RUN AT ONCE.' along 3 rails will look like:")
                    print("\n\tW . . . E . . . C . . . R . . . U . . . O . . .\n\t. E . R . D . S . O . E . E . R . N . T . N . E\n\t. . A . . . I . . . V . . . D . . . A . . . C .")
                    print("\nEncrypted message: WECRUO ERDSOEERNTNE AIVDAC")
                    input('\nPress enter key, to continue....')

                #encrypt/decrypt option
                endecrypt = input('\nEnter "E"/"e" for Encrypt and "D"/"d" for Decrypt: ')
                while endecrypt not in ('E','D','e','d'): #not valid inputs
                    print('Please enter either "E"/"e" or "D"/"d" only!') #validation 
                    endecrypt = input('\nEnter "E"/"e" for Encrypt and "D"/"d" for Decrypt: ')

                endecrypt = endecrypt.upper()
                #option 1 (encrypt/decrypt from text)
                if choice == '1':
                    message = self.getValidTextInput(endecrypt) #input message + check if message is empty
                    shift = self.getValidNumericalInput(1) #input shift value + validation (is it a num?)
                            
                    #encrypting/decrypting
                    savedMessage = CeasarCipher(message, shift, endecrypt) #initialise message and shift values
                    solvedMessage = savedMessage.solveCipher()

                    if endecrypt == "E": #print results based on encrypt/decrypt
                        print(f'\nPlaintext:\t{message}\nCiphertext:\t{solvedMessage}')
                    else:
                        print(f'\nCiphertext:\t{message}\nPlaintext:\t{solvedMessage}')

                #option 2 (encrypt/decrypt from file)
                elif choice == '2': 
                    messageFile = self.fileToEndecryptDoesNotExist(endecrypt) #open file for message + check if file exists
                    shift = self.getValidNumericalInput(2) #input shift value + validation (is it a num?)
                            
                    #encrypting
                    savedMessage = CeasarCipher(messageFile, shift, endecrypt) #initialise message and shift values
                    solvedMessage = savedMessage.solveCipher()

                    #check if exisiting file has same name (validation) + create file if file name is valid
                    self.fileAlreadyExists(solvedMessage)

                    if endecrypt == "E" or endecrypt =="e": #print success message based on encrypt/decrypt
                        print('Message successfully encrypted! Check your folder for the results!') 
                    else:
                        print('Message successfully decrypted! Check your folder for the results!') 
                
                #option 6 (using Vigenere Cipher to encrypt/decrypt)
                else:
                    message = self.getValidTextInput(endecrypt) #input message + check if message is empty
                    railNum = self.getValidNumericalInput(6)

                    #remove spaces between words
                    messageWithoutSpace = message.replace(" ", "")
                    
                    #encrypting/decrypting
                    if endecrypt == 'E': #encrypt
                        railFence = RailFenceCipher(messageWithoutSpace, railNum)
                        solvedMessage = railFence.encryptRailFence()
                    else: #decrypt
                        railFence = RailFenceCipher(messageWithoutSpace, railNum)
                        solvedMessage = railFence.decryptRailFence()

                    if endecrypt == "E": #print results based on encrypt/decrypt
                        print(f'\nPlaintext:\t{message}\nCiphertext:\t{solvedMessage}')
                    else:
                        print(f'\nCiphertext:\t{message}\nPlaintext:\t{solvedMessage}\n*Note: Programme cannot identify where spacing between words are. If necessary, please use your judgement to separate the words!')

                input ('\nPress enter key, to continue....') #enter to continue

            #option 3 (Analyse letter frequency distribution)
            elif choice == '3':                 
                textToCount = self.fileToEndecryptDoesNotExist(None)

                #create child(one for every letter) classes
                alphaList = AlphabetList()
                sortList = SortedList()
                alphaList.setCount(textToCount)

                for node in alphaList.letters:
                    sortList.insert(node)    
                
                #get top 5 letters
                top5_nodes = sortList.getTop5()

                letterStar = {}
                #create dictionary to store number of asterisks to print for each letter
                for letter in alphaList.getLetters():
                    percentage = self.getPercentage(letter, alphaList)
                    self.printPercentageBar(letter, percentage, letterStar)

                #loop to add a an asterisk based on % of letter appearing 
                message = ''
                for i in range(27):
                    for letter, countStar in letterStar.items():
                        if countStar > 26-i:
                            message += '* '
                        else:
                            message += '  '
                    if i>0:
                        message +=f'| {alphaList.getLetters()[i-1]} - {self.getPercentage(str(alphaList.getLetters()[i-1]),alphaList):.2f}%'

                    #print top 5 frequencies portion according to given format
                    if alphaList.getLetters()[i-1] =='H':
                        message += '        TOP 5 FREQ'
                    elif alphaList.getLetters()[i-1] =='I':
                        message += '        -----------'
                    elif alphaList.getLetters()[i-1] =='J':
                        message += f'        | {top5_nodes[0].letter}- {self.getPercentage(top5_nodes[0].letter,alphaList):.2f}%'
                    elif alphaList.getLetters()[i-1] =='K':
                        message += f'        | {top5_nodes[1].letter}- {self.getPercentage(top5_nodes[1].letter,alphaList):.2f}%'
                    elif alphaList.getLetters()[i-1] =='L':
                        message += f'        | {top5_nodes[2].letter}- {self.getPercentage(top5_nodes[2].letter,alphaList):.2f}%'
                    elif alphaList.getLetters()[i-1] =='M':
                        message += f'        | {top5_nodes[3].letter}- {self.getPercentage(top5_nodes[3].letter,alphaList):.2f}%'
                    elif alphaList.getLetters()[i-1] =='N':
                        message += f'        | {top5_nodes[4].letter}- {self.getPercentage(top5_nodes[4].letter,alphaList):.2f}%'
                        
                    message += '\n '

                message = message[:-3] #take out last '\n ' so that don't leave extra gap
                print(message)
                print('_____________________________________________________|')
                print(' A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ')

                input ('\nPress enter key, to continue....') #enter to continue
            
            #option 4 (Infer caesar cipher key from file)
            elif choice == '4':
                textToCount = self.fileToEndecryptDoesNotExist(None)

                #read reference file + check if reference file are eligible reference file
                while True:
                    try:
                        referenceFile = self.fileToEndecryptDoesNotExist('freq')
                        dictReferenceFile = {char: float(count) for line in referenceFile.split('\n') if line for char, count in [line.split(',')]}
                        break       
                    except ValueError:
                        print('Please input a file with reference frquencies only!')
    
                #get best shift key
                cipher = CipherKey(textToCount.upper(),dictReferenceFile)
                bestKey = cipher.inferKey()
                        
                #print inferred key
                print(f'\nThe inferred caesar cipher key is: {bestKey}')

                decrypt=''
                while decrypt not in ('y','n'):
                    decrypt = input(f'Would you want to decrypt this file using this key? y/n: ')
                    if decrypt =='y':
                        #encrypting/decrypting
                        savedMessage = CeasarCipher(textToCount, bestKey) #initialise message and shift values
                        solvedMessage = savedMessage.solveCipher()

                        #check if exisiting file has same name (validation) + create file if file name is valid
                        self.fileAlreadyExists(solvedMessage)

                        print('Message successfully decrypted! Check your folder for the results!')
                        break
                    elif decrypt != 'y' and decrypt != 'n':
                            print('Please only enter y/n!\n')

                input ('\nPress enter key, to continue....') #enter to continue

            #option 5 (Analyse, and sort encrypted file)
            elif choice == '5':
                #does folder exist?
                while True:
                    try:
                        folderPath = input('\nPlease enter the folder name: ')
                        folder = os.listdir(folderPath)

                        files = []
                        #append each file
                        for file in folder:
                            files.append(file)
                        break
                    except FileNotFoundError:
                        print('Please input an existing folder!')

                #read englishText file
                englishText = self.fileToEndecryptDoesNotExist('englishtext.txt')
                dictEnglishText = {char: float(count) for line in englishText.split('\n') if line for char, count in [line.split(',')]}

                #get best shift values for each file
                fileDecryptKeys = []
                for file in files:
                    #open each file
                    file_path = os.path.join(folderPath, file)
                    textToCount = open(file_path).read()

                    #get best key for file
                    cipher = CipherKey(textToCount.upper(),dictEnglishText)
                    bestKey = cipher.inferKey()

                    #append file and accompanying key
                    fileDecryptKeys.append((file, bestKey))
                
                #sorted by key
                sortedFileDecryptKeys = sorted(fileDecryptKeys, key=lambda item: item[1])
                
                #encrypting/decrypting each file
                count = 1
                logText = ''
                for file, key in sortedFileDecryptKeys:
                    #Warning if files already exists
                    if "file" in file or "log" in file:
                        if "log" in file:
                            print(f'Warning: {file} already exists, decryption log of encrypted files in this folder will overwrite {file}\n')
                        else:
                            print(f'Warning: {file} already exists, decryption of encrypted files in this folder will overwrite {file}\n')
                    
                    #decode & write decoded text into file1, file2, ...
                    else:
                        #read encoded text
                        with open(os.path.join(folderPath, file), 'r') as r:
                            fileText = r.read()
                        #solve cipher
                        savedMessage = CeasarCipher(fileText, key)
                        solvedMessage = savedMessage.solveCipher()

                        #create file with message
                        decodedMessageFile = 'file' + str(count) +'.txt' #file name
                        with open(os.path.join(folderPath, decodedMessageFile), 'w+') as w:
                            w.write(solvedMessage)

                        #print and save decrypt + key message 
                        logged = f'Decrypting: {file} with key: {key} as: {decodedMessageFile}\n'
                        print(logged)

                        logText += logged +'\n'
                        count += 1

                #write/overwrite log.txt file (depending if it already exists or not)
                with open(os.path.join(folderPath,'log.txt'), 'w') as w:
                    w.write(logText)

                input('\nPress enter key, to continue....') #enter to continue

            #option 7
            elif choice == '7':
                account = Account()
                accounts = {}
                
                while True:
                    createLogIn = input(f"\nPlease select your choice (1/2/3): \n\t1. Create Account\n\t2. Log in\n\t3. Exit\nEnter your choice: ")
                    if createLogIn == '1':
                        #for username validation (option 7): check if inputted values are alphabets only
                        while True:   
                            username = input('Username: ')

                            if username.isalnum():
                                if username in accounts.keys():
                                    print('Another account already has this username. Please use another username!\n')
                                else:
                                    break
                            else:
                                print('Please enter letters / numbers only!\n')
                        
                        account.setName(username) #setName to username

                        pwrand = input(f"\nHi {account.getName()}! Please select your choice (1/2/3): \n\t1. Use randomly generate password\n\t2. Use own password\n\t3. Exit\nEnter your choice: ")

                        if pwrand == '1': #randomly generate password
                            while True:
                                try:
                                    PWlen = self.getValidNumericalInput(7)
                                    randPW = account.randPassword(PWlen)
                                    account.setPassword(randPW)
                                    strength = account.passwordStrength(randPW)
                                    break
                                except ValueError:
                                    print("Sorry password generated is weak. Please increase password's length!")
                            
                            print(f"\nHere is your randomly generated password: {randPW}\nThis password has strength: {strength}")

                            #add username & passwords to accounts to save ing=fo for future log in
                            accounts[account.getName()] = account.getPassword()
        
                            input('\nPress enter key, to continue....') #enter to continue

                        elif pwrand == '2': #input own password + check strength of password
                            while True:
                                try:
                                    selfPW = input(f'\nPlease enter your own password: ')
                                    strength = account.passwordStrength(selfPW)
                                    break
                                except ValueError:
                                    print('Sorry password is weak. Please enter a stronger password (suggestions: make it longer/include special characters)')
                                
                            print(f"\nGreat! Your set password's stregth is: {strength}")
                            account.setPassword(selfPW)

                            #add username & passwords to accounts to save ing=fo for future log in
                            accounts[account.getName()] = account.getPassword()

                        elif pwrand == '3':
                            break

                        else:
                            print('Please input 1/2/3 only!\n')

                    elif createLogIn == '2':
                        #for demo only:
                        print(accounts)

                        currentUser = input('\nEnter username: ')
                        if currentUser not in accounts.keys():
                            print('Username not in database. Please create an account before continuing!')
                            continue

                        currentUserPW = ''
                        while currentUserPW != accounts.get(currentUser, ''):
                            currentUserPW = input('Enter password: ')
                            if currentUserPW != accounts.get(currentUser, ''):
                                print('Incorrect password. Please try again.\n')
                        
                        print('Successfully logged in!')
                        changePW = input('Would you like to change your password? [y/n] ')
                        if changePW =='y':
                            while True:
                                try:
                                    selfPW = input(f'\nPlease enter your own password: ')
                                    strength = account.passwordStrength(selfPW)
                                    break
                                except ValueError:
                                    print('Sorry password is weak. Please enter a stronger password (suggestions: make it longer/include special characters)')
                                
                            print(f"\nGreat! Your set password's stregth is: {strength}")
                            account.setPassword(selfPW)

                            #add username & passwords to accounts to save ing=fo for future log in
                            accounts[currentUser] = account.getPassword()
                        else:
                            print('Logged out! Have a nice day!')

                    elif createLogIn =='3':
                        break

                    else:
                        print('Please input 1/2/3 only!\n')

                input('\nPress enter key, to continue....') #enter to continue

            #option 8 - exit
            elif choice =='8':
                print('Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyser!')
                break
            else:
                print('Please input a number between 1 and 8 only!')


#-----------------------------------------------------------------------------------------------------------#
# FUNCTIONS!!
    #for message (option 1/6): ensure text isn't empty
    def getValidTextInput(self, endecrypt):
        while True:
            if endecrypt == "E":
                message = input('\nPlease type text you want to encrypt:\n') #need to be separate from decrypt since input message is different
            else:
                message = input('\nPlease type text you want to decrypt:\n')

            if message.strip() == "":
                if endecrypt == "E":
                    print("The string is empty or contains only whitespace. Please enter the text you would like to encrypt!")
                else:
                    print("The string is empty or contains only whitespace. Please enter the text you would like to decrypt!")

            else:
                return message  # Return the valid message

    #for numerical input (option 1/2/6/7): don't allow letter inputs & continue asking until number is given
    def getValidNumericalInput(self, option):
        while True:
            try:
                if option == 1 or option == 2:
                    integer = int(input('\nEnter the cipher key: '))
                elif option == 6:
                    integer = int(input('\nEnter number of rails: '))
                else: #option 7
                    integer = int(input('\nEnter length of desired password: '))
                return integer  # Return the valid integer
            except ValueError:
                print('Please input a digit!')

    #for file (option 2/3/4/5): if file doesn't exist, can't be encrypted/decrypted
    def fileToEndecryptDoesNotExist(self, encrypt):
        while True:
            try:
                if encrypt == "E": #custom message based on encrypt/decrypt
                    file = input('\nPlease enter the file you want to encrypt (include .txt, etc): ')
                elif encrypt == "D":
                    file = input('\nPlease enter the file you want to decrypt (include .txt, etc): ')
                elif encrypt == None: #option 3/4
                    file = input('\nPlease enter the file you want to analyse (include .txt, etc): ')
                elif encrypt == 'freq': #option 4
                    file = input('\nPlease enter the reference frequencies file (include .txt, etc): ')
                else: #option 5
                    file = encrypt
                
                #read .txt file
                messageFile = open(file).read()
                return messageFile # Return the valid message file

            except FileNotFoundError:
                if encrypt == "E": #custom message based on encrypt/decrypt
                    print('Please input an existing file to encrypt!')
                elif encrypt == "D":
                    print('Please input an existing file to decrypt!')
                else:
                    print('Please input an existing file!')
    
    #for file (option 2/4): if chosen output file already exists, do we overwrite it?
    def fileAlreadyExists(self,solvedMessage):
        while True:
            try:
                decodedMessageFile = '.txt'
                while decodedMessageFile =='.txt':
                    decodedMessageFile = input('\nPlease enter a output file (.txt not required): ')+'.txt' 
                    if decodedMessageFile =='.txt':
                        print('Please enter a valid filename!')

                with open(decodedMessageFile, 'r'):
                    overwrite = ''
                    while overwrite not in ('y','n'):
                        overwrite = input(f"The file '{decodedMessageFile}' already exists. Would you like to overwrite the file? [y/n] ")
                        if overwrite =='y':
                            with open(decodedMessageFile, 'w+') as w:
                                w.write(solvedMessage)
                            return
                        elif overwrite != 'y' and overwrite != 'n':
                            print('Please only enter y/n!\n')
            except FileNotFoundError:
                #create file with message
                with open(decodedMessageFile, 'w+') as w:
                    w.write(solvedMessage)
                return

    #for % (option 3): get % of letter occuring out of word/phrase
    def getPercentage(self, letter, alphaList):
        total_count = alphaList.getTotalCount()
        if total_count != 0:
            return alphaList.getLetterCount(letter) / total_count * 100
        else:
            return 0

    #for graph (option 3): get number of * to be shown per letter
    def printPercentageBar(self, letter, percentage, letterStar):
        #scale down such that total * = 26 (number of rows in bar chart)
        if percentage / 100 * 26 > 0: 
            asterisks = int(percentage / 100 * 26) +1 #always round up if letter exists in text
        else:
            asterisks = 0 #letter isnt in text
        letterStar[letter] = asterisks


run = RunProgramme()
run.start()
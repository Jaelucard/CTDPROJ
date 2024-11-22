# Name: Natalie Lim Kit Ee
# ID: 2201845
# Class: DAAA/2B/03

import string
import random
import re
class Account:
    def __init__(self, username = None, userPW = None):
        self.__username = username
        self._userPW = userPW

    #get name
    def getName(self):
        return self.__username

    #set name
    def setName(self, name):
        self.__username = name

    #get password
    def getPassword(self):
        try:
            return self.__userPW
        except AttributeError:
            return print('Acount ')

    #set password
    def setPassword(self, pw):
        self.__userPW = pw

    #generate random psasword (minimally have 1 uppercase, 1 lowercase, 1 digit)
    def randPassword(self, length):
        #all possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        #generate 1 uppercase, 1 lowercase letter and 1 digit (minimally 1 of each in pw)
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)

        self._randPW = uppercase + lowercase + digit

        #generate rest of random password by randomly choosing characters to fill in remaining length
        self._randPW += ''.join(random.choice(characters) for i in range(length-3))
        return self._randPW

    #check password strength of randomly generated & user input passwords
    def passwordStrength(self, password):
        lengthPoints = self.checkLen(password)
        complexityPoints = self.checkComplexity(password)

        #calculate total complexity by adding score from length and complexity
        total = lengthPoints + complexityPoints

        if total >= 8:
            return "Strong"
        elif total >= 6:
            return "Moderate"
        else:
            raise ValueError('Sorry password is weak. Please enter a stronger password (suggestions: make it longer/include special characters)')

    #length has largest impact on password complexity (longer password = more complex)
    def checkLen(self, password):
        length = len(password)
        if length >= 8:
            return 3
        elif length >= 6:
            return 2
        else:
            return 1

    def checkComplexity(self, password):
        complexity = 0

        #check for uppercase and lowercase
        if re.search(r'[A-Z]', password) or re.search(r'[a-z]', password):
            complexity += 2

        #check for digits
        if re.search(r'\d', password):
            complexity += 1

        #check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            complexity += 3

        return complexity
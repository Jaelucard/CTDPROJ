###function for randomly pick the word from a dictionary
import random

def word_pick_random (dictionary):
    ### to pick a random key:value pairing:
    random_answer = random.choice(list (dictionary.keys()))
    print (random_answer)
    random_hint = dictionary [random_answer]
    return random_answer, random_hint
print (word_pick_random(band_dict))

###test cases:
dictionary = {
    "apple": "fruit",
    "carrot": "vegetable",
    "dog": "animal",
    "rose": "flower",
    "python": "programming language",
    "guitar": "instrument",
    "ocean": "water body",
    "eagle": "bird",
    "diamond": "gemstone",
    "sun": "star"
}
word_of_the_day = word_pick_random(dictionary)
print(word_of_the_day)
###randomiser for values of functions to use in cipher
list_of_m_values = [5,9,11,13,15,17,19,21] # list of values of m that works, all of this are numbers that are odd and non co-prime to 21
list_of_c_values = list(range(1,21)) #list of values for c 
random_m = random.choice (list_of_m_values)
random_c = random.choice (list_of_c_values)
print (m,c)


###score calculation
score = 0 #starting value of score
scores = []
def score_calculation (modechoice, remaining_seconds):
    """
    takes in the type of mode (easy or hard) and the remaining seconds from jarrod's function. 
    returns the score for one question, calculated based on the remaining seconds
    """
    ### modechoice (modifier) + remaining time(multiplier)
        ###modechoice portion, each 'easy' is 10 points and 'hard' is 20 points.
    if modechoice == 1:
        modifier = 10
        
    elif modechoice == 2:
        modifier = 20

    score_per_question = modifier * remaining_seconds/60

    return score_per_question

       

###final score addition:
###storing the values of the score_per_question

def final_score (score_per_question , #number of questions):
    final = 


###hint function where X seconds is minused off the time section

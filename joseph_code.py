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
list_of_m_values = [1,3,5,7,9,11,13,15,17,19,21]
list_of_c_values = [1:25]
random_m = random.choice (list_of_m_values)
random_c = random.choice (list_of_c_values)
print (m,c)


###score calculation
score = 0
def score_calculation (modechoice, seconds)
    ### modechoice (modifier) + remaining time(multiplier)
        ###modechoice portion, each 'easy' is 10 points and 'hard' is 20 points.
    if modechoice == 1:
        modifier = 10
    elif modechoice == 2:
        modifier = 20

    remaining_time = 
    score_per_question = modifier *remaining_time/60

        ###remaining time is based on the number of secobnds left for the total points gained from the question. 
        ###each easy question is 60 seconds with minimum 30 seconds but hard questions are 120 seconds with min 30

###final score addition:
    final score(score, number_questions):



###hint function where X seconds is minused off the time section

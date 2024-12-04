import random

# Function definition (ensure this is defined earlier in the script)
def word_pick_random(dictionary):
    if not dictionary:
        raise ValueError("The dictionary is empty.")
    random_key = random.choice(list(dictionary.keys()))
    return random_key, dictionary[random_key]
### need to input a function to save and hold the value until next question 

# Random word picker
dictionary = {
    "apple": "fruit",
    "carrot": "vegetable",
    "dog": "animal",
    "rose": "flower"
}
word_of_the_day = word_pick_random(dictionary)
print("Word of the Day:", word_of_the_day)

# Randomiser for cipher values
list_of_m_values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
list_of_c_values = list(range(1, 25))  # Correctly generate values 1 through 25
def cipher_function_randomiser ():
    random_m = random.choice(list_of_m_values)
    random_c = random.choice(list_of_c_values)
    print("Random m value:", random_m)
    print("Random c value:", random_c)


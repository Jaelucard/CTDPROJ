import tkinter as tk
import random

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
        
    
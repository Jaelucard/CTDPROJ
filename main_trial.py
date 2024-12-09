import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
from encryptDecrypt import EnigmaCipher as enig
from validation import Validation as val
from zahinbahin import GameFunction as game


class EnigmaGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Puzzle Game")
        self.alphabet = {
            0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
            8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's',
            15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
        }
        self.accumulated_points = 0
        self.hints_used = 0
        self.failcheck1 = 0
        self.failcheck2 = 0
        self.progress = 0
        self.remaining_time = 60
        self.message = ""
        self.build_main_menu()

    def build_main_menu(self):
        """Main menu to choose between options."""
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = ttk.Label(self.root, text="Enigma Puzzle Game", font=("Helvetica", 20))
        title_label.pack(pady=10)

        # Menu Buttons
        encrypt_btn = ttk.Button(self.root, text="Encrypt Message", command=self.encrypt_menu)
        encrypt_btn.pack(pady=5)

        decrypt_btn = ttk.Button(self.root, text="Decrypt Message", command=self.decrypt_menu)
        decrypt_btn.pack(pady=5)

        game_btn = ttk.Button(self.root, text="Start Game", command=self.start_game_menu)
        game_btn.pack(pady=5)

        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=5)

        
    def encrypt_menu(self):
        self.process_message_menu("Encrypt")

    def decrypt_menu(self):
        self.process_message_menu("Decrypt")

    def process_message_menu(self, mode):
        """Menu for encryption or decryption."""
        for widget in self.root.winfo_children():
            widget.destroy()

        mode_label = ttk.Label(self.root, text=f"{mode} Message", font=("Helvetica", 16))
        mode_label.pack(pady=10)

        message_label = ttk.Label(self.root, text="Enter your message:")
        message_label.pack()
        message_entry = ttk.Entry(self.root, width=40)
        message_entry.pack(pady=5)

        m_label = ttk.Label(self.root, text="Enter Gradient (m):")
        m_label.pack()
        m_entry = ttk.Entry(self.root, width=10)
        m_entry.pack(pady=5)

        c_label = ttk.Label(self.root, text="Enter Intercept (c):")
        c_label.pack()
        c_entry = ttk.Entry(self.root, width=10)
        c_entry.pack(pady=5)

        result_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        result_label.pack(pady=10)

        def process():
            message = message_entry.get()
            m = m_entry.get()
            c = c_entry.get()

            if not message or not m.isdigit() or not c.isdigit():
                messagebox.showerror("Input Error", "Please provide valid inputs!")
                return

            m = int(m)
            c = int(c)
            action = 1 if mode == "Encrypt" else 2
            cipher = enig(message, m, c, endecrypt=action, alphabet=self.alphabet)
            processed_message, shifted_alphabet = cipher.encryptEnigma()
            self.alphabet = shifted_alphabet
            result_label.config(text=f"{mode}ed Message: {processed_message}")

        process_button = ttk.Button(self.root, text=f"{mode}", command=process)
        process_button.pack(pady=5)

        back_button = ttk.Button(self.root, text="Back", command=self.build_main_menu)
        back_button.pack(pady=5) 

    def start_game_menu(self):
        """Menu to start the game."""
        for widget in self.root.winfo_children():
            widget.destroy()

        mode_label = ttk.Label(self.root, text="Choose Game Mode", font=("Helvetica", 16))
        mode_label.pack(pady=10)

        easy_button = ttk.Button(self.root, text="Easy Mode", command=lambda: self.start_game("Easy"))
        easy_button.pack(pady=5)


        hard_button = ttk.Button(self.root, text="Hard Mode", command=lambda: self.start_game("Hard"))
        hard_button.pack(pady=5)

        back_button = ttk.Button(self.root, text="Back", command=self.build_main_menu)
        back_button.pack(pady=5)

    def start_game(self, mode):
        """Game logic for easy or hard mode."""
        band_dict = {'die with a smile': 'bruno mars', 'rolling in the deep': 'adele', 'love story': 'taylor swift',
                     'all i want for christmas is you': 'mariah carey', 'treasure': 'bruno mars', 'im yours': 'jason mraz'}

        self.progress = 0
        self.accumulated_points = 0
        self.hints_used = 0
        self.remaining_time = 60

        timer_label = ttk.Label(self.root,text=f"Time Remaining: {self.remaining_time} seconds", font=("Helvetica", 12))
        timer_label.pack(pady=5)

        def update_timer():
            if self.remaining_time > 0:
                self.remaining_time -= 1
                timer_label.config(text=f"Time Remaining: {self.remaining_time} seconds")
                self.root.after(1000, update_timer)  # Schedule the timer to update after 1 second
            else:
                messagebox.showinfo("Time's Up!", "Game over! You ran out of time.")
                self.build_main_menu()

        def ask_question():
            nonlocal band_dict
            if self.progress >= 6:
                messagebox.showinfo("Game Over", f"You won! Total Points: {self.accumulated_points}")
                self.build_main_menu()
                return

            answer = game.word_pick_random(band_dict)
            question_label.config(text=f"Guess the Song: {answer[0]}")
            cipher = game.cipher_random()
            encrypted_message = game.encrypter(answer[0], cipher[0], cipher[1])

            encryption_label.config(text=f"Encryption Cipher: {cipher[0]}*key + {cipher[1]}")
            encrypted_label.config(text=f"Encrypted Message: {encrypted_message}")

            def submit():
                user_input = answer_entry.get()
                if game.submit(user_input, answer[0]) == 1:
                    self.progress += 1
                    self.accumulated_points += game.calculate_award(1 if mode == "Easy" else 2, self.remaining_time)
                    messagebox.showinfo("Correct", "Good job! Moving to the next question.")
                    ask_question()
                else:
                    messagebox.showerror("Incorrect", "Try again!")

            submit_button = ttk.Button(self.root, text="Submit", command=submit)
            submit_button.pack(pady=5)

        for widget in self.root.winfo_children():
            widget.destroy()

        game_label = ttk.Label(self.root, text=f"Mode: {mode}", font=("Helvetica", 16))
        game_label.pack(pady=10)

        question_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        question_label.pack(pady=5)

        encryption_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        encryption_label.pack(pady=5)

        encrypted_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        encrypted_label.pack(pady=5)

        answer_label = ttk.Label(self.root, text="Your Answer:")
        answer_label.pack(pady=5)

        answer_entry = ttk.Entry(self.root, width=20)
        answer_entry.pack(pady=5)

        ask_question()
        update_timer()

        back_button = ttk.Button(self.root, text="Back", command=self.build_main_menu)
        back_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    app = EnigmaGameApp(root)
    root.mainloop()

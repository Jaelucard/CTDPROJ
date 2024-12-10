import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import time
import random
from math import gcd
from encryptDecrypt import EnigmaCipher as enig
from validation import Validation as val
from zahinbahin import GameFunction as game


class EnigmaGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Puzzle Game")
        self.root.geometry("600x600")
        self.alphabet = {
            0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
            8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's',
            15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
        }
        self.correct_attempts = 0
        self.remaining_time = 120
        self.progress = 0
        self.hints_used = 0
        self.band_hint = ""
        self.timer_running = False
        self.build_main_menu()

    def build_main_menu(self):
        """Main Menu with Start Game and Exit Buttons."""
        for widget in self.root.winfo_children():
            widget.destroy()

        title1_label = ttk.Label(self.root, text="Enigma Puzzle Game", font=("Helvetica", 20))
        title1_label.pack(pady=10)

       
        button1_frame = ttk.Frame(self.root)
        button1_frame.pack(pady=10)

        start_button = ttk.Button(button1_frame, text="Start Game", command=self.start_game_menu)
        start_button.pack(side="left", padx=20)

        exit_button = ttk.Button(button1_frame, text="Exit", command=self.root.quit)
        exit_button.pack(side="left", padx=20)

        title2_label = ttk.Label(self.root, text="Learn Educational Encryption?"
                                 , font=("Helvetica", 20))
        title2_label.pack(pady=10)

        button2_frame = ttk.Frame(self.root)
        button2_frame.pack(pady=10)

        encryption_button = ttk.Button(button2_frame, text="Go", command=self.learning_encrypt_window)
        encryption_button.pack(side="left", padx=20)

    def start_game_menu(self):
        #Game Mode with Timer, Hint, and Pop-up Encrypt/Decrypt.
        for widget in self.root.winfo_children():
            widget.destroy()

        # Timer Display
        self.remaining_time = 120
        self.correct_attempts = 0
        self.timer_running = True
        self.timer_label = ttk.Label(self.root, text=f"Time Left: {self.remaining_time}s", font=("Helvetica", 12))
        self.timer_label.place(relx=0.95, rely=0.05, anchor="ne")
        self.start_timer()

        # Game Instructions
        game_label = ttk.Label(self.root, text="Solve the Enigma Puzzle!", font=("Helvetica", 16))
        game_label.pack(pady=10)

        # Display for Questions and Encrypted Message
        self.question_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=5)

        self.encryption_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.encryption_label.pack(pady=5)

        self.encrypted_message_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.encrypted_message_label.pack(pady=5)

        # User Answer
        answer_label = ttk.Label(self.root, text="Your Answer:")
        answer_label.pack(pady=5)

        self.answer_entry = ttk.Entry(self.root, width=30)
        self.answer_entry.pack(pady=5)

        # Buttons
        button1_frame = ttk.Frame(self.root)
        button1_frame.pack(pady=10)

        submit_button = ttk.Button(button1_frame, text="Submit", command=self.check_answer)
        submit_button.pack(side="left", padx=5)

        hint_button = ttk.Button(button1_frame, text="Hint", command=self.show_hint)
        hint_button.pack(side="left", padx=5)

        encrypt_button = ttk.Button(button1_frame, text="Decrypt", command=self.open_encrypt_window)
        encrypt_button.pack(side="left", padx=5)

        button2_frame = ttk.Frame(self.root)
        button2_frame.pack(pady=10)

        back_button = ttk.Button(button2_frame, text="Back", command=self.build_main_menu)
        back_button.pack(side="left", padx=5)

        # Start First Question
        self.ask_question()

    def start_timer(self):
        """Timer Countdown."""
        if self.remaining_time > 0 and self.timer_running:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}s")
            self.root.after(1000, self.start_timer)
        elif self.remaining_time == 0:
            self.timer_running = False
            messagebox.showinfo("Time's Up!", "Time is up! Returning to the main menu.")
            self.build_main_menu()

    def ask_question(self):
        #Generate a Question.
        self.current_band = game.word_pick_random({
            'die with a smile': 'bruno mars',
            'rolling in the deep': 'adele',
            'love story': 'taylor swift',
            'all i want for christmas is you': 'mariah carey',
            'treasure': 'bruno mars',
            'im yours': 'jason mraz',
            'cruel summer': 'taylor swift',
            'thats so true': 'gracie adams',
            'we fell in love in october': 'girl in red', 
            'lily in the valley': 'Daniel',
            'thick of it': 'KSI',
            'wrecking ball': 'miley cyrus',
            'perfect': 'one direction',
            'night changes': 'one direction', 
            'what makes you beautiful': 'one direction',
            'the man who cant be moved': 'the script',
            'i knew you were trouble': 'taylor swift',
            'too sad to dance': 'jungkook',
            'from the start': 'laufey',
            'a sky full of stars': 'coldplay',
            'hymn for the weekend': 'coldplay',
            'we didnt start the fire': 'billy joel',
            'crazy little thing called love': 'queen',
            'september': 'earth wind and fire', 
            'good life': 'g-eazy',
            'wildflower': 'billie eilish',
            'magnetic': 'illit',
            'i wanna be like you': 'louis prima',
            'super shy': 'newjeans',
            'the first snow': 'exo',
            'supercalifragilisticexpialidocious': 'dick van dyke and julie andrews'
            })


        self.song_name = self.current_band[0]
        self.band_hint = self.current_band[1]
        cipher = game.cipher_random()
        encrypted_message = game.encrypter(self.current_band[0], cipher[0], cipher[1])

        self.x_value = cipher[0]

        self.question_label.config(text=f"Guess the Song!")
        self.encryption_label.config(text=f"Cipher: ___ x + {cipher[1]}") 
        self.encrypted_message_label.config(text=f"Encrypted Message: {encrypted_message}")

    def check_answer(self):
        """Check the User's Answer."""
        user_input = self.answer_entry.get()
        if game.submit(user_input, self.current_band[0]) == 1:
            self.correct_attempts += 1
            self.progress += 1
            self.remaining_time = 120  # Reset Timer
            messagebox.showinfo("Correct", "Great job! Moving to the next question.")
            if self.correct_attempts >= 3:
                messagebox.showinfo("Success!", "You solved 3 in a row! Returning to the main menu.")
                self.build_main_menu()
            else:
                self.ask_question()
        else:
            messagebox.showerror("Wrong", "Incorrect. Try again!")

    def show_hint(self):
        """Show Hint and Reduce Timer."""
        if self.remaining_time > 20:
            self.remaining_time -= 20
            messagebox.showinfo("Hint", f"The band is: {self.band_hint}")
        else:
            self.remaining_time = 0
            messagebox.showinfo("Time's Up!", "Time is up! Returning to the main menu.")
            self.build_main_menu()

    def learning_encrypt_window(self):
        """Open a Pop-up Window for Encryption/Decryption."""
        popup = Toplevel(self.root)
        popup.title("Decrypt")
        popup.geometry("400x300")

        mode1_label = ttk.Label(popup, text="Encryption Page", font=("Helvetica", 18))
        mode1_label.pack(pady=10)

        mode2_label = ttk.Label(popup, 
                      text="--------------------------USER GUIDE--------------------------\n"
                      "A linear function takes the form of mx + c, where m is the number of times we split the list and c is the translation to the left or right.\n"
                      "Please note the vowels and first and last letters of the message will not be encrypted.\n"
                      , font=("Helvetica", 10, "bold"),
                      justify="center",
                      anchor="center",
                      )
        mode2_label.pack(pady=20)

        mode3_label = ttk.Label(popup, text= "What is your message? "
                              , font=("Helvetica", 12))
        mode3_label.pack(pady=5)

        message_entry = ttk.Entry(popup, width=30)
        message_entry.pack()

        mode4_label = ttk.Label(popup, text= "Please input a linear function for your encryption! "
                              , font=("Helvetica", 12))
        mode4_label.pack(pady=5)

        m_label = ttk.Label(popup, text="Gradient (m):", 
                            font=("Helvetica", 12))
        m_label.pack()
        m_entry = ttk.Entry(popup, width=30)
        m_entry.pack()

        c_label = ttk.Label(popup, text="Intercept (c):",
                             font=("Helvetica", 12))
        c_label.pack()
        c_entry = ttk.Entry(popup, width=30)
        c_entry.pack()

        result_label = ttk.Label(popup, text="Output", font=("Helvetica", 12))
        result_label.pack(pady=5)

        def encrypt_message():
            message = message_entry.get()
            m = m_entry.get()
            c = c_entry.get()
            try:
                if not message:
                    result_label.config(text="Please enter a valid message!")

                m = int(m)
                c = int(c)
                alphabet = {
                    0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
                    8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
                    15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
                }
                #encrypt/decrypt message
                encrypted, oringinal_alphabet,shifted_alphabet = enig(message, m, c, endecrypt = 1, alphabet = alphabet).encryptEnigma(1)
                alphabet = shifted_alphabet #update alphabet
                result_label.config(text=f"Processed Message: {encrypted}\n\nOriginal Alphabet:\n{oringinal_alphabet}\n\n{shifted_alphabet}\n^ Shifted Alphabet ^"
                                    , justify="center",anchor="center",)
                        
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid inputs!\nnumber needs to be integer and coprime with 21!")
        
            # Display the jumbled encrypted message
            #return result_label.config(text=f"Processed Message: {jumbled_message}")

        process_button = ttk.Button(popup, text="Submit", command=encrypt_message)
        process_button.pack(pady=5)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=5)

    def open_encrypt_window(self):
        """Open a Pop-up Window for Encryption/Decryption."""
        popup = Toplevel(self.root)
        popup.title("Encrypt/Decrypt")
        popup.geometry("400x300")

        mode_label = ttk.Label(popup, text="Enter Details:", font=("Helvetica", 14))
        mode_label.pack(pady=10)

        message_label = ttk.Label(popup, text="Message:")
        message_label.pack()
        message_entry = ttk.Entry(popup, width=30)
        message_entry.pack()

        m_label = ttk.Label(popup, text="Gradient (m):")
        m_label.pack()
        m_entry = ttk.Entry(popup, width=10)
        m_entry.pack()

        c_label = ttk.Label(popup, text="Intercept (c):")
        c_label.pack()
        c_entry = ttk.Entry(popup, width=10)
        c_entry.pack()

        result_label = ttk.Label(popup, text="", font=("Helvetica", 12))
        result_label.pack(pady=5)

        def process():
            message = message_entry.get()
            m = m_entry.get()
            c = c_entry.get()
            try:
                m = int(m)
                c = int(c)
                alphabet = {
                    0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
                    8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
                    15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
                }
                decrypted, oringinal_alphabet,new_alphabet = enig(message,m,c,2,alphabet).encryptEnigma(2)
                result_label.config(text=f"Processed Message: {decrypted}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid inputs!\nnumber needs to be integer and coprime with 21!")

        process_button = ttk.Button(popup, text="Submit", command=process)
        process_button.pack(pady=5)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaGameApp(root)
    root.mainloop()
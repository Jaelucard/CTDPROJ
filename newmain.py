import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import time
import random
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
        self.remaining_time = 60
        self.progress = 0
        self.hints_used = 0
        self.band_hint = ""
        self.timer_running = False
        self.build_main_menu()

    def build_main_menu(self):
        """Main Menu with Start Game and Exit Buttons."""
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = ttk.Label(self.root, text="Enigma Puzzle Game", font=("Helvetica", 20))
        title_label.pack(pady=10)

       
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        start_button = ttk.Button(button_frame, text="Start Game", command=self.start_game_menu)
        start_button.pack(side="left", padx=20)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.root.quit)
        exit_button.pack(side="left", padx=20)

    def start_game_menu(self):
        #Game Mode with Timer, Hint, and Pop-up Encrypt/Decrypt.
        for widget in self.root.winfo_children():
            widget.destroy()

        # Timer Display
        self.remaining_time = 60
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
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        submit_button = ttk.Button(button_frame, text="Submit", command=self.check_answer)
        submit_button.pack(side="left", padx=5)

        hint_button = ttk.Button(button_frame, text="Hint", command=self.show_hint)
        hint_button.pack(side="left", padx=5)

        encrypt_button = ttk.Button(button_frame, text="Encrypt/Decrypt", command=self.open_encrypt_window)
        encrypt_button.pack(side="left", padx=5)

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
            'im yours': 'jason mraz'
        })
        self.band_hint = self.current_band[1]
        cipher = game.cipher_random()
        encrypted_message = game.encrypter(self.current_band[0], cipher[0], cipher[1])

        self.question_label.config(text=f"Guess the Song!")
        self.encryption_label.config(text=f"Cipher: {cipher[0]}*key + {cipher[1]}")
        self.encrypted_message_label.config(text=f"Encrypted Message: {encrypted_message}")

    def check_answer(self):
        """Check the User's Answer."""
        user_input = self.answer_entry.get()
        if game.submit(user_input, self.current_band[0]) == 1:
            self.correct_attempts += 1
            self.progress += 1
            self.remaining_time = 60  # Reset Timer
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
            if not message or not m.isdigit() or not c.isdigit():
                messagebox.showerror("Input Error", "Please enter valid inputs!")
            else:
                result_label.config(text=f"Processed Message: {message}")

        process_button = ttk.Button(popup, text="Submit", command=process)
        process_button.pack(pady=5)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaGameApp(root)
    root.mainloop()
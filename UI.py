import tkinter as tk
from tkinter import ttk, messagebox


class EnigmaGameUI:
    def __init__(self, root, logic_interface):
        self.root = root
        self.logic = logic_interface  # Reference to the RunProgramme class
        self.root.title("Enigma Puzzle Game")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Enigma Puzzle Game", font=("Helvetica", 16)).pack(pady=10)

        self.message_label = ttk.Label(self.root, text="Enter Message:")
        self.message_label.pack()
        self.message_entry = ttk.Entry(self.root, width=40)
        self.message_entry.pack()

        self.gradient_label = ttk.Label(self.root, text="Gradient (m):")
        self.gradient_label.pack()
        self.gradient_entry = ttk.Entry(self.root, width=10)
        self.gradient_entry.pack()

        self.intercept_label = ttk.Label(self.root, text="Intercept (c):")
        self.intercept_label.pack()
        self.intercept_entry = ttk.Entry(self.root, width=10)
        self.intercept_entry.pack()

        self.encrypt_button = ttk.Button(self.root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = ttk.Button(self.root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.pack(pady=5)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def encrypt_message(self):
        message = self.message_entry.get()
        gradient = self.gradient_entry.get()
        intercept = self.intercept_entry.get()

        if message and gradient.isdigit() and intercept.isdigit():
            encrypted_message = self.logic.encrypt_message(message, int(gradient), int(intercept))
            messagebox.showinfo("Encrypted Message", f"Encrypted: {encrypted_message}")
        else:
            messagebox.showerror("Input Error", "Please provide valid inputs.")

    def decrypt_message(self):
        message = self.message_entry.get()
        gradient = self.gradient_entry.get()
        intercept = self.intercept_entry.get()

        if message and gradient.isdigit() and intercept.isdigit():
            decrypted_message = self.logic.decrypt_message(message, int(gradient), int(intercept))
            messagebox.showinfo("Decrypted Message", f"Decrypted: {decrypted_message}")
        else:
            messagebox.showerror("Input Error", "Please provide valid inputs.")
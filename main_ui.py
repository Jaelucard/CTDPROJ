import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import decrypt_ui_rachel
import encrypt_ui_rachel
#create a class

class EnigmaGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Puzzle Game")
        self.timer_seconds = 0
        self.configure_styles()
        self.create_widgets()

    def configure_styles(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), padding=10)
        style.configure("Hint.TLabel", font=("Helvetica", 12, "italic"), foreground="gray")

    def create_widgets(self):
        self.title_label = ttk.Label(self.root, text="Welcome to the Enigma Puzzle Game", style="Title.TLabel")
        self.title_label.pack(pady=10)

        self.timer_label = ttk.Label(self.root, text="Timer: 00:00", style="TLabel")
        self.timer_label.place(relx=0.95, rely=0.05,  anchor="ne")

        self.info_label = ttk.Label(self.root, text="Game details will appear here.", style="TLabel")
        self.info_label.pack(pady=5)

        self.text_box = tk.Text(self.root, height = 5, width = 50, wrap = "word", font = ("Helvetica", 12))
        self.text_box.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_game)
        self.start_button.pack(side="left", padx=5)

        self.hint_button = ttk.Button(button_frame, text="Hint", command=self.show_hint)
        self.hint_button.pack(side="left", padx=5)

        self.exit_button = ttk.Button(button_frame, text="Exit", command=self.exit_game)
        self.exit_button.pack(side="left", padx=5)

        second_button_frame = ttk.Frame(self.root)
        second_button_frame.pack(pady=10)

        self.encrypt_button = ttk.Button(second_button_frame, text="Encryptor", command=self.encryptor)
        self.encrypt_button.pack(side="left", padx=5)

        self.decrypt_button = ttk.Button(second_button_frame, text="Decryptor", command= self.decryptor)
        self.decrypt_button.pack(side="left", padx=5)

    def update_timer(self):
        self.timer_seconds += 1
        minutes, seconds = divmod(self.timer_seconds, 60)
        self.timer_label.config(text=f"Timer: {minutes:02}:{seconds:02}")
        self.root.after(1000, self.update_timer)

    def start_game(self):
        self.timer_seconds = 0
        self.update_timer()
        self.info_label.config(text="Game started! Solve the puzzles to proceed.")
        self.hint_label.config(text="Hint will appear when you request it.")

    def show_hint(self):
        self.hint_label.config(text="This is your hint: [Hint placeholder]")
        messagebox.showinfo("Hint", "Here is your hint: [Hint placeholder]")

    def exit_game(self):
        self.root.quit()

    def encryptor(self):
        new_window = tk.Toplevel(root)  # Create a new window
        new_window.title("Encrypt")
        new_window.geometry("600x400")

        encrypt_ui_rachel.populate_window(new_window)

    def decryptor(self):
        new_window = tk.Toplevel(root)  # Create a new window
        new_window.title("Decrypt")
        new_window.geometry("600x400")

        decrypt_ui_rachel.populate_window(new_window)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    EnigmaGameUI(root)
    root.mainloop()

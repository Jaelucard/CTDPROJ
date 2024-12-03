from tkinter import *
from tkinter import ttk

def open_new_window():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("New Page")
    new_window.geometry("300x200")
    
    # Add widgets to the new window
    ttk.Label(new_window, text="Welcome to the new page!", font=("Helvetica", 14)).pack(pady=20)
    ttk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

# Create the main window
root = Tk()
root.title("Main Page")
root.geometry("400x300")

# Create a button to open the new window
open_button = ttk.Button(root, text="Go to New Page", command=open_new_window)
open_button.pack(pady=50)

root.mainloop()

 
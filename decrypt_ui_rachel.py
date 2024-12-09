from tkinter import ttk

def populate_window(window):
    # Add widgets to the new window
    label = ttk.Label(window, text="Decryption Page", font=("Helvetica", 16, "bold"))
    label.pack(pady=20)
    
    # Add input field for decryption
    decrypt1_label = ttk.Label(window, text="The Decrypted Message:", font=("Helvetica", 12))
    decrypt1_label.pack(pady=5)
    
    decrypt_input = ttk.Entry(window, width=30)
    decrypt_input.pack(pady=5)

    # To replace
    def decrypt_message():
        message = decrypt_input.get()
        # Placeholder for encryption logic (reversing the message here)
        decrypted_message = message[::-1]
        decrypted_output.config(text=decrypted_message)  # Update the encrypted message label

    # Button to perform decryption (example placeholder)
    decrypt_button = ttk.Button(window, text="Decrypt",command=decrypt_message)
    decrypt_button.pack(pady=10)

    # Label to show the encrypted message (initially empty)
    decrypted_label = ttk.Label(window, text="Final Output: ", font=("Helvetica", 12))
    decrypted_label.pack(pady=5)

    # Label to display the actual encrypted message output
    decrypted_output = ttk.Label(window, text="", font=("Helvetica", 12, "italic"), foreground="blue")
    decrypted_output.pack(pady=5)
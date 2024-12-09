from tkinter import ttk

def populate_window(window):
    # Add widgets to the new window
    label = ttk.Label(window, text="Encryption Page", font=("Helvetica", 16, "bold"))
    label.pack(pady=20)
    
    # Add input field for encryption
    encrypt_label = ttk.Label(window, text="Enter Message to Encrypt:", font=("Helvetica", 12))
    encrypt_label.pack(pady=5)
    
    encrypt_input = ttk.Entry(window, width=30)
    encrypt_input.pack(pady=5)

    # Row frame for buttons (fixed reference to `window`)
    row_frame = ttk.Frame(window)
    row_frame.pack(pady=10)

    # Label to show the encrypted message (initially empty)
    encrypted_label = ttk.Label(window, text="Encrypted Message: ", font=("Helvetica", 12))
    encrypted_label.pack(pady=5)

    # Label to display the actual encrypted message output
    encrypted_output = ttk.Label(window, text="", font=("Helvetica", 12, "italic"), foreground="blue")
    encrypted_output.pack(pady=5)

    # To replace
    def encrypt_message():
        message = encrypt_input.get()
        # Placeholder for encryption logic (reversing the message here)
        encrypted_message = message[::-1]
        encrypted_output.config(text=encrypted_message)  # Update the encrypted message label

    encrypt_button = ttk.Button(row_frame, text="Encrypt", command=encrypt_message)
    encrypt_button.pack(side="left", padx=5)

    # Optionally add a button to return to the main UI
    close_button = ttk.Button(row_frame, text="Close", command=window.destroy)
    close_button.pack(side="left", padx=5)
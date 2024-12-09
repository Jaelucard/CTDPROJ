from tkinter import ttk
from validation import Validation as val
from encryptDecrypt import EnigmaCipher as enig

def populate_window(window):
    # Add widgets to the new window
    label = ttk.Label(window, text="Encryption Page", font=("Helvetica", 16, "bold"))
    label.pack(pady=20)

    sub_label = ttk.Label(window, 
                      text="--------------------------USER GUIDE--------------------------\n"
                      "A linear function takes the form of mx + c, where m is the number of times we split the list and c is the translation to the left or right.\n"
                      "Please note the vowels and first and last letters of the message will not be encrypted.\n"
                      , font=("Helvetica", 10, "bold"),
                      justify="center",
                      anchor="center",
                      )
    sub_label.pack(pady=20)
    
    # Add input field for encryption
    encrypt_label = ttk.Label(window, text= "What is your message? "
                              "\nPlease input a linear function for your encryption!"
                              , font=("Helvetica", 12))
    encrypt_label.pack(pady=5)
    
    encrypt_input = ttk.Entry(window, width=30)
    encrypt_input.pack(pady=10)

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

        #validate inputs for m and c
        #gradientvalue = val.get_integer_input("Input a value for m: ",'m')
        #interceptvalue = val.get_integer_input("Input a value for c: ",'c')

        #initial alphabet without vowels
        #alphabet = {
                    #0: 'b', 1: 'c', 2: 'd', 3: 'f', 4: 'g', 5: 'h', 6: 'j', 7: 'k',
                   # 8: 'l', 9: 'm', 10: 'n', 11: 'p', 12: 'q', 13: 'r', 14: 's', 
                   # 15: 't', 16: 'v', 17: 'w', 18: 'x', 19: 'y', 20: 'z'
               # }
        
        #3cipher = EnigmaCipher(message, gradientvalue, interceptvalue, endecrypt=1, alphabet=alphabet)
        #encrypted_message, shifted_alphabet = cipher.encryptEnigma() 
        # Placeholder for encryption logic (reversing the message here)
        encrypted_message = message[::-1]
        encrypted_output.config(text=encrypted_message)  # Update the encrypted message label

    encrypt_button = ttk.Button(row_frame, text="Encrypt", command=encrypt_message)
    encrypt_button.pack(side="left", padx=5)

    # Optionally add a button to return to the main UI
    close_button = ttk.Button(row_frame, text="Close", command=window.destroy)
    close_button.pack(side="left", padx=5)
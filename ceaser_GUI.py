import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                shifted = (ord(char) - ascii_offset + shift) % 26
            else:
                shifted = (ord(char) - ascii_offset - shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def perform_cipher():
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
        if not (1 <= shift <= 25):
            raise ValueError("Shift value must be between 1 and 25.")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        return
    
    mode = mode_var.get()
    result = caesar_cipher(text, shift, 'encrypt' if mode == 'e' else 'decrypt')
    result_label.config(text=f"Result: {result}")

# Main window
root = tk.Tk()
root.title("Caesar Cipher")
root.configure(bg="#2C3E50")

title_frame = tk.Frame(root, bg="#1d8ed3", padx=20, pady=10)
title_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# Title Labels
title_label0 = tk.Label(title_frame, text="Prodigy Infotech", font=("Arial", 18), fg="#ECF0F1", bg="#1d8ed3")
title_label1 = tk.Label(title_frame, text="Divine Dzandu", font=("Arial", 14), fg="#ECF0F1", bg="#1d8ed3")
title_label2 = tk.Label(title_frame, text="Caesar Cipher", font=("Arial", 20, "bold"), fg="#ECF0F1", bg="#1d8ed3")
title_label0.pack(side="top", pady=(0, 5))
title_label1.pack(side="top", pady=5)
title_label2.pack(side="top", pady=(5, 10))

# Text input
text_label = tk.Label(root, text="Enter the message:", fg="#ECF0F1", bg="#2C3E50")
text_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
text_entry = tk.Entry(root, width=40, bg="#34495E", fg="#ECF0F1", insertbackground="#ECF0F1")
text_entry.grid(row=1, column=1, padx=10, pady=5)

# Shift value input
shift_label = tk.Label(root, text="Enter the shift value (1-25):", fg="#ECF0F1", bg="#2C3E50")
shift_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
shift_entry = tk.Entry(root, width=5, bg="#34495E", fg="#ECF0F1", insertbackground="#ECF0F1")
shift_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Mode selection
mode_var = tk.StringVar(value='e')
encrypt_radiobutton = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value='e', fg="#ECF0F1", bg="#2C3E50", selectcolor="#34495E")
decrypt_radiobutton = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value='d', fg="#ECF0F1", bg="#2C3E50", selectcolor="#34495E")
encrypt_radiobutton.grid(row=3, column=0, padx=10, pady=5, sticky='e')
decrypt_radiobutton.grid(row=3, column=1, padx=10, pady=5, sticky='w')

perform_button = tk.Button(root, text="Perform Cipher", command=perform_cipher, bg="#E74C3C", fg="#ECF0F1", activebackground="#C0392B", activeforeground="#ECF0F1")
perform_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result:", fg="#ECF0F1", bg="#2C3E50")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

info_label = tk.Label(root, text="Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.", wraplength=400, fg="#ECF0F1", bg="#2C3E50", justify="left")
info_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

root.mainloop()

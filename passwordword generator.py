#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string
import tkinter as tk
from tkinter import messagebox

# Password generation logic
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# GUI mode
def launch_gui():
    def on_generate():
        try:
            length = int(length_entry.get())
            password = generate_password(
                length,
                upper_var.get(),
                lower_var.get(),
                digits_var.get(),
                special_var.get()
            )
            result_var.set(password)
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x300")

    tk.Label(root, text="Password Length:").pack(pady=5)
    length_entry = tk.Entry(root)
    length_entry.pack()

    upper_var = tk.BooleanVar(value=True)
    lower_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    special_var = tk.BooleanVar(value=False)

    tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w')
    tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w')
    tk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor='w')
    tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w')

    tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)

    result_var = tk.StringVar()
    tk.Entry(root, textvariable=result_var, width=40, font=('Arial', 12)).pack(pady=10)

    root.mainloop()

# CLI mode
def launch_cli():
    try:
        print("\n=== Password Generator (CLI Mode) ===")
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    print("Choose mode:\n1. Command-line Interface (CLI)\n2. Graphical User Interface (GUI)")
    mode = input("Enter 1 or 2: ").strip()
    if mode == '1':
        launch_cli()
    elif mode == '2':
        launch_gui()
    else:
        print("Invalid selection. Please enter 1 or 2.")


# In[ ]:





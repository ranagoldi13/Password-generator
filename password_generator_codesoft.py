import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate the password
def create_password():
    user_input = length_entry.get()
    if not user_input.isdigit() or int(user_input) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return

    length = int(user_input)
    charset = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choices(charset, k=length))

    password_output.config(state='normal')
    password_output.delete(0, tk.END)
    password_output.insert(0, result)
    password_output.config(state='readonly')

# Function to copy password to clipboard
def copy_password():
    pwd = password_output.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x320")
root.configure(bg="#e9f5ff")
root.resizable(False, False)

# Title Heading
title_label = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Helvetica", 16, "bold"),
    bg="#e9f5ff",
    fg="#2b3e50"
)
title_label.pack(pady=15)

# Input Frame
input_frame = tk.Frame(root, bg="#e9f5ff")
input_frame.pack()

length_label = tk.Label(input_frame, text="Password Length:", font=("Arial", 12), bg="#e9f5ff")
length_label.pack(side="left", padx=5)

length_entry = tk.Entry(input_frame, font=("Arial", 12), width=8)
length_entry.pack(side="left")

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11),
    bg="#1B801F",
    fg="white",
    activebackground="#45a049",
    width=20,
    command=create_password
)
generate_btn.pack(pady=20)

# Output Field
password_output = tk.Entry(root, font=("Courier", 12), width=38, justify="center", state='readonly', bd=2, relief="sunken")
password_output.pack(pady=5)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Arial", 11),
    bg="#303A05",
    fg="white",
    activebackground="#1976D2",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

# Start GUI loop
root.mainloop()

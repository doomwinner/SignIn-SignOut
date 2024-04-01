import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create a database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

# Function to handle sign up
def sign_up():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if email == '' or password == '' or confirm_password == '':
        messagebox.showerror("Error", "Please fill in all fields")
        return

    if '@' not in email or '.' not in email:
        messagebox.showerror("Error", "Invalid email address")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Sign up successful!")

# Function to handle sign in
def sign_in():
    email = email_signin_entry.get()
    password = password_signin_entry.get()

    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Email or password incorrect")

# Create database table if not exists
create_table()

# Create sign up window
sign_up_window = tk.Tk()
sign_up_window.title("Sign Up")

email_label = tk.Label(sign_up_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(sign_up_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(sign_up_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(sign_up_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

confirm_password_label = tk.Label(sign_up_window, text="Confirm Password:")
confirm_password_label.grid(row=2, column=0, padx=10, pady=5)
confirm_password_entry = tk.Entry(sign_up_window, show="*")
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(sign_up_window, text="Submit", command=sign_up)
submit_button.grid(row=3, columnspan=2, padx=10, pady=5)

# Create sign in window
sign_in_window = tk.Tk()
sign_in_window.title("Sign In")

email_signin_label = tk.Label(sign_in_window, text="Email:")
email_signin_label.grid(row=0, column=0, padx=10, pady=5)
email_signin_entry = tk.Entry(sign_in_window)
email_signin_entry.grid(row=0, column=1, padx=10, pady=5)

password_signin_label = tk.Label(sign_in_window, text="Password:")
password_signin_label.grid(row=1, column=0, padx=10, pady=5)
password_signin_entry = tk.Entry(sign_in_window, show="*")
password_signin_entry.grid(row=1, column=1, padx=10, pady=5)

signin_button = tk.Button(sign_in_window, text="Sign In", command=sign_in)
signin_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Start GUI loop
sign_up_window.mainloop()

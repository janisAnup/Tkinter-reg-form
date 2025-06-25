# main.py

import customtkinter as ctk
import tkinter.messagebox as msg
import designs

# Initialize CustomTkinter theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window
window = ctk.CTk()
window.title("Registration Form")
window.geometry("400x400")
window.configure(fg_color=designs.bg_color)

# Title
label_title = ctk.CTkLabel(
    window, 
    text="Register Now", 
    font=designs.font_title
)
label_title.pack(pady=15)

# Name
label_name = ctk.CTkLabel(
    window, 
    text="Name", 
    font=designs.font_label
)
label_name.pack()

entry_name = ctk.CTkEntry(
    window, 
    width=designs.entry_width, 
    font=designs.font_entry,
    placeholder_text="Enter your name"
)
entry_name.pack(pady=5)

# Email
label_email = ctk.CTkLabel(
    window, 
    text="Email", 
    font=designs.font_label
)
label_email.pack()

entry_email = ctk.CTkEntry(
    window, 
    width=designs.entry_width, 
    font=designs.font_entry,
    placeholder_text="Enter your email"
)
entry_email.pack(pady=5)

# Password
label_password = ctk.CTkLabel(
    window, 
    text="Password", 
    font=designs.font_label
)
label_password.pack()

entry_password = ctk.CTkEntry(
    window, 
    width=designs.entry_width, 
    font=designs.font_entry,
    show="*",
    placeholder_text="Enter password"
)
entry_password.pack(pady=5)

# Submit Function
def submit():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if name and email and password:
        msg.showinfo("Success", f"Welcome {name}!\nYou have registered successfully.")
        # Clear fields
        entry_name.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_password.delete(0, 'end')
    else:
        msg.showwarning("Missing Info", "Please fill in all fields.")

# Submit Button
submit_btn = ctk.CTkButton(
    window,
    text="Submit",
    font=designs.font_button,
    fg_color=designs.button_color,
    command=submit
)
submit_btn.pack(pady=20)

window.mainloop()


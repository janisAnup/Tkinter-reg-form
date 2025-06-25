import tkinter as tk
from tkinter import messagebox
import designs

window = tk.Tk()
window.title("Modern Registration Form")
window.geometry("400x600")
window.configure(bg=designs.bg_color)

# Title
tk.Label(window, text="Register Now", font=("Arial", 16, "bold"), bg=designs.bg_color).pack(pady=10)

# Name
tk.Label(window, text="Name", font=designs.label_font, bg=designs.bg_color).pack()
entry_name = tk.Entry(window, width=designs.entry_width, font=designs.entry_font)
entry_name.pack()

# Email
tk.Label(window, text="Email", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
entry_email = tk.Entry(window, width=designs.entry_width, font=designs.entry_font)
entry_email.pack()

# Password
tk.Label(window, text="Password", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
entry_password = tk.Entry(window, width=designs.entry_width, font=designs.entry_font, show="*")
entry_password.pack()

# Confirm Password
tk.Label(window, text="Confirm Password", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
entry_confirm = tk.Entry(window, width=designs.entry_width, font=designs.entry_font, show="*")
entry_confirm.pack()

# Age
tk.Label(window, text="Age", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
entry_age = tk.Entry(window, width=designs.entry_width, font=designs.entry_font)
entry_age.pack()

# Gender
tk.Label(window, text="Gender", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
gender_var = tk.StringVar(value="None")
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", bg=designs.bg_color).pack()
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", bg=designs.bg_color).pack()
tk.Radiobutton(window, text="Other", variable=gender_var, value="Other", bg=designs.bg_color).pack()

# Country Dropdown
tk.Label(window, text="Country", font=designs.label_font, bg=designs.bg_color).pack(pady=(10, 0))
country_var = tk.StringVar()
country_dropdown = tk.OptionMenu(window, country_var, "India", "USA", "UK", "Canada", "Australia")
country_dropdown.config(width=28, font=designs.entry_font)
country_dropdown.pack()

# Terms Checkbox
terms_var = tk.IntVar()
tk.Checkbutton(window, text="I agree to the Terms & Conditions", variable=terms_var, bg=designs.bg_color).pack(pady=(10, 0))

# Submit Button
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm = entry_confirm.get()
    age = entry_age.get()
    gender = gender_var.get()
    country = country_var.get()

    if not (name and email and password and confirm and age and gender != "None" and country):
        messagebox.showwarning("Error", "Please fill in all fields.")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
    elif terms_var.get() == 0:
        messagebox.showwarning("Error", "You must accept the Terms & Conditions.")
    else:
        messagebox.showinfo("Success", f"Welcome {name}!\nYou are registered.")
        # Clear entries
        entry_name.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_password.delete(0, 'end')
        entry_confirm.delete(0, 'end')
        entry_age.delete(0, 'end')
        gender_var.set("None")
        country_var.set("")
        terms_var.set(0)

tk.Button(window, text="Submit", command=submit_form,
          bg=designs.btn_bg, fg=designs.btn_fg, font=designs.button_font).pack(pady=20)

window.mainloop()

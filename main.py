import tkinter as tk
from tkinter import messagebox
import designs

window = tk.Tk()
window.title("Stylish Registration Form")
window.geometry("420x620")
window.configure(bg=designs.bg_color)

# Title
tk.Label(window, text="Register Now", font=("Segoe UI", 16, "bold"),
         bg=designs.bg_color, fg="#66fcf1").pack(pady=15)

def create_labeled_entry(label_text):
    tk.Label(window, text=label_text, font=designs.label_font,
             bg=designs.bg_color, fg=designs.label_color).pack(pady=(10, 2))
    entry = tk.Entry(window, width=designs.entry_width, font=designs.entry_font,
                     bg=designs.entry_bg, fg=designs.entry_fg, insertbackground=designs.entry_fg)
    entry.pack()
    return entry

entry_name = create_labeled_entry("Name")
entry_email = create_labeled_entry("Email")
entry_password = create_labeled_entry("Password")
entry_password.config(show="*")
entry_confirm = create_labeled_entry("Confirm Password")
entry_confirm.config(show="*")
entry_age = create_labeled_entry("Age")

# Gender
tk.Label(window, text="Gender", font=designs.label_font,
         bg=designs.bg_color, fg=designs.label_color).pack(pady=(10, 2))
gender_var = tk.StringVar(value="None")
gender_frame = tk.Frame(window, bg=designs.bg_color)
gender_frame.pack()
for gender in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=gender, variable=gender_var, value=gender,
                   bg=designs.bg_color, fg=designs.label_color, selectcolor=designs.bg_color).pack(side="left", padx=10)

# Country Dropdown
tk.Label(window, text="Country", font=designs.label_font,
         bg=designs.bg_color, fg=designs.label_color).pack(pady=(10, 2))
country_var = tk.StringVar()
country_menu = tk.OptionMenu(window, country_var, "India", "USA", "UK", "Canada", "Germany")
country_menu.config(font=designs.entry_font, width=28, bg=designs.entry_bg, fg=designs.entry_fg)
country_menu.pack()

# Terms
terms_var = tk.IntVar()
tk.Checkbutton(window, text="I agree to the Terms & Conditions", variable=terms_var,
               bg=designs.bg_color, fg=designs.checkbox_color, activebackground=designs.bg_color,
               activeforeground=designs.checkbox_color, selectcolor=designs.bg_color).pack(pady=10)

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


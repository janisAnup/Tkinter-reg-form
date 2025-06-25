import tkinter as tk
import designs  # ✅ This now points to designs.py instead of css.py

# Main window
window = tk.Tk()
window.title("Styled Form")
window.configure(bg=designs.bg_color)
window.geometry("300x250")

# Name Label and Entry
tk.Label(window, text="Name", font=designs.font_label, bg=designs.bg_color).pack()
entry_name = tk.Entry(window, font=designs.font_entry, bg=designs.entry_bg, fg=designs.entry_fg, width=designs.entry_width)
entry_name.pack(pady=5)

# Email Label and Entry
tk.Label(window, text="Email", font=designs.font_label, bg=designs.bg_color).pack()
entry_email = tk.Entry(window, font=designs.font_entry, bg=designs.entry_bg, fg=designs.entry_fg, width=designs.entry_width)
entry_email.pack(pady=5)

# Submit Button
def submit():
    print("Name:", entry_name.get())
    print("Email:", entry_email.get())

tk.Button(window, text="Submit", command=submit, bg=designs.btn_color, fg=designs.btn_text).pack(pady=10)

window.mainloop()


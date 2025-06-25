import tkinter as tk  # Import the tkinter module

# Create the main window
window = tk.Tk()
window.title("Registration Form")  # Title for the window
window.geometry("300x250")  # Size of the window

# Create a label and entry for Name
label_name = tk.Label(window, text="Name")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

# Create a label and entry for Email
label_email = tk.Label(window, text="Email")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

# Create a label and entry for Password
label_password = tk.Label(window, text="Password")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a label and entry for Age
label_age = tk.Label(window, text="Age")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

# Define what happens when we click the button
def submit():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    age = entry_age.get()

    print("----- Registration Info -----")
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)
    print("Age:", age)

# Create a Submit Button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

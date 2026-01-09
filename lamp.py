import tkinter as tk

root = tk.Tk()
root.title("Lamp control")

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if(username == "Elisee" and password == "jefazo"):
        root.withdraw()
        open_dashboard()

def open_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Control lamp")

    on_button = tk.Button(
        dashboard,
        text="ON",
        command=toggle_on
    )
    on_button.pack()

    off_button = tk.Button(
        dashboard,
        text="OFF",
        command = toggle_off
        # message.config(text="Lamp ON")
    )
    off_button.pack()
    message = tk.Label(dashboard, text="")
    message.pack()

def toggle_on():
    # message.config(dashboard, text="Lamp ON")
    print("ON button clicked")

def toggle_off():
    # message.config(dashboard, text="Lamp OFF")
    print("Off button clicked")

label = tk.Label(
    root,
    text="Welcome to lamp ocontrol page!!",
    fg="blue"
    ).pack()

label = tk.Label(
    root,
    text="Username"
    ).pack()

username_entry = tk.Entry(root)
username_entry.pack()

label = tk.Label(root,
    text="Password"
    ).pack()
password_entry = tk.Entry(
    root,
    show="*"
    )
password_entry.pack()

login_button = tk.Button(
    root,
    text="Login",
    command=check_credentials
)
login_button.pack()

root.mainloop()
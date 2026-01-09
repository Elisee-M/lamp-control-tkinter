import tkinter as tk

root = tk.Tk()
root.title("Lamp Control")

message = None  

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Elisee" and password == "jefazo":
        root.withdraw()
        open_dashboard()
    else:
        print("Wrong credentials")

def open_dashboard():
    global message

    dashboard = tk.Toplevel(root)
    dashboard.title("Control Lamp")

    on_button = tk.Button(
        dashboard,
        text="ON",
        width=10,
        command=toggle_on
    )
    on_button.pack(pady=5)

    off_button = tk.Button(
        dashboard,
        text="OFF",
        width=10,
        command=toggle_off
    )
    off_button.pack(pady=5)

    message = tk.Label(dashboard, text="Lamp is OFF", fg="red")
    message.pack(pady=10)

def toggle_on():
    message.config(text="Lamp is ON", fg="green")
    print("ON button clicked")

def toggle_off():
    message.config(text="Lamp is OFF", fg="red")
    print("OFF button clicked")

tk.Label(
    root,
    text="Welcome to lamp control page!!",
    fg="blue"
).pack(pady=10)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(
    root,
    text="Login",
    command=check_credentials
)
login_button.pack(pady=10)

root.mainloop()

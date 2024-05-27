import random
import string
import tkinter as tk
import Model.Users as db

def SaveUser(id, title, username, password, note):
    conn = db.connect()
    db.update_user(conn, id, title, username, password, note)
    db.close_connection(conn)
    add_user_window.destroy()

def GeneratePassword(Length):
    Letters = string.ascii_letters + string.digits + "@" + "!" + "&"
    entry_password.delete("0", tk.END)
    Password = ""
    for i in range(Length):
        Password += random.choice(Letters)

    entry_password.insert(tk.END, Password)

def ShowEditForm(root, id, title, username, password, note):

    global add_user_window
    add_user_window = tk.Toplevel(root)
    add_user_window.title("Add New User")

    window_width = 500
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    add_user_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    tk.Label(add_user_window, text="Title:").grid(row=0, column=0, padx=5, pady=5)
    entry_title = tk.Entry(add_user_window, width=30, justify=tk.CENTER, font=("Arial", 15))
    entry_title.grid(row=0, column=1, padx=50, pady=20)
    entry_title.insert(tk.END, title)

    tk.Label(add_user_window, text="Username:").grid(row=1, column=0, padx=5, pady=5)
    entry_username = tk.Entry(add_user_window, width=30, justify=tk.CENTER, font=("Arial", 15))
    entry_username.grid(row=1, column=1, padx=50, pady=20)
    entry_username.insert(tk.END, username)

    tk.Label(add_user_window, text="Password:").grid(row=2, column=0, padx=5, pady=5)
    global entry_password
    entry_password = tk.Entry(add_user_window, width=30, justify=tk.CENTER, font=("Arial", 15))
    entry_password.grid(row=2, column=1, padx=50, pady=20)
    entry_password.insert(tk.END, password)

    tk.Label(add_user_window, text="Length:").grid(row=3, column=0, padx=5, pady=5)
    entry_generatePasswordNum = tk.Spinbox(add_user_window ,from_=8, to=50, width=5, font=("Arial", 10))
    entry_generatePasswordNum.grid(row=3, column=1, padx=50, pady=0, sticky=tk.W)

    entry_generatePassword = tk.Button(add_user_window, text="Generate Password", width=35, command=lambda: GeneratePassword(int(entry_generatePasswordNum.get())))
    entry_generatePassword.grid(row=3, column=1, padx=50, pady=0,sticky=tk.E)

    tk.Label(add_user_window, text="Note:").grid(row=4, column=0, padx=5, pady=5)
    entry_note = tk.Entry(add_user_window, width=30, justify=tk.CENTER, font=("Arial", 15))
    entry_note.grid(row=4, column=1, padx=50, pady=15)
    entry_note.insert(tk.END, note)

    btn_save = tk.Button(add_user_window, text="Save", width=35,command=lambda: SaveUser(id,entry_title.get(),entry_username.get(),entry_password.get(),entry_note.get()))
    btn_save.grid(row=5, column=0, columnspan=2, pady=10)

    return add_user_window
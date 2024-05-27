import tkinter as tk
from tkinter import ttk, Menu, messagebox
import Model.Users as db
import View.AddNewForm as AddNewForm
import View.EditForm as EditForm

def load_users():
    conn = db.connect()
    db.create_table(conn)
    users = db.get_all_users(conn)
    for row in tree.get_children():
        tree.delete(row)

    for user in users:
        tree.insert('', 'end', values=user)
    db.close_connection(conn)

def ShowAddNewUserForm():
    window = AddNewForm.ShowAddNewForm(root)
    root.wait_window(window)
    load_users()

def EditUserForm():
    SelectedUser = tree.selection()
    if SelectedUser:
        item = tree.item(SelectedUser[0])
        userid = item['values'][0]
        conn = db.connect()
        user = db.get_user(conn,int(userid))
        db.close_connection(conn)
        window = EditForm.ShowEditForm(root,user[0],user[1],user[2],user[3],user[4])
        root.wait_window(window)

        load_users()

def DeleteUser(event=None):
    SelectedUser = tree.selection()
    if SelectedUser:
        item = tree.item(SelectedUser[0])
        userid = item['values'][0]
        response = messagebox.askyesno("Delete Confirmation", "آیا میخواهید داده مورد نظر رو پاک کنید؟")
        if response:
            conn = db.connect()
            user = db.delete_user(conn,int(userid))
            db.close_connection(conn)
            load_users()

def copy_password(event=None):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        password = item['values'][3]
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password has been copied to clipboard")


root = tk.Tk()
root.title("Password Manager")
root.geometry("1300x700")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: ShowAddNewUserForm())
file_menu.add_command(label="Edit", command=lambda: EditUserForm())
file_menu.add_command(label="Delete", command=lambda:DeleteUser())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

columns = ('id','Title', 'Username', 'Password', 'Notes')
tree = ttk.Treeview(frame, columns=columns, show='headings')

tree.heading('id', text='id')
tree.heading('Title', text='Title')
tree.heading('Username', text='Username')
tree.heading('Password', text='Password')
tree.heading('Notes', text='Notes')

tree.column('id', width=100)
tree.column('Title', width=100)
tree.column('Username', width=100)
tree.column('Password', width=100)
tree.column('Notes', width=200)

scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')
tree.pack(fill='both', expand=True)

popup_menu = Menu(root, tearoff=0)
popup_menu.add_command(label="New", command=lambda:ShowAddNewUserForm())
popup_menu.add_command(label="Edit", command=lambda:EditUserForm())
popup_menu.add_command(label="Delete", command=lambda:DeleteUser())

def show_popup(event):
    try:
        popup_menu.tk_popup(event.x_root, event.y_root)
    finally:
        popup_menu.grab_release()

tree.bind("<Button-3>", show_popup)
root.bind('<Control-c>', copy_password)
root.bind('<Delete>', DeleteUser)
load_users()

root.mainloop()
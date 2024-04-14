import tkinter as tk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (name TEXT, phone TEXT, email TEXT)''')
conn.commit()


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    c.execute("INSERT INTO contacts VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    messagebox.showinfo("Success", "Contact added successfully")
    clear_entries()

def view_contacts():
    c.execute("SELECT * FROM contacts")
    records = c.fetchall()
    listbox_contacts.delete(0, tk.END)
    for row in records:
        listbox_contacts.insert(tk.END, row)

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Manager")


tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)


tk.Label(root, text="Phone").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)


tk.Label(root, text="Email").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)


button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.grid(row=3, column=0)
button_view = tk.Button(root, text="View Contacts", command=view_contacts)
button_view.grid(row=3, column=1)


listbox_contacts = tk.Listbox(root)
listbox_contacts.grid(row=4, column=0, columnspan=2)


root.mainloop()

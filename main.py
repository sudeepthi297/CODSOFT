
import tkinter as tk
from tkinter import ttk, messagebox


# -------------------------------
# 1. Create the main application
# -------------------------------

root = tk.Tk()
root.title("Contact Management System")
root.geometry("1050x650")
root.minsize(850, 550)
root.configure(bg="#F2F5F9")


# -------------------------------
# 2. Application heading
# -------------------------------

heading = tk.Label(
    root,
    text="Contact Management System",
    font=("Arial", 22, "bold"),
    bg="#F2F5F9",
    fg="#1F3A5F"
)
heading.pack(pady=15)


# -------------------------------
# 3. Contact form
# -------------------------------

form_frame = ttk.LabelFrame(
    root,
    text="Contact Details",
    padding=15
)
form_frame.pack(fill="x", padx=20, pady=5)

# Name
ttk.Label(form_frame, text="Full Name:").grid(
    row=0, column=0, sticky="w", padx=5, pady=8
)
name_entry = ttk.Entry(form_frame, width=35)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

# Phone
ttk.Label(form_frame, text="Phone Number:").grid(
    row=0, column=2, sticky="w", padx=5, pady=8
)
phone_entry = ttk.Entry(form_frame, width=35)
phone_entry.grid(row=0, column=3, sticky="ew", padx=5, pady=8)

# Email
ttk.Label(form_frame, text="Email Address:").grid(
    row=1, column=0, sticky="w", padx=5, pady=8
)
email_entry = ttk.Entry(form_frame, width=35)
email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=8)

# Address
ttk.Label(form_frame, text="Home Address:").grid(
    row=1, column=2, sticky="w", padx=5, pady=8
)
address_entry = ttk.Entry(form_frame, width=35)
address_entry.grid(row=1, column=3, sticky="ew", padx=5, pady=8)

for column in (1, 3):
    form_frame.columnconfigure(column, weight=1)


# -------------------------------
# 4. Search section
# -------------------------------

search_frame = ttk.Frame(root, padding=(20, 10))
search_frame.pack(fill="x")

ttk.Label(
    search_frame,
    text="Search by name or phone:"
).pack(side="left", padx=(0, 8))

search_entry = ttk.Entry(search_frame, width=35)
search_entry.pack(side="left", padx=5)


# -------------------------------
# 5. Contact table
# -------------------------------

table_frame = ttk.LabelFrame(
    root,
    text="Saved Contacts",
    padding=10
)
table_frame.pack(fill="both", expand=True, padx=20, pady=5)

columns = ("ID", "Name", "Phone", "Email", "Address")

contact_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

contact_table.heading("ID", text="Contact ID")
contact_table.heading("Name", text="Full Name")
contact_table.heading("Phone", text="Phone Number")
contact_table.heading("Email", text="Email Address")
contact_table.heading("Address", text="Home Address")

contact_table.column("ID", width=80, anchor="center")
contact_table.column("Name", width=180)
contact_table.column("Phone", width=140)
contact_table.column("Email", width=220)
contact_table.column("Address", width=260)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=contact_table.yview
)
contact_table.configure(yscrollcommand=scrollbar.set)

contact_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# -------------------------------
# 6. Temporary button functions
# -------------------------------

def add_contact():
    messagebox.showinfo(
        "Information",
        "Add Contact will be implemented in Session 2."
    )


def update_contact():
    messagebox.showinfo(
        "Information",
        "Update Contact will be implemented in Session 2."
    )


def delete_contact():
    messagebox.showinfo(
        "Information",
        "Delete Contact will be implemented in Session 2."
    )


def search_contact():
    messagebox.showinfo(
        "Information",
        "Search Contact will be implemented in Session 3."
    )


def clear_form():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

    selected_items = contact_table.selection()
    if selected_items:
        contact_table.selection_remove(*selected_items)


# -------------------------------
# 7. Application buttons
# -------------------------------

button_frame = ttk.Frame(root, padding=10)
button_frame.pack(pady=5)

ttk.Button(
    button_frame,
    text="Add Contact",
    command=add_contact
).grid(row=0, column=0, padx=6)

ttk.Button(
    button_frame,
    text="Update Contact",
    command=update_contact
).grid(row=0, column=1, padx=6)

ttk.Button(
    button_frame,
    text="Delete Contact",
    command=delete_contact
).grid(row=0, column=2, padx=6)

ttk.Button(
    button_frame,
    text="Search",
    command=search_contact
).grid(row=0, column=3, padx=6)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_form
).grid(row=0, column=4, padx=6)


# -------------------------------
# 8. Start the application
# -------------------------------

root.mainloop()

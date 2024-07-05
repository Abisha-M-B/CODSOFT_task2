import tkinter as tk
from tkinter import messagebox


# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_list.append((name, phone))
        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please enter both name and phone number.')


# Function to update the listbox with contacts
def update_listbox():
    listbox.delete(0, tk.END)
    for contact in contact_list:
        listbox.insert(tk.END, f'{contact[0]} - {contact[1]}')


# Function to delete a selected contact
def delete_contact():
    try:
        index = listbox.curselection()[0]
        contact_list.pop(index)
        update_listbox()
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a contact to delete.')


# Function to search for a contact
def search_contact():
    query = search_entry.get().strip().lower()
    listbox.delete(0, tk.END)
    for contact in contact_list:
        if query in contact[0].lower():
            listbox.insert(tk.END, f'{contact[0]} - {contact[1]}')


# Create the main window
root = tk.Tk()
root.title('Contact Book')

# Contact list 
contact_list = []

# Frames
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

frame_list = tk.Frame(root)
frame_list.pack(padx=10, pady=5)

# Entry widgets
name_label = tk.Label(frame_input, text='Name:')
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

name_entry = tk.Entry(frame_input, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(frame_input, text='Phone:')
phone_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

phone_entry = tk.Entry(frame_input, width=15)
phone_entry.grid(row=0, column=3, padx=5, pady=5)

# Buttons
add_button = tk.Button(frame_input, text='Add Contact', command=add_contact, fg="white", bg="maroon")
add_button.grid(row=0, column=4, padx=5, pady=5)

delete_button = tk.Button(frame_list, text='Delete Contact', command=delete_contact, fg="white", bg="maroon")
delete_button.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(frame_list, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(frame_list, text='Search', command=search_contact, fg="white", bg="black")
search_button.pack(side=tk.LEFT, padx=5)

# Listbox to display contacts
listbox = tk.Listbox(frame_list, width=50, height=10)
listbox.pack(pady=10)

# Populate initial listbox
update_listbox()

# Run the main loop
root.mainloop()

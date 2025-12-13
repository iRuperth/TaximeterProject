import tkinter as tk
from tkinter import ttk
import main

root = tk.Tk()
root.title("Taximeter")
root.geometry('400x600')
# button = tk.Button(r, text='Start', width=25, command=r.destroy)
# button.pack()

title = tk.Label(root, text="Taximeter", font=("Arial", 18))
title.pack(padx=20, pady=20)

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

combo_box = ttk.Combobox(root, values=["Daytime", "Nightime"], state='readonly')
combo_box.pack(pady=5)
combo_box.set("Daytime")
combo_box.bind("<<ComboboxSelected>>", select)

label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

name_label = tk.Label(root, text="Passenger Name: ")
name_label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)


button = tk.Button(root, text="Start", relief="raised", width=25, bd=5, background="Green", foreground="black", font=("Arial", 10))
button.pack(pady=10, padx=10)

button = tk.Button(root, text="Stop", relief="raised", width=25, bd=5, background="yellow", foreground="black", font=("Arial", 10))
button.pack(pady=10, padx=10)

button = tk.Button(root, text="Finish", relief="raised", width=25, bd=5, background="red", foreground="black", font=("Arial", 10))
button.pack(pady=10, padx=10)




root.mainloop() 


#command=root.destroy
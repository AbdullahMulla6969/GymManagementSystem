# Gym Management System - Version 2.5 (Tkinter GUI Refactor)
import tkinter as tk
from tkinter import messagebox, ttk

member_records = {}

def add_member():
    m_id = id_entry.get().strip()
    name = name_entry.get().strip()
    plan = plan_entry.get().strip()
    status = status_combobox.get()
    
    if not m_id or not name or not plan:
        messagebox.showerror("Error", "All fields are required!")
        return
        
    if m_id in member_records:
        messagebox.showerror("Error", "Member ID already exists!")
        return
        
    member_records[m_id] = {"name": name, "plan": plan, "status": status}
    update_listbox()
    clear_entries()
    messagebox.showinfo("Success", "Member added successfully.")

def delete_member():
    m_id = id_entry.get().strip()
    if m_id in member_records:
        del member_records[m_id]
        update_listbox()
        clear_entries()
        messagebox.showinfo("Success", "Member removed successfully.")
    else:
        messagebox.showerror("Error", "Member ID not found.")

def update_listbox():
    listbox.delete(0, tk.END)
    for m_id, info in member_records.items():
        listbox.insert(tk.END, f"ID: {m_id} | Name: {info['name']} | Plan: {info['plan']} | Status: {info['status']}")

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    plan_entry.delete(0, tk.END)

# Window configuration
root = tk.Tk()
root.title("Gym Management System (v2.5)")
root.geometry("450x450")

# Layout Components
tk.Label(root, text="Member ID:").pack(pady=2)
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name:").pack(pady=2)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Plan:").pack(pady=2)
plan_entry = tk.Entry(root)
plan_entry.pack()

tk.Label(root, text="Status:").pack(pady=2)
status_combobox = ttk.Combobox(root, values=["Active", "Expired"], state="readonly")
status_combobox.set("Active")
status_combobox.pack()

# Control Buttons
tk.Button(root, text="Add Member", command=add_member, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Delete Member (by ID)", command=delete_member, bg="lightcoral").pack(pady=5)

# View Display
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()

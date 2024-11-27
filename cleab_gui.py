import tkinter as tk
from tkinter import filedialog, messagebox
from clean import clean

def process():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file:
        messagebox.showwarning("No File", "Select  CSV file to clean.")
        return

    out_dir = filedialog.askdirectory()
    if not out_dir:
        messagebox.showwarning("No Directory", "Select a directory to save the file.")
        return

    opt = choice.get()
    if opt == "1":
        cleaned_path = clean(file, opt="1", out_dir=out_dir)
    elif opt == "2":
        val = val_entry.get()
        if not val:
            messagebox.showwarning("No Value", "Enter a value to fill missing entries.")
            return
        cleaned_path = clean(file, opt="2", out_dir=out_dir, fill_val=val)
    else:
        messagebox.showwarning("Invalid Option", "Choose a valid option.")
        return

    if cleaned_path:
        messagebox.showinfo("Success", f"Cleaned file saved as: {cleaned_path}")
    else:
        messagebox.showerror("Error", "Cleaning failed.")

root = tk.Tk()
root.title("Cleaner")
root.geometry("400x400")

title = tk.Label(root, text="Cleaner", font=("Helvetica", 16))
title.pack(pady=10)

choice = tk.StringVar(value="1")

opt_label = tk.Label(root, text="Choose Option:")
opt_label.pack(pady=5)

opt1 = tk.Radiobutton(root, text="1. Drop rows with missing values", variable=choice, value="1")
opt1.pack()

opt2 = tk.Radiobutton(root, text="2. Fill missing values with a value", variable=choice, value="2")
opt2.pack()

val_label = tk.Label(root, text="Value to fill missing entries (Option 2):")
val_label.pack(pady=5)

val_entry = tk.Entry(root)
val_entry.pack()

btn = tk.Button(root, text="Select & Clean", command=process)
btn.pack(pady=20)

root.mainloop()

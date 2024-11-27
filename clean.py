import pandas as pd
import os

def load(file):
    try:
        data = pd.read_csv(file)
        print("CSV loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
        return None

def info(data):
    print("\nInfo:")
    print(data.info())
    print("\nFirst 5 Rows:")
    print(data.head())

def drop_na(data):
    clean = data.dropna()
    print("\nRows with missing values dropped.")
    return clean

def fill_na(data, val):
    filled = data.fillna(val)
    print(f"\nMissing values filled with {val}.")
    return filled

def save(data, out_dir, file_name):
    if not os.path.exists(out_dir):
        print(f"Error: Directory {out_dir} not found.")
        return None

    path = os.path.join(out_dir, file_name)
    data.to_csv(path, index=False)
    print(f"\nSaved cleaneddataset at {path}")
    return path

def clean(file, opt, out_dir, fill_val=None):
    data = load(file)
    if data is None:
        return None

    info(data)

    if opt == "1":
        cleaned = drop_na(data)
    elif opt == "2" and fill_val is not None:
        cleaned = fill_na(data, fill_val)
    else:
        print("Invalid choice.")
        return None

    name = f"cleaned_{os.path.basename(file)}"
    cleaned_path = save(cleaned, out_dir, name)
    return cleaned_path

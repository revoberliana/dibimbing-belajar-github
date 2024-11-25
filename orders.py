import pandas as pd
import os

def process_user_data(file_path):
    # Membaca file Excel atau CSV
    df = pd.read_csv(file_path)  # Ganti dengan read_csv jika formatnya CSV
    
    # Membuat dictionary
    user_data = {}
    for _, row in df.iterrows():
        username = row['Username']
        user_data[username] = {
            "Identifier": row['Identifier'],
            "First name": row['First name'],
            "Last name": row['Last name']
        }
    
    return user_data

# Contoh penggunaan
#file_path = "./username.csv"  # Sesuaikan dengan nama file Anda
file_path = os.path.join(os.path.dirname(__file__), "username.csv")
user_dict = process_user_data(file_path)
print(user_dict)

# Mendapatkan path absolut ke file CSV

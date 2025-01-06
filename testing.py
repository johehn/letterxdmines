import pandas as pd


excel_file_path = 'C:/Users/JustAvon/Desktop/Hidrolat.xlsx'


sheet_name = 'Sheet1'  # Вкажіть назву листа

# Читання даних з Excel у DataFrame
reviews_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Вивести перші 5 рядків для перевірки
print(reviews_df)

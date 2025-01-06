
import pandas as pd


excel_file_path = 'C:\Users\JustAvon\Downloads\reviews.xlsx'

sheet_name = 'Sheet1'  # Вкажіть назву листа

# Читання даних з Excel у DataFrame
reviews_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Вивести перші 5 рядків для перевірки
print(reviews_df.head())

# Припустимо, що файл містить стовпці: 'Film Title', 'Rating', 'Review', 'Review Link'
#for index, row in reviews_df.iterrows():
  #  film_title = row['Film Title']
 #   rating = row.get('Rating', 'N/A')  # Якщо рейтинг відсутній, використовувати 'N/A'
   # review_text = row['Review']
    #review_link = row['Review Link']

    # Форматування рецензії для Telegram
    #message = f"🎥 *{film_title}*\n⭐️ Rating: {rating}/10\n\n{review_text}\n\n[Read on Letterboxd]({review_link})"
    #print(message)



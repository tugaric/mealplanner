import sqlite3

conn = sqlite3.connect('mealplanner.db')
cursor = conn.execute("SELECT * from meal_ingredient")
data = cursor.fetchall()
for row in data:
    print(row)


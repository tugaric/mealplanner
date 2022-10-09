import sqlite3

class meal():
    def __init__(self, meal_name, meal_ingredients):
        self.meal_name = meal_name
        self.meal_ingredients = meal_ingredients

def get_meals():
# connect to the database
    conn = sqlite3.connect(r'db/mealplanner.db')
    # get a list of the meals with the ingredients
    cursor = conn.execute("SELECT * from meal_ingredient")
    meal_ingredients = cursor.fetchall()
    # get a list of all meals in the database
    cursor = conn.execute("SELECT description from meal")
    meal_list = cursor.fetchall()
    meals = []
    for meal_name in meal_list:
        ingredients = [ meal[1] for meal in meal_ingredients if meal[0]==meal_name[0]]
        my_meal = meal(meal_name[0], ingredients)
        meals.append(my_meal)
    return meals

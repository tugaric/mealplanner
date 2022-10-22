import sqlite3
from typing import Tuple, List

def get_data(sql_statement) -> Tuple[str]:
    conn = sqlite3.connect(r'db/mealplanner.db')
    # get a list of the meals with the ingredients
    cursor = conn.execute(sql_statement)
    data = cursor.fetchall()
    return data

# ["meal_1", "meal_2", ...]
def get_meal() -> List[str]:
    return [ meal[0] for meal in get_data("SELECT meal.description from meal")]

def get_recipe() -> Tuple[str]:
    return get_data("SELECT * from meal_ingredient")

def get_meal_ingredients(meal) -> Tuple[str]:
    return [ ingredient[0] for ingredient in get_data(f"SELECT ingredients from meal_ingredient where meal='{meal}'") ]

if __name__ == "__main__":
    pass
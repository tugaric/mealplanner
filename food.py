import sqlite3
import get_sql_data as gsd
from random import randint
from dataclasses import dataclass
from typing import List

MEAL_LIST = gsd.get_meal()

@dataclass
class ingredient():
    name: str

class recipe():
    def __init__(self, meal):
        self.meal = meal
        self.ingredients = gsd.get_meal_ingredients(meal)

class day_plan():
    def __init__(self)-> List[str]:
        self.meals = []

        for i in range(3):
            random_selection = randint(0, len(MEAL_LIST)-1)
            self.meals.append(MEAL_LIST[random_selection])

@dataclass
class week_plan():
    week: List[day_plan]

if __name__ == "__main__":
    my_day = day_plan()
    pass
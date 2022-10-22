import get_sql_data as gsd

if __name__ == "__main__":
    recipe              = gsd.get_recipe()
    list_of_ingredient  = gsd.get_ingredient()
    print(recipe)
def load_recipes(file_name):
    recipes = []
    with open(file_name, "r", encoding="utf8") as file:
        recipe_data = file.read().split("\n\n")
        for data in recipe_data:
            recipe_lines = data.strip().split('\n')
            recipe_name = recipe_lines[0].split(': ')[1]
            ingredients = recipe_lines[1].split(': ')[1].split(', ')
            directions = recipe_lines[2:]
            recipes.append({'recipe_name': recipe_name, 'ingredients': ingredients, 'directions': directions})
    return recipes
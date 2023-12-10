def find_matched_recipes(recipes, user_ingredients):
    return [recipe for recipe in recipes if all(ingredient in recipe['ingredients'] for ingredient in user_ingredients)]

def calculate_similarity(user_ingredients, recipe):
    ingredients_set = set(recipe['ingredients'])
    similarity = len(set(user_ingredients) & ingredients_set) / len(set(user_ingredients) | ingredients_set)
    return similarity

def find_similar_recipes(recipes, user_ingredients):
    similar_recipes = []
    for recipe in recipes:
        similarity = calculate_similarity(user_ingredients, recipe)
        similar_recipes.append((recipe, similarity))

    similar_recipes.sort(key=lambda x: x[1], reverse=True)
    return similar_recipes[:3]
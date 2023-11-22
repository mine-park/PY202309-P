# 레시피 데이터를 읽어오는 함수
def load_recipes(file_name):
    recipes = []
    file = open(file_name, "r", encoding="utf8")
    recipe_data = file.read().split("\n\n")
    for data in recipe_data:
        recipe_lines = data.strip().split('\n')
        recipe_name = recipe_lines[0].split(': ')[1]
        ingredients = recipe_lines[1].split(': ')[1].split(', ')
        directions = recipe_lines[2:]
        recipes.append({'recipe_name': recipe_name, 'ingredients': ingredients, 'directions': directions})
    return recipes

# 사용자 입력을 받아 재료 리스트로 변환
user_input = input("냉장고에 있는 재료 목록을 입력하세요 (띄어쓰기로 구분): ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(' ')]

# 레시피 데이터 파일명
recipe_file = "recipe.txt"

# 레시피 데이터를 불러옴
recipes = load_recipes(recipe_file)

# 사용자 입력과 일치하는 레시피를 찾기
matched_recipes = []
for recipe in recipes:
    if all(ingredient in recipe['ingredients'] for ingredient in user_ingredients):
        matched_recipes.append(recipe)

# 찾은 레시피 출력

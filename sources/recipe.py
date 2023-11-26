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

# 사용자 입력과 일치하는 레시피를 찾아서 출력
matched_recipes = []
for recipe in recipes:
    if all(ingredient in recipe['ingredients'] for ingredient in user_ingredients):
        matched_recipes.append(recipe)

if matched_recipes:
    print("\n냉장고 재료로 만들 수 있는 레시피 목록")
    print("------------------------------------------")
    for i, recipe in enumerate(matched_recipes, 1):
        print(f"{i}. {recipe['recipe_name']}")
        print("< 재료 > ", ', '.join(recipe['ingredients']))
        for step in recipe['directions']:
            print(step)
        print()
else:
    print("냉장고 재료로 만들 수 있는 레시피를 찾을 수 없습니다.")

    # 유사한 레시피 탐색
    similar_recipes = []
    for recipe in recipes:
        ingredients_set = set(recipe['ingredients'])
        similarity = len(set(user_ingredients) & ingredients_set) / len(set(user_ingredients) | ingredients_set)
        similar_recipes.append((recipe, similarity))

    # 유사도 리스트 정렬
    similar_recipes.sort(key=lambda x: x[1], reverse=True)

    # 상위 3가지 레시피 출력
    print("\n유사한 레시피를 고려해보세요:")
    for i, (recipe, similarity) in enumerate(similar_recipes[:3], 1):
        print(f"{i}. {recipe['recipe_name']} (유사도: {similarity:.2%})")
        print("< 재료 > ", ', '.join(recipe['ingredients']))
        print()

    # 사용자에게 다른 방안 제시
    print("\n다른 방안을 고려해보세요:")
    print("1. 다른 재료로 검색해보세요.")
    print("2. 심플한 요리를 시도해보세요. (예: 계란후라이, 김치볶음밥 등)")
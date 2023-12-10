from recipe_manager import load_recipes
from recipe_finder import find_matched_recipes, find_similar_recipes

# 레시피 데이터 파일명
recipe_file = "recipe.txt"

# 레시피 데이터를 불러옴
recipes = load_recipes(recipe_file)

# 사용자 입력 받기
user_input = input("냉장고에 있는 재료 목록을 입력하세요 (띄어쓰기로 구분): ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(' ')]

# 사용자 입력과 일치하는 레시피 찾기
matched_recipes = find_matched_recipes(recipes, user_ingredients)

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
    similar_recipes = find_similar_recipes(recipes, user_ingredients)

    # 유사도 리스트 정렬 및 상위 3가지 레시피 출력
    print("\n유사한 레시피를 고려해보세요!\n")
    for i, (recipe, similarity) in enumerate(similar_recipes, 1):
        print(f"{i}. {recipe['recipe_name']} (유사도: {similarity:.2%})")
        print("< 재료 > ", ', '.join(recipe['ingredients']))
        print()

    # 사용자에게 다른 방안 제시
    print("다른 방안을 고려해보세요:")
    print("1. 다른 재료로 검색해보세요.")
    print("2. 심플한 요리를 시도해보세요. (예: 계란후라이, 김치볶음밥 등)")
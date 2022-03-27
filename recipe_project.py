import requests


def recipe_search(ingredient):
    app_id = 'c1657e03'
    app_key = '110b79f689115bee5a220d6f5d5753e5'

    response = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = response.json()

    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    veggie = input('are you vegetarian? ')
    for result in results:
        recipe = result['recipe']
        if veggie == 'yes' and "Vegetarian" in recipe["healthLabels"]:
            print(recipe['label'])
            print(recipe['dietLabels'])
            print(recipe['url'])
            print()
        else:
            print('not suitable')

run()

with open('recipe.txt', 'w+') as text_file:
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        recipes = recipe['url']
        text_file.write(recipes)
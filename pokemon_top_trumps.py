import random

import requests

def random_pokemon():
    pokemon_number = random.randint(1,151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return{
      'name':pokemon['name'],
      'id':pokemon['id'],
      'height':pokemon['height'],
      'weight':pokemon['weight'],
    }

def run():
    my_pokemon = random_pokemon()
    print('My pokemon is {}'.format(my_pokemon['name']))

    other_pokemon = random_pokemon()
    print('Opponents selected pokemon is {}'.format(other_pokemon['name']))

    stats = ['id', 'height', 'weight']
    chosen_stat = random.choice(stats)

    my_stat = my_pokemon[chosen_stat]
    opponent_stat = other_pokemon[chosen_stat]

    my_win = ('My {} was better, I win'.format(chosen_stat))
    they_win = ('My opponents {} was better, I lose'.format(chosen_stat))
    draw = ('The stats were the same, its a draw')

    if my_stat > opponent_stat:
        print(my_win)
    elif opponent_stat > my_stat:
        print(they_win)
    else:
        print(draw)
run()

def winner():


    if 'my_win' and 'my_win' and 'my_win' and 'my_win':
        print('I am the overall winner')
    elif 'my_win' and 'my_win' and 'my_win' and 'they_win':
        print('I am the overall winner')
    elif 'they_win' and 'they_win' and 'they_win' and 'they_win':
        print('Opponent is the overall winner')
    elif 'they_win' and 'they_win' and 'they_win' and 'my_win':
        print('Opponent is the overall winner')
    elif 'my_win' and 'my_win' and 'draw' and 'they_win':
        print('I am the overall winner')
    elif 'my_win' and 'my_win' and 'draw' and 'draw':
        print('I am the overall winner')
    elif 'they_win' and 'they_win' and 'draw' and 'draw':
        print('Opponent is the overall winner')
    elif 'they_win' and 'they_win' and 'draw' and 'my_win':
        print('Opponent is the overall winner')
    else:
        print('Overall, its a draw')
winner()

for game in range(3):
    run()

winner()


















import requests


def get_token_from_file(file_name='token.txt') -> str:
    """Возвращает авторизационный токен сохраненный в отдельном файле 'file_name'."""
    with open(file_name, 'rt', encoding='utf-8') as file:
        return file.read().strip()


def create_dict_of_heroes(list_of_heroes: list, stat: str) -> dict:
    """Возвращает словарь, где ключи - имена героев из списка 'list_of_heroes', а значения - выбранная характеристика 'stat'."""
    dict_of_heroes = {}
    for hero in list_of_heroes:
        dict_of_heroes[hero] = float(requests.get(f'https://superheroapi.com/api/{token}/search/{hero}').json()['results'][0]['powerstats'][stat])
    return dict_of_heroes


def designate_the_smartest_hero(list_of_heroes: list, stat='intelligence'):
    """Определяет элемент словаря, полученный от функции 'create_dict_of_heroes()', обладающий самым высоким значением'."""
    highest_intelligence = 0
    dict_of_heroes = create_dict_of_heroes(list_of_heroes, stat)
    for hero in dict_of_heroes:
        if dict_of_heroes[hero] > highest_intelligence:
            highest_intelligence = dict_of_heroes[hero]
            the_smartest_hero = hero
    print(f'{the_smartest_hero} - герой c самым высоким показателем {stat.title()}.')


if __name__ == "__main__":
    token = get_token_from_file()
    list_of_heroes = ['Hulk', 'Captain America', 'Thanos']

    designate_the_smartest_hero(list_of_heroes)
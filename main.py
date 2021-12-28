import requests


class Hero:
    list_of_all = []

    def __init__(self, name: str, token):
        self.name = name.title()
        self.intelligence = float(requests.get(f'https://superheroapi.com/api/{token}/search/{self.name}').json()['results'][0]['powerstats']['intelligence'])
        self.list_of_all.append(self)


def designate_the_smartest_hero(list_of_heroes=Hero.list_of_all):
    """Определяет объект, обладающий самым высоким значением атрибута 'intelligence' среди элементов списка 'list_of_heroes'.
    Элементами списка должны быть экземпляры класса 'Hero'.
    """
    highest_intelligence = 0
    for hero in list_of_heroes:
        if hero.intelligence > highest_intelligence:
            highest_intelligence = hero.intelligence
            the_smartest_hero = hero.name
    print(f'{the_smartest_hero} - умнейший герой')


if __name__ == "__main__":
    token = ''

    hulk = Hero('hulk', token)
    captain_america = Hero('Captain America', token)
    thanos = Hero('Thanos', token)

    designate_the_smartest_hero()
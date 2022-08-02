import requests
from bs4 import BeautifulSoup


def get_next_page(page):
    soup = BeautifulSoup(page, 'lxml')
    links = soup.find('div', id='mw-pages').find_all('a')

    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text
            return page

    page = None
    return page


def get_animals_for_each_letter_of_alphabet():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    letters_to_animals_count = {}

    while page is not None:
        soup = BeautifulSoup(page, 'lxml')
        parent_1 = soup.find('div', id='mw-pages')
        parent_2 = parent_1.find('div', class_='mw-category-group')
        animals_names_of_page = parent_2.find_all('a')

        for animal_name in animals_names_of_page:
            first_letter_of_animal_name = animal_name.text[0]
            if first_letter_of_animal_name not in letters_to_animals_count:
                letters_to_animals_count[first_letter_of_animal_name] = 1
            else:
                letters_to_animals_count[first_letter_of_animal_name] += 1
        page = get_next_page(page)

    return letters_to_animals_count


def do_program():
    letters_to_animals_count = get_animals_for_each_letter_of_alphabet()
    for key, value in letters_to_animals_count.items():
        print(f'{key}: {value}')


do_program()

# Написать программу, где создадим класс Soup (для определения типа супа),
# принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать
# «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup:
    def __init__(self, soup, ingridient):
        self.soup = soup
        self.ingridient = ingridient
        self.hot_water = 'просто кипяток!'
    def show_my_soup(self):
        if self.ingridient == 'свекла':
            self.hot_water = self.ingridient
            return f'В супе "{self.soup}" гавный ингридиент - "{self.ingridient}"'
        else:
            return f'Это не {self.soup} - это просто {self.hot_water}'

soup = Soup('Борщ', 'свекла')
print(soup.show_my_soup())


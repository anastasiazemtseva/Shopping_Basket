import codecs
class Product:
    def __init__(self, name, price,
                 brand, year, kod):
        '''Метод инициализации '''
        self.name = name
        self.price = price
        self.__brand = brand
        self.__year = year
        self.kod = kod

    brand = property()
    year = property()

    @brand.setter
    def set_brand(self, brand):
        self.__brand = brand

    @brand.getter
    def get_brand(self):
        return self.__brand

    @year.setter
    def set_year(self, year):
        self.__year = year

    @year.getter
    def get_year(self):
        return self.__year

    def info_p(self):
        print('Название: ', self.name,'\nЦена:', self.price,
              '\nБренд', self.brand, '\nГод', self.year, '\nШтрих-код', self.kod)

    def new_price(self, n_price):
        self.price = n_price

    def __str__(self):
        '''Метод строкового представления объекта '''
        name = '|' + str(self.name) + ' '
        price = str(self.price) + ' '
        brand = str(self.__brand) + ' '
        year = str(self.__year) + ' '
        kod = str(self.kod) + ' '

        name += ((16 - len(name)) * ' ' + '|')
        price += ((10 - len(price)) * ' ' + '|')
        brand += ((20 - len(brand)) * ' ' + '|')
        year += ((14 - len(year)) * ' ' + '|')
        kod += ((14 - len(kod)) * ' ' + '|')
        table = ('%2s %3s %4s %5s %6s' % (name, price, brand, year, kod))

        return table

    def __repr__(self):
        '''Метод представления объекта '''
        return self.__str__()

class Shopping_Basket:
    '''Класс корзины магазина'''
    def __init__(self):
        self.lst_of_products = []

    def add_prod(self, prod):
        self.lst_of_products.append(prod)

    def del_prod(self, prod):
        self.lst_of_products.pop(prod)


    def info(self):
        for i in self.lst_of_products:
            i.info_p()


def main():
    all = Shopping_Basket()
    print('Что вы хотите сделать? ')
    print('1. Добавить новый товар')
    print('2. Изменить цену товара')
    print('3. Удалить товар')
    print('4. Выйти')
    print()
    answer = input('Введите ответ: ')

    while answer != '4':

        if answer == '1':
            name = input('Название: ')
            price = input('Цена: ')
            brand = input('Бренд: ')
            year = input('Год производства: ')
            kod = input('Штрих-код: ')

            product = Product(str(name), str(price), str(brand), str(year), str(kod))
            all.add_prod(product)
            answer = input('Что вы хотите сделать? ')

        elif answer == '2':
            name_of_prod = input('Название товара? ')
            for i in range(len(all.lst_of_products)):
                if all.lst_of_products[i].name == name_of_prod:
                    new_price = input('Новая цена? ')
                    product.new_price(new_price)
                    answer = input('Что вы хотите сделать? ')

        elif answer == '3':
            name_of_prod = input('Название товара? ')
            for i in range(len(all.lst_of_books)):
                if all.lst_of_products[i].name == name_of_prod:
                    all.del_book(i)
                    answer = input('Что вы хотите сделать? ')



    with codecs.open('out.txt', 'w', encoding='utf-8') as f:

        name = '|Название:'
        price = 'Цена:'
        brand = 'Бренд:'
        year = 'Год производства:'
        kod = 'Штрих-код:'

        name += ((16 - len(name)) * ' ' + '|')
        price += ((10 - len(price)) * ' ' + '|')
        brand += ((20 - len(brand)) * ' ' + '|')
        year += ((14 - len(year)) * ' ' + '|')
        kod += ((14 - len(kod)) * ' ' + '|')



        table = ('%2s %3s %4s %5s %6s' % (name, price, brand, year, kod))
        f.write('-' * len(table) + '\n')
        f.write(table)
        f.write('\n')

        for item in all.lst_of_products:
            f.write(str(item) + '\n')

if __name__ == '__main__':
    main()
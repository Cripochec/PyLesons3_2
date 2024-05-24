class Furniture:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def display_info(self):
        print("Марка:", self.brand)
        print("Название:", self.name)
        print("Цена:", self.price)


class Table(Furniture):
    def __init__(self, brand, name, price, has_backrest, num_legs):
        super().__init__(brand, name, price)
        self.has_backrest = has_backrest
        self.num_legs = num_legs

    def display_info(self):
        super().display_info()
        print("Спинка:", "есть" if self.has_backrest else "нет")
        print("Количество ножек:", self.num_legs)

if __name__ == '__main__':
    # Пример использования классов

    brand = input("Введите наименование бренда: ")
    name = input("Введите наименование продукта: ")
    price = input("Введите цену продукта: ")

    furniture_item = Furniture(brand, name, price)
    furniture_item.display_info()

    print("\n")

    brand = input("Введите наименование бренда: ")
    name = input("Введите тип стула: ")
    price = input("Введите цену стула: ")
    has_backrest = input("Есть ли спинка (True/False): ")
    num_legs = input("Введите количество ножек: ")
    table_item = Table(brand, name, price, has_backrest, num_legs)
    table_item.display_info()
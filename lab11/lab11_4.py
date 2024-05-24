class Human:
    default_name = "Джон Коффи"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Имя: {self.name};")
        print(f"Возраст: {self.age} лет;")
        print(f"Дом: {self.__house};")
        print(f"Деньги: {self.__money} рублей;")

    @staticmethod
    def default_info():
        print(f"Имя по умолчанию: {Human.default_name};")
        print(f"Возраст по умолчанию: {Human.default_age} лет;")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f"{self.name} заработал {amount} рублей.")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f"{self.name} купил дом за {price} рублей.")
        else:
            print(f"{self.name}, у вас недостаточно денег для покупки этого дома.")


# Пример класса "Дом" (для демонстрации)
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

    def __str__(self):
        return f"Дом площадью {self._area} кв.м стоимостью {self._price} рублей"


# Пример
human1 = Human("Генадий", 45)
human2 = Human()

human1.info()
human2.info()

Human.default_info()


human1.earn_money(500000)

house = House(220, 90000)
human1.buy_house(house, 5)
human1.info()

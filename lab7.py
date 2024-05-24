class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def make_sound(self):
        pass

    def display_info(self):
        print(f"Животное: {self.name}\nу него {self.legs} ноги")

    def __str__(self):
        return f"Ваше животное: {self.name}"


class Dog(Animal):
    def __init__(self, name, legs, breed):
        super().__init__(name, legs)
        self.breed = breed

    def make_sound(self):
        print("Гав!")

    def __str__(self):
        return f"Собака по кличке: {self.name}, Породы: {self.breed}, имеет {self.legs} ноги"

    def display_info(self):
        super().display_info()
        print(f"Собака породы: {self.breed}")


class Cat(Animal):
    def make_sound(self):
        print("Мяу!")


class Parrot(Animal):
    def __init__(self, name, legs, color):
        super().__init__(name, legs)
        self.color = color

    def __str__(self):
        return f"Папугай по кличке: {self.name}, он {self.color}цвета, у него {self.legs} ног"

    def display_info(self):
        super().display_info()
        print(f"Попугай {self.color} цвета")

if __name__ == '__main__':
    # Пример использования классов
    while True:
        v = input("Какой объект вы хотите создать (1-животное, 2-собака, 3-кот, 4-папугай, 5-закрыть программу): ")
        if v == "1":
            name = input("Введите кличку животного: ")
            legs = input("Введите количество ног у животного: ")
            animal = Animal(name, legs)
            print("\n")
            animal.display_info()
        elif v == "2":
            name = input("Введите кличку собаки: ")
            legs = input("Введите количество ног у собаки: ")
            breed = input("Введите породу собаки: ")
            dog = Dog(name, legs, breed)
            print("\n")
            dog.make_sound()
            print("\n")
            dog.display_info()
        elif v == "3":
            name = input("Введите кличку кота/кошки: ")
            legs = input("Введите количество ног у кота/кошки: ")
            cat = Cat(name, legs)
            print("\n")
            cat.make_sound()
            print("\n")
            cat.display_info()
        elif v == "4":
            name = input("Введите кличку попугая: ")
            legs = input("Введите количество ног у попугая: ")
            color = input("Введите цвет попугая: ")
            parrot = Parrot(name, legs, color)
            print("\n")
            parrot.display_info()
        elif v == "5":
            break
        else:
            print("Некоректные данные, попробуйте заново")

from abc import ABC, abstractmethod


class Starship(ABC):
    @abstractmethod
    def warp_speed(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass

    @abstractmethod
    def self_destruct(self):
        pass


class FederationStarship(Starship):
    def warp_speed(self):
        print("Звездолет Федерации включил варп-привод.")

    def fire_weapon(self):
        print("Звездолет Федерации выпустил фазеры.")

    def self_destruct(self):
        print("Звездолет Федерации инициировал самоуничтожение.")


class KlingonWarship(Starship):
    def warp_speed(self):
        print("Клингонский корабль включил варп-привод.")

    def fire_weapon(self):
        print("Клингонский корабль выпустил фотонные торпеды.")

    def self_destruct(self):
        print("Клингонский корабль инициировал самоуничтожение.")


class Ingredient(ABC):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def get_quantity(self):
        return self.quantity


class Vegetable(Ingredient):
    def get_name(self):
        return f"Овощ: {self.name}"

    def get_quantity(self):
        return f"Количество овощей {self.name}: {self.quantity}"


class Fruit(Ingredient):
    def get_name(self):
        return f"Фрукт: {self.name}"

    def get_quantity(self):
        return f"Количество фруктов {self.name}: {self.quantity}"


# Пример использования:
if __name__ == "__main__":
    print("1)\n")
    federation_ship = FederationStarship()
    klingon_ship = KlingonWarship()

    federation_ship.warp_speed()
    federation_ship.fire_weapon()
    federation_ship.self_destruct()
    print("\n")
    klingon_ship.warp_speed()
    klingon_ship.fire_weapon()
    klingon_ship.self_destruct()

    print("\n2)\n")
    tomato = Vegetable(input("Введите овощь: "), int(input("Введите количество: ")))
    apple = Fruit(input("Введите фрукт: "), int(input("Введите количество: ")))
    print("\n")
    print(tomato.get_name())
    print(tomato.get_quantity())
    print("\n")
    print(apple.get_name())
    print(apple.get_quantity())

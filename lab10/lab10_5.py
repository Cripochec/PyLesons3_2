class Ship:
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
        self.hits = [False] * size

    def is_sunk(self):
        return all(self.hits)

    def is_hit(self, x, y):
        if (x, y) in self.coordinates:
            index = self.coordinates.index((x, y))
            self.hits[index] = True
            return True
        return False

    def collides_with(self, other_ship):
        for coord in self.coordinates:
            for other_coord in other_ship.coordinates:
                if abs(coord[0] - other_coord[0]) <= 1 and abs(coord[1] - other_coord[1]) <= 1:
                    return True
        return False


class SingleDeckShip(Ship):
    def __init__(self, coordinates):
        super().__init__(1, [coordinates])


class DoubleDeckShip(Ship):
    def __init__(self, coordinates):
        # [(x1, y1), (x2, y2)]
        super().__init__(2, coordinates)


class TripleDeckShip(Ship):
    def __init__(self, coordinates):
        # [(x1, y1), (x2, y2), (x3, y3)]
        super().__init__(3, coordinates)


class QuadrupleDeckShip(Ship):
    def __init__(self, coordinates):
        # [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        super().__init__(4, coordinates)


class Battlefield:
    def __init__(self, size=10):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def add_ship(self, ship):
        for (x, y) in ship.coordinates:
            if x < 0 or x >= self.size or y < 0 or y >= self.size:
                raise ValueError("Координаты корабля выходят за пределы поля.")

        for other_ship in self.ships:
            if ship.collides_with(other_ship):
                raise ValueError("Корабли не должны соприкасаться.")

        self.ships.append(ship)
        for (x, y) in ship.coordinates:
            self.grid[x][y] = '#'

    def display(self):
        for row in self.grid:
            print(' '.join(row))


class Game:
    def __init__(self):
        self.battlefield = Battlefield()

    def add_ship(self, ship):
        self.battlefield.add_ship(ship)

    def display_battlefield(self):
        self.battlefield.display()


# Демонстрация работы программы
if __name__ == "__main__":
    game = Game()
    SingleDeckShipCount = 4
    DoubleDeckShipCount = 3
    TripleDeckShipCount = 2
    QuadrupleDeckShipCount = 1
    print("Для установки напишите цифру обозначающую количество палуб\nX-вертикаль, Y-горизонталь\n")

    while True:
        if SingleDeckShipCount == 0 and DoubleDeckShipCount == 0 and TripleDeckShipCount == 0 and QuadrupleDeckShipCount == 0:
            print("\n\nВы заполнили поле")
            game.display_battlefield()
            break

        game.display_battlefield()
        type_ship = int(input(f"Одиночный - {SingleDeckShipCount}\n"
                              f"Двойной - {DoubleDeckShipCount}\n"
                              f"Тройной - {TripleDeckShipCount}\n"
                              f"Четверной - {QuadrupleDeckShipCount}\n"
                              f"Какой корабль вы хотите установить (1, 2, 3, 4): "))

        if type_ship == 1:
            if SingleDeckShipCount != 0:
                x = int(input("укажите X:"))
                y = int(input("укажите Y:"))
                game.add_ship(SingleDeckShip((x - 1, y - 1)))
                SingleDeckShipCount -= 1
            else:
                print("Уже установлен максимум кораблей этого типа")

        if type_ship == 2:
            if DoubleDeckShipCount != 0:
                x = int(input("укажите X (Начальную):"))
                y = int(input("укажите Y (Начальную):"))
                X = int(input("укажите X (Конечную):"))
                Y = int(input("укажите Y (Конечную):"))
                game.add_ship(DoubleDeckShip([(x - 1, y - 1), (X - 1, Y - 1)]))
                DoubleDeckShipCount -= 1
            else:
                print("Уже установлен максимум кораблей этого типа")

        if type_ship == 3:
            if TripleDeckShipCount != 0:
                x = int(input("укажите X (Начальную):"))
                y = int(input("укажите Y (Начальную):"))
                X = int(input("укажите X (Конечную):"))
                Y = int(input("укажите Y (Конечную):"))
                if x == X:
                    game.add_ship(TripleDeckShip([(x - 1, y - 1), (x - 1, y), (x - 1, Y - 1)]))
                if y == Y:
                    game.add_ship(TripleDeckShip([(x - 1, y - 1), (x, y - 1), (X - 1, y - 1)]))
                TripleDeckShipCount -= 1
            else:
                print("Уже установлен максимум кораблей этого типа")

        if type_ship == 4:
            if QuadrupleDeckShipCount != 0:
                x = int(input("укажите X (Начальную):"))
                y = int(input("укажите Y (Начальную):"))
                X = int(input("укажите X (Конечную):"))
                Y = int(input("укажите Y (Конечную):"))
                if x == X:
                    game.add_ship(QuadrupleDeckShip([(x-1, y-1), (x-1, y), (x-1, Y-2), (x-1, Y-1)]))
                if y == Y:
                    game.add_ship(QuadrupleDeckShip([(x-1, y-1), (x, y-1), (X-2, y-1), (X-1, y-1)]))
                QuadrupleDeckShipCount -= 1
            else:
                print("Уже установлен максимум кораблей этого типа")

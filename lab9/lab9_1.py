import math


class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def area(self):
        return 2 * (self.width * self.height + self.length * self.height)


class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Wallpaper:
    def __init__(self, roll_width, roll_length):
        self.roll_width = roll_width
        self.roll_length = roll_length

    def roll_area(self):
        return self.roll_width * self.roll_length

    def rolls_needed(self, room_area):
        return room_area / self.roll_area()


if __name__ == "__main__":
    room = Room(float(input("Введите ширину комнаты в метрах: ")), float(input("Введите длину комнаты в метрах: ")),
                float(input("Введите высоту комнаты в метрах: ")))

    extra_area = 0

    number_objects = int(input("\nСколько дверей будет в комнате: "))
    for i in range(number_objects):
        door = Door(float(input(f"\nВведите ширину {i+1} двери в метрах: ")),
                    float(input(f"Введите высоту {i+1} двери в метрах: ")))
        extra_area += door.area()

    number_objects = int(input("\nСколько окон будет в комнате: "))
    for i in range(number_objects):
        window = Window(float(input(f"\nВведите ширину {i+1} окна в метрах: ")),
                        float(input(f"Введите высоту {i+1} окна в метрах: ")))
        extra_area += window.area()

    wallpaper = Wallpaper(float(input("\nВведите ширину рулона обоев в метрах: ")),
                          float(input("Введите длину рулона обоев в метрах: ")))

    total_area = room.area() - extra_area
    rolls_needed = wallpaper.rolls_needed(total_area)
    rolls_needed_rounded = math.ceil(rolls_needed)
    rolls_leftover = rolls_needed_rounded - rolls_needed

    print(f"\nОбщая площадь стен: {total_area} кв. м")
    print(f"Необходимо рулонов обоев: {rolls_needed_rounded:}")
    print(f"Остаток рулонов обоев: {rolls_leftover:.2f}")

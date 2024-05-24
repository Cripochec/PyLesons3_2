class Ammunition:
    def __init__(self, name, ammunition_type, quantity):
        self.name = name
        self.ammunition_type = ammunition_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (тип: {self.ammunition_type}, количество: {self.quantity})"


class CombatMission:
    def __init__(self, target, start_time, duration):
        self.target = target
        self.start_time = start_time
        self.duration = duration

    def __str__(self):
        return f"Цель: {self.target}, Начало: {self.start_time}, Длительность: {self.duration} часов"


class Warrior:
    def __init__(self, name, warrior_type):
        self.name = name
        self.warrior_type = warrior_type
        self.ammunition = []
        self.combat_missions = []

    def add_ammunition(self, ammunition):
        self.ammunition.append(ammunition)

    def add_combat_mission(self, mission):
        self.combat_missions.append(mission)

    def display_ammunition(self):
        print(f"Амуниция воина {self.name}:")
        for ammo in self.ammunition:
            print(f"    {ammo}")

    def display_combat_missions(self):
        print(f"Боевые задачи воина {self.name}:")
        for mission in self.combat_missions:
            print(f"    {mission}")


class Army:
    def __init__(self):
        self.warriors = []

    def add_warrior(self, warrior):
        self.warriors.append(warrior)

    def display_warriors(self):
        print("Армия:")
        for warrior in self.warriors:
            print(f"{warrior.name} (тип: {warrior.warrior_type})")


def create_ammunition():
    name = input("\nВведите название: ")
    ammunition_type = input("Введите тип: ")
    quantity = int(input("Введите количество: "))
    return Ammunition(name, ammunition_type, quantity)


def create_combat_mission():
    target = input("\nВведите цель боевой задачи: ")
    start_time = input("Введите время приступания к заданию: ")
    duration = float(input("Введите время на выполнение задания (в часах): "))
    return CombatMission(target, start_time, duration)


def create_warrior():
    name = input("\nВведите имя воина: ")
    warrior_type = input("Введите тип воина: ")
    return Warrior(name, warrior_type)


if __name__ == "__main__":
    army = Army()

    while True:
        print("Добавление воинов в армию:\n")
        warrior = create_warrior()
        army.add_warrior(warrior)

        print(f"\nДобавление амуниции для({warrior.name}):")
        while True:
            ammunition = create_ammunition()
            warrior.add_ammunition(ammunition)
            more_ammo = input("Хотите добавить что-то ещё? (y/n): ")
            if more_ammo.lower() != 'y':
                break

        print(f"\nДобавление боевых задач для({warrior.name}):")
        while True:
            mission = create_combat_mission()
            warrior.add_combat_mission(mission)
            more_missions = input("Хотите добавить еще одну боевую задачу? (y/n): ")
            if more_missions.lower() != 'y':
                break

        more_warriors = input("\nХотите добавить еще одного воина? (y/n): ")
        if more_warriors.lower() != 'y':
            break

    army.display_warriors()
    for warrior in army.warriors:
        warrior.display_ammunition()
        warrior.display_combat_missions()

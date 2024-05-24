def convert_to_minutes(time_str):
    # Преобразует время в формате 'HH:MM' в количество минут с начала дня
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


def check_schedule(schedule):
    # Преобразуем время прибытия в минуты с начала дня
    times_in_minutes = [convert_to_minutes(time) for time in schedule]

    # Сортируем время прибытия
    times_in_minutes.sort()

    # Проверяем разницу между каждым последовательным рейсом
    for i in range(1, len(times_in_minutes)):
        if times_in_minutes[i] - times_in_minutes[i - 1] > 20:
            return "NO"

    return "YES"


# Примеры использования
schedule = []
num_flights = int(input("Введите количество рейсов: "))

for i in range(num_flights):
    flights = input("Введите Время в формате (ЧЧ:ММ): ")
    schedule.append(flights)

print(check_schedule(schedule))

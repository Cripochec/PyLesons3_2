import math


def average(arr):
    amount = 0
    for i in arr:
        amount+=i
    return amount/len(arr)


def quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        # Вывод результатов
        print("Корни:")
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        print("Нет действительных корней.")


def separation_into_parts(n):
    hundreds = n // 100
    tens = (n % 100) // 10
    units = n % 10
    print("Сотни:", hundreds)
    print("Десятки:", tens)
    print("Единицы:", units)


def is_triangle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            return "Треугольник существует и является прямоугольным"
        else:
            return "Треугольник существует, но не является прямоугольным"
    else:
        return "Треугольник не существует"


def water_condition(t):
    if t <= 0:
        print("Вода находится в твердом состоянии (лед)")
    elif t > 0 and t < 100:
        print("Вода находится в жидком состоянии")
    else:
        print("Вода находится в газообразном состоянии")


def parity(n):
    if n % 2 == 0:
        print("Введенное число является четным")
    else:
        print("Введенное число не является четным")


if __name__ == '__main__':

#1
    print("1)\nВводите два числа для нахождения среднего арифметического:")
    arr = [float(input("x:")), float(input("y:"))]
    print(f"среднее арифитическое = {average(arr)}")
#2
    print("2)\n     x^3\ny= -------- , введите x\n    2(x+5)")
    x = float(input())
    print(f"y={(x**3)/(2*(x+5))}")
#3
    print("3)\nРешение квадратного уровнения.")
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    quadratic_equation(a, b, c)
#4
    n = int(input("4)\nВведите трехзначное число: "))
    separation_into_parts(n)
#5
    angle1 = int(input("5)\nВведите значение первого угла треугольника: "))
    angle2 = int(input("Введите значение второго угла треугольника: "))
    print(is_triangle(angle1, angle2))
#6
    temperature = float(input("6)\nВведите температуру: "))
    water_condition(temperature)
#7
    number = int(input("7)\nВведите число: "))
    parity(number)
#8
    print(f"8)\na = {5+3**2-18*4+120/5}\nb = {25.5+4.2**2-125/5}")
#9
    num1 = float(input("9)\nВведите первое число: "))
    num2 = float(input("Введите второе число: "))

    power = num1 ** num2
    result = power / num1
    remainder = power % result

    print(f"Результат возведения первого числа в степень второго числа: {power}")
    print(f"Результат деления возведения в степень на первое число: {result}")
    print(f"Остаток от деления: {remainder}")
#10
    num1 = float(input("10)\nВведите первое число: "))
    num2 = float(input("Введите второе число: "))

    print(f"Результат обычного деления: {num1 / num2}")
    print(f"Результат целочисленного деления: {num1 // num2}")
#11
    num1 = float(input("11)\nВведите дробное число: "))
    num2 = int(input("Введите целое число: "))

    print(f"Остаток от деления дробного числа на целое: {num1 % num2}")
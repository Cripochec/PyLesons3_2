from random import randint


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def complexity(n):
    if n == 1:
        return 10
    elif n == 2:
        return 100
    elif n == 3:
        return 1000
    elif n == 4:
        return 10000


if __name__ == '__main__':
    # 1
    n = int(input("1)\nВведите целое число:"))
    if n > 0:
        print("1")
    elif n < 0:
        print("-1")
    else:
        print("0")
    # 2
    print("2)\nВводите два вещественных числа для нахождения большего из них:")
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print(f"число {num1} = {num2}")
    # 3
    print("3)\nВведите четыри целых числа:")
    num1 = int(input("Первое число:"))
    num2 = int(input("Второе число:"))
    num3 = int(input("Третье число:"))
    num4 = int(input("Четвёртое число:"))
    arr = [num1, num2, num3, num4]
    maximum = 0
    for i in arr:
        if i > maximum:
            maximum = i
    print(f"Наибольшее число {maximum}")
    # 4
    n = 0
    for i in range(101):
        n += i
    print(f"4)\nCумма чисел от 0 до 100 = {n}")
    # 5
    n = int(input("5)\nВведите число для нахождения его факториала: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"факториал числа ({n}) = {factorial}")
    # 6
    n = int(input("6)\nВведите количество чисел ряда Фибоначи: "))
    num1 = 1
    num2 = 2
    arr = [1, 2]
    for i in range(n - 2):
        arr.append(num1 + num2)
        buf = num1
        num1 = num2
        num2 += buf
    print(f"Ряд Фибоначи из {n} элементов: {arr}")
    # 7
    n = int(input(
        "7)\nВыберите сложность игры, для выхода \"stop\":\n1) числа от 1 до 10\n2) числа от 1 до 100\n3) числа от 1 "
        "до 1000\n4) числа от 1 до 10000\n"))

    num = randint(0, complexity(n))
    while True:
        n = input("попробуйте угадать число: ")
        if n == "stop":
            break
        n = int(n)
        if n > num:
            print("Меньше")
        elif n < num:
            print("Больше")
        else:
            print("Вы угадали!")
            break

    # 8
    number1 = int(input("8)\nВведите первое число: "))
    number2 = int(input("Введите второе число: "))
    print(f"Наибольший общий делитель: {find_gcd(number1, number2)}")

    # 9
    n = int(input(
        "9)\nВыберите сложность игры:"
        "\n1) числа от 1 до 10\n2) числа от 1 до 100\n3) числа от 1 до 1000\n4) числа от 1 до 10000"
        "\nНа то чтобы угадать число у вас есть 10 попыток!\n"))

    num = randint(0, complexity(n))
    for i in range(1, 12):
        if i == 9:
            print("Будьте внимательны!")
        if i == 10:
            print("Последний шанс!")
        if i == 11:
            print(f"GAME OVER!\nЗагаданное число: {num}")
            break
        n = int(input(f"Попытка № {i}, попробуйте угадать число: "))
        if n > num:
            print("Меньше")
        elif n < num:
            print("Больше")
        else:
            print("Вы угадали!")
            break

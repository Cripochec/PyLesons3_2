def quantity_numbers(n):
    if "-" in n:
        n = n[1: len(n)]

    if "." in n:
        n = n[1: len(n)]

    if "," in n:
        n = n[1: len(n)]

    return len(n)


def factorial_numbers(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


if __name__ == '__main__':

#1
    n = input("1)\nВведите число, у данного числа будут подсчитаны все цифры и выведены в консоль: ")
    print(f"В числе ({n}), {quantity_numbers(n)} чисел.")
#2
    n = int(input("2)\nВведите число, для данного числа будут найден его факториал и выведены в консоль: "))
    print(f"Факториал числа {n} = {factorial_numbers(n)}.")

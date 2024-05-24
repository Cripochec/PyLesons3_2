from random import randint


if __name__ == '__main__':
    # Строки
    # 1
    line = input("Строки:\n1)\nВвведите строку, первый и последний знак в ней будет заменён на \"!\": ")
    if len(line) == 1:
        print("!")
    else:
        new_line = "!" + line[1:-1] + "!"
        print(new_line)
    # 2
    line = input("2)\nВвведите строку, будет определена длина строки и первый и последний символ: ")
    print(f"длина: {len(line)}; первый символ: {line[0]}; последний символ: {line[-1]}")
    # 3
    k = int(input("3)\nВы введёте длину строки (k), после введёте строку, если длина строки будет больше чем (k),"
                  " то остаточная длина выведится в новой строке.\nk = "))
    line = input("Строка: ")

    while True:
        if len(line) <= k:
            print(line)
            break
        else:
            print(line[0:k])
            line = line[k:len(line)]
    # 4
    line = input("4)\nВвведите два слова через \" \", будет определено второе слово и выведено в консоль: ")
    line1, line2 = line.split(" ")
    print(line2)
    # 5
    line = input("5)\nВвведите строку с разделеителями слов \" \", "
                 "будет определено наидлинейшее слово и выведено в консоль: ")
    arr = line.split(" ")
    maximum = ""
    for i in arr:
        if len(i) > len(maximum):
            maximum = i
    print(maximum)
    # 6
    line = input("6)\nВвведите строку на английском в разном регистре, "
                 "будет подсчитано количество символов в верхнем и нижнем регистре: ")
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countUP = 0
    countDWN = 0
    for i in abc:
        countUP += line.count(i)

    abc = abc.lower()

    for i in abc:
        countDWN += line.count(i)
    print(f"Букв в верхнем регистре: {countUP}; Букв в нижнем регистре: {countDWN}")
    # Списки
    # 1
    arr = [1, 2, 3, 4, 5]
    print(f"Списки\n1)\nИзначальный список: {arr}")
    print(f"Обращения к элементу по его индексу (arr[1]): {arr[1]}")
    arr[1] = 6
    print(f"Замена элемента : {arr}")
    arr.append(7)
    arr2 = arr.copy()
    print(f"Добавления элемента: {arr}")
    arr.pop(2)
    print(f"Удаления элемента: {arr}")
    print(f"Дублирование списка: {arr2}")
    # 2
    arr = [5, 6, 3, 2]
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    print(f"2)\nИндекс минимального элемента, список: {arr}")
    print(f"индекс: {arr.index(minimum)}")
    # 3
    arr = [5, -2, 6, 3, -4, 2, 0]
    arr_negative = []
    arr_positive = []
    for i in arr:
        if i > 0:
            arr_positive.append(i)
        else:
            arr_negative.append(i)
    print(f"3)\nРазделение положительных и отрицательных чисел в разные списки,список: {arr}")
    print(f"Список положительных элементов: {arr_positive}\nСписок остальных элементов: {arr_negative} ")
    # 4
    arr = [5, -2, 6, 3, -4, 2, 0]
    summ = 0
    for i in range(1, len(arr), 2):
        summ += arr[i]
    print(f"4)\nСумма элементов с нечётными индексами, список: {arr}\nСумма элементов = {summ}")
    # 5
    arr = [5, 12, 20, 3, 47, 15, 9, 0]
    print(f"5)\nЭлементы имеющие значение меньше 15 будут заменены на их удвоенную версию, изначальный список: {arr}")
    index = 0
    for i in arr:
        if i < 15:
            arr[index] = i*2
        index += 1
    print(f"\nФинальныйы список: {arr}")
    # 6
    arr = []
    arr1 = []
    arr2 = []
    for i in range(31):
        arr1.append(randint(0, 20))
        arr2.append(randint(0, 20))
    print(f"6)\nПервый список: {arr1}\nВторой список: {arr2}")
    for i in arr1:
        if arr2.count(i) > 0:
            if i not in arr:
                arr.append(i)

    arr.sort()
    print(f"Отсортированное вхождение первого списка во второй: {arr}")

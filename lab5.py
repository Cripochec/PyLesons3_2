def replacement(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] > 0:
                my_list[i][j] = 1
            else:
                my_list[i][j] = 0
    return my_list


def array_output(arr):
    for row in arr:
        print(row)


def sorting_arr(arr):
    all_elements = []
    for row in arr:
        for element in row:
            all_elements.append(element)

    all_elements.sort()
    index = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = all_elements[index]
            index += 1
    return arr


def is_magic_square(matrix):
    n = len(matrix)
    # Проверяем, что матрица является квадратной
    if not all(len(row) == n for row in matrix):
        return False

    # Вычисляем сумму элементов в первой строке
    sum_row = sum(matrix[0])

    # Проверяем суммы строк
    for i in range(1, n):
        if sum(matrix[i]) != sum_row:
            return False

    # Проверяем суммы столбцов
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != sum_row:
            return False

    # Проверяем сумму главной диагонали
    if sum(matrix[i][i] for i in range(n)) != sum_row:
        return False

    # Проверяем сумму побочной диагонали
    if sum(matrix[i][n - i - 1] for i in range(n)) != sum_row:
        return False

    return True


def input_arr():
    while True:
        size = input("Введите размеры массива в формате (5:5): ")
        try:
            x, y = map(int, size.split(":"))
            if x > 0 and y > 0:
                break
            else:
                print("Введите корректные данные в формате (5:5)")
        except ValueError:
            print("Введите корректные данные в формате (5:5)")

    arr = []
    for _ in range(x):
        line = []
        for _ in range(y):
            while True:
                try:
                    n = int(input("Введите элемент массива:"))
                    break
                except ValueError:
                    print("Введите корректное число")
            line.append(n)
        arr.append(line)

    return arr

if __name__ == '__main__':

    #1
    print("1)")
    arr = input_arr()

    print("Изначальный массив:")
    array_output(arr)

    arr = replacement(arr)

    print("изменённый массив:")
    array_output(arr)

    # 2
    matrix = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    print("\n2)")
    array_output(matrix)
    if is_magic_square(matrix):
        print("Это магический квадрат.")
    else:
        print("Это не магический квадрат.")

    # 3
    print("\n3)\n")
    arr = input_arr()

    print("Изначальный массив:")
    array_output(arr)

    arr = sorting_arr(arr)

    print("\nОтсортированный массив:")
    array_output(arr)

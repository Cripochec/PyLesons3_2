class Subscript:
    def __init__(self, base_symbol):
        self.base_symbol = base_symbol

    def display(self):
        raise NotImplementedError("Subclass must implement display method")


class Superscript(Subscript):
    def __init__(self, base_symbol, superscript):
        super().__init__(base_symbol)
        self.superscript = superscript

    def display(self):
        print(f"{self.base_symbol}^{self.superscript}")


class SubscriptedSymbol(Subscript):
    def __init__(self, base_symbol, subscript):
        super().__init__(base_symbol)
        self.subscript = subscript

    def display(self):
        print(f"{self.base_symbol}_{self.subscript}")


# Функция для ввода данных от пользователя
def get_user_input(message):
    return input(message)


if __name__ == "__main__":
    # Ввод данных от пользователя
    base_symbol = get_user_input("Введите основной символ: ")
    superscript = get_user_input("Введите верхний индекс (если есть): ")
    subscript = get_user_input("Введите нижний индекс (если есть): ")

    # Создание объектов и вывод на экран
    if superscript and subscript:
        superscripted_symbol = Superscript(base_symbol, superscript)
        subscripted_symbol = SubscriptedSymbol(base_symbol, subscript)
        superscripted_symbol.display()
        subscripted_symbol.display()
    elif superscript:
        superscripted_symbol = Superscript(base_symbol, superscript)
        superscripted_symbol.display()
    elif subscript:
        subscripted_symbol = SubscriptedSymbol(base_symbol, subscript)
        subscripted_symbol.display()
    else:
        print(base_symbol)

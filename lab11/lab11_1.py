class Word:
    def __init__(self, word, pages):
        self.word = word
        self.pages = set(pages)
        self.page_count = len(pages)

    def __str__(self):
        return f"{self.word}: {self.pages}"

    @staticmethod
    def filter_by_page_count(words, min_pages):
        """
        Фильтрует слова по минимальному количеству страниц.
        """
        return [word for word in words if word.page_count > min_pages]

    @staticmethod
    def sort_alphabetically(words):
        """
        Сортирует слова в алфавитном порядке.
        """
        return sorted(words, key=lambda word: word.word)

    @staticmethod
    def find_pages(words, search_word):
        """
        Находит номера страниц для заданного слова.
        """
        for word in words:
            if word.word == search_word:
                return word.pages
        return None


# Массив объектов Word
words = [
    Word("my", [2, 4, 7, 8, 9]),
    Word("hello", [1, 3, 5]),
    Word("world", [1, 2, 3, 4, 5, 6]),
]

print("\nСписок слов:")
for word in words:
    print(word)

# Бесконечный цикл с пользовательским интерфейсом
while True:
    print("\nВыберите операцию:")
    print("1: Фильтр по количеству страниц")
    print("2: Сортировка по алфавиту")
    print("3: Поиск страниц для слова")
    print("0: Выход")

    choice = input("Операция: ")

    if choice == "1":
        min_pages = int(input("Введите минимальное количество страниц: "))
        filtered_words = Word.filter_by_page_count(words, min_pages)
        print("Отфильтрованные слова:")
        for word in filtered_words:
            print(word)
    elif choice == "2":
        sorted_words = Word.sort_alphabetically(words)
        print("Слова в алфавитном порядке:")
        for word in sorted_words:
            print(word)
    elif choice == "3":
        search_word = input("Введите слово для поиска: ")
        pages = Word.find_pages(words, search_word)
        if pages:
            print(f"Страницы для слова '{search_word}': {pages}")
        else:
            print(f"Слово '{search_word}' не найдено.")
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

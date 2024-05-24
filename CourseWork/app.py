import tkinter as tk
from joblib import load
import numpy as np
from sklearn.datasets import load_iris
from tkinter import messagebox


class BasicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Базовое приложение")
        self.root.geometry("800x600")

        # Переменные для ввода текста и радиокнопок
        self.entry1_text = tk.StringVar()
        self.entry2_text = tk.StringVar()
        self.entry3_text = tk.StringVar()
        self.entry4_text = tk.StringVar()
        self.radio_var = tk.StringVar(value="Линейная регрессия")

        # Создание виджетов
        self.create_widgets()

    def create_widgets(self):
        # Надпись и поля ввода текста сверху слева
        self.create_label_and_entries(0.06, 0.16, "Лепесток", self.entry1_text, self.entry2_text)

        # Надпись и поля ввода текста снизу слева
        self.create_label_and_entries(0.06, 0.6, "Чашелистник", self.entry3_text, self.entry4_text)

        # Радиокнопки справа сверху
        self.create_radio_buttons()

        # Кнопка справа снизу
        button = tk.Button(self.root, text="Результат", command=self.button_action)
        button.place(relx=0.8, rely=0.7, anchor=tk.SE)

        # Метка для вывода текста под кнопкой
        self.result_label = tk.Label(self.root, text="")
        self.result_label.place(relx=0.85, rely=0.8, anchor=tk.SE)

        # Изображение по центру
        self.create_center_image()

    def create_label_and_entries(self, relx, rely, label_text, var1, var2):
        label = tk.Label(self.root, text=label_text)
        label.place(relx=relx, rely=rely, anchor=tk.NW)

        entry1_label = tk.Label(self.root, text="Ширина:")
        entry1_label.place(relx=relx, rely=rely + 0.05, anchor=tk.NW)
        entry1 = tk.Entry(self.root, textvariable=var1)
        entry1.place(relx=relx + 0.1, rely=rely + 0.05, anchor=tk.NW)

        entry2_label = tk.Label(self.root, text="Длина:")
        entry2_label.place(relx=relx, rely=rely + 0.1, anchor=tk.NW)
        entry2 = tk.Entry(self.root, textvariable=var2)
        entry2.place(relx=relx + 0.1, rely=rely + 0.1, anchor=tk.NW)

    def create_radio_buttons(self):
        radio_frame = tk.Frame(self.root)
        radio_frame.place(relx=0.9, rely=0.16, anchor=tk.NE)

        radio_options = ["Линейная регрессия", "Логистическая регрессия", "Метод k-ближайших соседей",
                         "Решающие деревья"]
        for option in radio_options:
            radio_button = tk.Radiobutton(
                radio_frame,
                text=option,
                variable=self.radio_var,
                value=option
            )
            radio_button.pack(anchor=tk.W)

    def create_center_image(self):
        # Здесь нужно указать путь к вашему изображению
        image_path = "iris.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def button_action(self):
        text1 = float(self.entry1_text.get())
        text2 = float(self.entry2_text.get())
        text3 = float(self.entry3_text.get())
        text4 = float(self.entry4_text.get())
        selected_option = self.radio_var.get()

        if selected_option == "Линейная регрессия":
            predicted_class, accuracy = predict_linear_regression(text4, text3, text2, text1)
            accuracy *= 100
            result_text = f"тип цветка: {predicted_class}\nТочность : {accuracy:.2f}"
        elif selected_option == "Логистическая регрессия":
            predicted_class, accuracy = predict_logistic_regression(text4, text3, text2, text1)
            result_text = f"тип цветка: {predicted_class}\nТочность : {accuracy:.2f}"
        elif selected_option == "Метод k-ближайших соседей":
            predicted_class, accuracy = predict_knn_regression(text4, text3, text2, text1)
            accuracy *= 100
            result_text = f"тип цветка: {predicted_class}\nТочность : {accuracy:.2f}"
        else:
            predicted_class, accuracy = predict_decisive_trees_regression(text4, text3, text2, text1)
            result_text = f"тип цветка: {predicted_class}\nТочность : {accuracy:.2f}"

        self.result_label.config(text=result_text)


def predict_linear_regression(sepal_length, sepal_width, petal_length, petal_width):
    # Загрузка сохраненной модели
    model = load('linear_regression.joblib')

    # Новые данные для предсказания (длина и ширина чашелистика и лепестка)
    new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Предсказание типа цветка
    prediction = model.predict(new_data)

    # Названия классов (типов цветка)
    class_names = ['setosa', 'versicolor', 'virginica']

    # Получение имени предсказанного типа цветка
    predicted_class = class_names[int(prediction[0])]

    # Добавляем вычисление точности
    X_test, y_test = load_iris(return_X_y=True)
    accuracy = model.score(X_test, y_test)

    return predicted_class, accuracy


def predict_logistic_regression(sepal_length, sepal_width, petal_length, petal_width):
    # Загрузка сохраненной модели
    model = load('logistic_regression.joblib')

    # Новые данные для предсказания (длина и ширина чашелистика и лепестка)
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Предсказание типа цветка
    predicted_class = model.predict(new_data)

    # Оценка точности предсказания
    predicted_proba = model.predict_proba(new_data)
    max_proba = max(predicted_proba[0])
    accuracy = max_proba * 100

    # Названия классов (типов цветка)
    class_names = ['setosa', 'versicolor', 'virginica']

    # Получение имени предсказанного типа цветка
    predicted_class_name = class_names[predicted_class[0]]

    return predicted_class_name, accuracy


def predict_knn_regression(sepal_length, sepal_width, petal_length, petal_width):
    # Загрузка сохраненной модели
    model = load('knn.joblib')

    # Новые данные для предсказания (длина и ширина чашелистика и лепестка)
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Предсказание типа цветка
    predicted_class = model.predict(new_data)

    # Оценка точности предсказания
    accuracy = model.score(new_data, predicted_class)

    # Названия классов (типов цветка)
    class_names = ['setosa', 'versicolor', 'virginica']

    # Получение имени предсказанного типа цветка
    predicted_class_name = class_names[predicted_class[0]]

    return predicted_class_name, accuracy


def predict_decisive_trees_regression(sepal_length, sepal_width, petal_length, petal_width):
    # Загрузка сохраненной модели
    model = load('decisive_trees.joblib')

    # Новые данные для предсказания (длина и ширина чашелистика и лепестка)
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Предсказание типа цветка
    predicted_class = model.predict(new_data)

    # Оценка точности предсказания
    predicted_proba = model.predict_proba(new_data)
    max_proba = max(predicted_proba[0])
    accuracy = max_proba * 100

    # Названия классов (типов цветка)
    class_names = ['setosa', 'versicolor', 'virginica']

    # Получение имени предсказанного типа цветка
    predicted_class_name = class_names[predicted_class[0]]

    return predicted_class_name, accuracy


if __name__ == "__main__":
    root = tk.Tk()
    app = BasicApp(root)
    root.mainloop()

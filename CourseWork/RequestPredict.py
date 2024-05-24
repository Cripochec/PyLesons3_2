from joblib import load
import numpy as np
from sklearn.datasets import load_iris


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


# Пример использования функции
sepal_length = 5.1
sepal_width = 3.5
petal_length = 1.4
petal_width = 0.2


predicted_class, accuracy = predict_linear_regression(sepal_length, sepal_width, petal_length, petal_width)
print(f"Предсказанный тип цветка: {predicted_class}")
print(f"Точность предсказания: {accuracy:.2f}")

predicted_class, accuracy = predict_logistic_regression(sepal_length, sepal_width, petal_length, petal_width)
print(f"Предсказанный тип цветка: {predicted_class}")
print(f"Точность предсказания: {accuracy:.2f}")

predicted_class, accuracy = predict_knn_regression(sepal_length, sepal_width, petal_length, petal_width)
print(f"Предсказанный тип цветка: {predicted_class}")
print(f"Точность предсказания: {accuracy:.2f}")

predicted_class, accuracy = predict_decisive_trees_regression(sepal_length, sepal_width, petal_length, petal_width)
print(f"Предсказанный тип цветка: {predicted_class}")
print(f"Точность предсказания: {accuracy:.2f}")
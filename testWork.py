import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Чтение данных из файла XLSX, пропуская заголовок
data = pd.read_excel("testWork.xlsx", header=None, names=["x", "y"])

# Удаление строк с некорректными данными
data = data.dropna()  # Удаляем строки с пустыми значениями

# Преобразование данных к числовому типу и удаление строк с ошибками
data["x"] = pd.to_numeric(data["x"], errors='coerce')
data["y"] = pd.to_numeric(data["y"], errors='coerce')
data = data.dropna()

# Проверка, что данные загружены корректно
print(data)

# Определение значений x и y
X = data[["x"]]  # X должен быть двумерным массивом
y = data["y"]

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)

# Коэффициенты линейной регрессии
intercept = model.intercept_
slope = model.coef_[0]

print(f"Уравнение линейной регрессии: y = {slope} * x + {intercept}")

# Прогнозирование значения для x = x0
x0 = 110
x0_df = pd.DataFrame([[x0]], columns=["x"])
y_pred = model.predict(x0_df)
print(f"Прогнозное значение y для x = {x0}: {y_pred[0]}")

# Визуализация данных и линии регрессии
plt.scatter(X, y, color='blue', label='Данные')
plt.plot(X, model.predict(X), color='red', label='Линия регрессии')
plt.scatter([x0], [y_pred], color='green', label=f'Прогноз для x0={x0}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

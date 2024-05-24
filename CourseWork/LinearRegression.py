import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump
import numpy as np

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)  # Обучение модели

# Кросс-валидационное предсказание
y_pred = cross_val_predict(model, X, y, cv=5)

# Оценка модели на основе кросс-валидации
cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
mse_cv = -np.mean(cv_scores)

# Сохранение результатов предсказания
dump(model, 'linear_regression.joblib')

# Оценка модели
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Среднеквадратичная ошибка: %.2f" % mse)
print("Коэффициент детерминации (R^2): %.2f" % r2)
print("Среднеквадратичная ошибка на основе кросс-валидации: %.2f" % mse_cv)

# Визуализация результатов
plt.scatter(X[:, 0], y, color='black', label='Истинные значения')
plt.scatter(X[:, 0], y_pred, color='blue', label='Предсказанные значения')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Целевой показатель')
plt.title('Линейная регрессия на наборе данных Iris')
plt.legend()
plt.show()

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Создание и обучение модели логистической регрессии
model = LogisticRegression(max_iter=1000)
model.fit(X, y)  # Обучение модели

# Кросс-валидационное предсказание
y_pred = cross_val_predict(model, X, y, cv=5)

# Сохранение модели
dump(model, 'logistic_regression.joblib')

# Оценка модели
accuracy = accuracy_score(y, y_pred)
print("Точность: %.2f" % accuracy)
print("Отчет по классификации:")
print(classification_report(y, y_pred))

# Визуализация результатов
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.binary, edgecolor='k', label='Истинные значения')
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap=plt.cm.cool, marker='x', label='Предсказанные значения')
plt.xlabel('Длина чашелистика')
plt.ylabel('Ширина чашелистика')
plt.title('Логистическая регрессия на наборе данных Iris')
plt.legend()
plt.show()

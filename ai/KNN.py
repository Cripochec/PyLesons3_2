from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Создание модели k-NN
model = KNeighborsClassifier(n_neighbors=5)

# Обучение модели на всем наборе данных
model.fit(X, y)

# Сохранение модели
dump(model, 'knn.joblib')

# Кросс-валидационное предсказание
y_pred = cross_val_predict(model, X, y, cv=5)

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
plt.title('Метод k-NN на наборе данных Iris')
plt.legend()
plt.show()

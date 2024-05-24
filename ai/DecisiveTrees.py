from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Создание модели решающего дерева
model = DecisionTreeClassifier()

# Обучение модели
model.fit(X, y)

# Кросс-валидационное предсказание
y_pred = cross_val_predict(model, X, y, cv=5)

# Сохранение модели
dump(model, 'decisive_trees.joblib')

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
plt.title('Решающее дерево на наборе данных Iris')
plt.legend()
plt.show()

# Визуализация дерева решений
plt.figure(figsize=(12,8))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title('Структура решающего дерева')
plt.show()


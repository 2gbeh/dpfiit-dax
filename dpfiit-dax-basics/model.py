import pandas
from sklearn.tree import DecisionTreeClassifier

dataset = pandas.read_csv('src/users.csv')
X = dataset[['GENDER', 'AGE']]
y = dataset['INTEREST']

model = DecisionTreeClassifier()
model.fit(X, y)
consideration = [[1, 3], [2, 3]]
prediction = model.predict(consideration)

print(prediction)

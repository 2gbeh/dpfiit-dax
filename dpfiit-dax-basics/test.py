import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = pandas.read_csv('src/users.csv')
X = dataset[['GENDER', 'AGE']]
y = dataset['INTEREST']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

rate = accuracy_score(y_test, prediction)
print(rate)

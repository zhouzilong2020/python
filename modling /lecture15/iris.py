from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
iris=datasets.load_iris()
X=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(X, y)
bayes = GaussianNB()
model=bayes.fit(data_train, target_train)
pred = model.predict(data_test)
error=pred-target_test
# print(target_test)
# print(error) 
cnt = 0
for i in error:
    if i != 0:
        cnt+=1
print(1-cnt/error.size)
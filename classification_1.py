from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
iris = datasets.load_iris()
type(iris)
print(iris.keys())
type(iris.data)
type(iris.target)
iris.data.shape
iris.target_names
X=iris.data
y=iris.target
df=pd.DataFrame(x,columns=iris.feature_names)
print(df.head())
_=pd.plotting.scatter_matrix(df,c=y,figsize=[8,8], s=150, marker='D')
##################################################
#####################Knn classifier
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(iris['data'],iris['target'])
iris['data'].shape
iris['target'].shape
# Predicting on unlabeled data
X_new = np.array([[5.6, 2.8, 3.9, 1.1],
       [5.7, 2.6, 3.8, 1.3],
       [4.7, 3.2, 1.3, 0.2]])
prediction = knn.predict(X_new)
####Measuriing model performance
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.30,random_state=21, stratify=y)
knn=KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(y_pred)
knn.score(X_test,y_test)

import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir("D:/DataCamp/1_Supervised Learning with Scikit Learn")
boston=pd.read_csv('boston.csv')
print(boston.head())
# first we identified that target variable is medv
# now we separate medv
X=boston.drop('medv',axis=1).values
y=boston['medv'].values
X_rooms=X[:,6]
type(X_rooms)
type(y)
y=y.reshape(-1,1)
X_rooms=X_rooms.reshape(-1,1)
plt.scatter(X_rooms, y)
plt.ylabel('Value of house /1000 ($)')
plt.xlabel('Number of rooms')
plt.show()
import numpy as np
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_rooms,y)
prediction_space = np.linspace(min(X_rooms),max(X_rooms)).reshape(-1, 1)
plt.scatter(X_rooms,y,color='blue')
plt.plot(prediction_space, reg.predict(prediction_space),color='black', linewidth=3)
plt.show()
##################################################
##################################################
# we use  i.e ordinary least sqaures as simply using distances would not help us
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=42)
reg_all=LinearRegression()
reg_all.fit(X_train,y_train)
y_pred=reg_all.predict(X_test)
reg_all.score(X_test,y_test)
####################Cross_validation
from sklearn.model_selection import cross_val_score
reg2=LinearRegression()
cv_results=cross_val_score(reg2,X,y,cv=5)
print(cv_results)
np.mean(cv_results)
##########################################Regularisation
# Large coefficents can lead to overfitting
# Penalizing large coefficents is Regularization
# Type 1 Ridge Regression
# Loss fxn=OLS fxn + alpha * E i from 1 to n (ai) **2
# Here alpha is a parameter we need to choose
# Picking alpha here is same as picking K for KNN
# Alpha controls complexity 
# Aplha=0 we get back OLS == Lead to Overfitting
# Very high Alpha can lead to underfitting
from sklearn.linear_model import Ridge
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=42)
ridge=Ridge(alpha=.1,normalize=True)
ridge.fit(X_train,y_train)
ridge_pred=ridge.predict(X_test)
ridge.score(X_test,y_test)
#Normalize=True ensures all our variables are on same scale
##########################################################
# Type 2 lasso regression 
#loss function = OLS + alpha* E from i to n mod(ai)
from sklearn.linear_model import Lasso
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=42)
lasso=Lasso(alpha=.1,normalize=True)
lasso.fit(X_train,y_train)
lasso_pred=ridge.predict(X_test)
lasso.score(X_test,y_test)
# Lasso regression can be used to select important features of a dataset
# because it shrinks the coefficent of less important features exactly to zero

from sklearn.linear_model import Lasso

names = boston.drop('medv', axis=1).columns

lasso = Lasso(alpha=0.1)

lasso_coef = lasso.fit(X, y).coef_

_ = plt.plot(range(len(names)), lasso_coef,color='blue')
_ = plt.xticks(range(len(names)), names, rotation=60)
_ = plt.ylabel('Coefficients')
plt.show()


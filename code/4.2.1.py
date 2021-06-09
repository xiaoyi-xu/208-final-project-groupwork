import pandas as pd
from sklearn import preprocessing,model_selection
import warnings
warnings.simplefilter("ignore")

housing = pd.read_csv('../data/heart.csv')

set1 = ['age','sex','cp','trtbps','chol','thalachh','oldpeak','caa','thall','output']

contin = ['age','trtbps','chol','thalachh','oldpeak']

data = housing[set1]

data[contin] = preprocessing.StandardScaler().fit_transform(data[contin])

data_tr,data_te = model_selection.train_test_split(data,test_size = 0.33)

X_tr, y_tr = data_tr.iloc[:,:-1],data_tr.iloc[:,-1]

X_te, y_te = data_te.iloc[:,:-1],data_te.iloc[:,-1]

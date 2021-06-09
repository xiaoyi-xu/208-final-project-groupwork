from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb

svc = svm.SVC(kernel = 'linear', C = 1)
svc2 = svm.SVC(kernel = 'sigmoid', C = 1)
rf = RandomForestClassifier()
xgboost= xgb.XGBClassifier(eval_metric=['logloss','auc','error'])
knn = KNeighborsClassifier()

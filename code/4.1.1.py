import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotnine as p9
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
data = pd.read_csv('../data/heart.csv')
y = data['output']
x = data.iloc[:,0:13]
model = sm.OLS(y, x).fit()
print(model.summary())

Xtrain, Xtest, Ytrain, Ytest = train_test_split(x,y,test_size=0.3,random_state=0)
results = pd.DataFrame({'output': Ytrain, 
                        'resids': model.resid, # 残差
                        'std_resids': model.resid_pearson, # 方差标准化的残差
                        'fitted': model.predict() # y预测值
                       })
print(results.head())

#raw residuals vs. fitted
residsvfitted = plt.plot(results['fitted'], results['resids'],  'o')
l = plt.axhline(y = 0, color = 'grey', linestyle = 'dashed') # 绘制y=0水平线
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted')
plt.show(residsvfitted)

# q-q plot
qqplot = sm.qqplot(results['std_resids'], line='s')
plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.title('Normal Q-Q')
plt.show(qqplot)
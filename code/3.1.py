import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('../data/heart.csv')
des_data = data[['age','trtbps','thalachh','chol','oldpeak']]
print(des_data.describe())

corrPearson = data.corr(method="spearman")
figure = plt.figure(figsize=(10,8))
sns.heatmap(corrPearson,annot=True,cmap='RdYlGn', vmin=-1, vmax=+1)
plt.title("PEARSON")
plt.xlabel("COLUMNS")
plt.ylabel("COLUMNS")
plt.show()
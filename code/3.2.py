import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('../data/heart.csv')
import plotnine as p9
data['output'] = data['output'].astype('object')

data['sex'] = data['sex'].astype('object')

data['cp'] = data['cp'].astype('object')

data['fbs'] = data['fbs'].astype('object')

data['restecg'] = data['restecg'].astype('object')

data['exng'] = data['exng'].astype('object')

data['slp'] = data['slp'].astype('object')

data['caa'] = data['caa'].astype('object')

data['thall'] = data['thall'].astype('object')

print(p9.ggplot(data, p9.aes(x = 'age',fill = 'output')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'trtbps',fill = 'output')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'thalachh',fill = 'output')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'chol',fill = 'output')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'oldpeak',fill = 'output')) + p9.geom_density(alpha=.2))

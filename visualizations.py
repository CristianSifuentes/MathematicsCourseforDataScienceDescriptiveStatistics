import pandas as pd 
import seaborn as sns

iris = sns.load_dataset('iris')

iris.head()

sns.scatterplot(data=iris, x = 'sepal_length', y = 'petal_length', hue = 'species')

sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length', hue = 'species')

sns.boxplot(x = 'species', y = 'sepal_length', data = iris)

sns.barplot(x = 'species', y = 'sepal_length', data = iris)
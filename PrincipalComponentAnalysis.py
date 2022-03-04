import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


iris = sns.load_dataset('iris')

scaler = StandardScaler()
scaled = scaler.fit_transform(
    iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
    )

covariance_matrix = np.cov(scaled.T)
covariance_matrix

sns.pairplot(iris)

sns.jointplot(x= iris['petal_length'], y=iris['petal_width'])
sns.jointplot(x = scaled[:, 2], y = scaled[:,3])

eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

eigen_values

eigen_vectors

variance_explained = []
for i in eigen_values:
    variance_explained.append((i/sum(eigen_values))*100)

print(variance_explained)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(scaled)

pca.explained_variance_ratio_

reduced_scaled = pca.transform(scaled)

iris['pca_1'] = scaled[:,0]
iris['pca_2'] = scaled[:,1]
sns.jointplot(iris['pca_1'], iris['pca_2'], hue = iris['species'])
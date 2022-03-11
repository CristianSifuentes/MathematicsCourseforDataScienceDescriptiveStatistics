# MathematicsCourseforDataScienceDescriptiveStatistics
'https://github.com/ekalinin/github-markdown-toc/edit/master/README.md'
## Required

Installation:

    pip install pandas pip install seaborn



## Description

This is a repository where I write about descriptive statistics oriented for Machine Learnig and Data Science. 

In this repository we can see what is the general propose for descriptive statistics and we also get knowlage for try to diference between descriptive statistics and inferencial statistics.


## Table of Contents (Optional)

Descriptive statistics for Data Science.

<!--ts-->
   * [What is descriptive statistics for?](#what-is-descriptive-statistics-for)
      * [Descriptive statistics vs statistics inference](#descriptive-statistics-vs-statistics-inference)
        * [Why learn statistics?](#why-learn-statistics)
      * [Workflow in data science](#workflow-in-data-science)
        * [Flow](#flow)
   * [Descriptive statistics for analytics](#descriptive-statistics-for-analytics)
      * [Data types in inferential statistics](#data-types-in-inferential-statistics)
      * [Measures of central tendency](#measures-of-central-tendency)
        * [Mean or average → mean(df)](#mean-or-average→mean(df))
        * [Median → median(df)](#median→median(df))
        * [Mode](#mode)
        * [Application and Notes in Python (Deepnote)](#application-and-notes-in-python-(deepnote))
      * [Measures of dispersion](#measures-of-dispersion)
        * [Standard deviation](#standard-deviation)
        * [Dispersion measures in Python](#dispersion-measures-in-python)
        * [Limits for outlier detection (with symmetrically distributed data)](#limits-for-outlier-detection-(with-symmetrically-distributed-data))
      * [Visual exploration of data](#visual-exploration-of-data)  
        * [Scatter Plots in Data Analysis](#scatter-plots-in-data-analysis)
   * [Statistics on data ingestion](#statistics-on-data-ingestion)
      * [Processing pipelines for numeric variables](#processing-pipelines-for-numeric-variables)
        * [Linear scaling](#linear-scaling)
        * [Linear Scaling Types](#linear-scaling-types)
        * [Linear transformations in Python](#linear-transformations-in-python)
        * [Nonlinear transformation](#nonlinear-transformation)
        * [Nonlinear transformations in Python](#nonlinear-transformations-in-python)
      * [Processing pipelines for categorical variables](#processing-pipelines-for-categorical-variables)
        * [Categorical Data Processing in Python](#categorical-data-processing-in-python)
      * [Covariance and correlation coefficient](#covariance-and-correlation-coefficient)  
        * [Covariance matrix](#covariance-matrix)
        * [Covariance matrix in Python](#covariance-matrix-in-python)
   * [Bonus: Pandas and Seaborn commands used in the course](#Bonus:-Pandas-and-Seaborn-commands-used-in-the-course)      
<!--te-->



What is descriptive statistics for?
============

La estadística descriptiva sirve para 2 cosas:

Anális exploratorio de la información.
Preprocesamiento de la información antes de tener un modelo de machine learning.

Descriptive Statistics vs Statistics inference
-----------

Estadística descriptiva: resumir un historial de datos.

Estadística inferencial: predecir con datos.


Why learn statistics?
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Workflow in data science
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Flow
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Descriptive statistics for analytics
============

Data types in inferential statistics
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```


Measures of central tendency
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Mean or average → mean(df)
-----------

Here's an example of TOC creating for a local README.md:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Mean or average → mean(df)
-----------

Median → median(df

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Mean or average → mean(df)
-----------
```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Mode
-----------
```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Application and Notes in Python (Deepnote)
-----------
```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md
```

Statistics on data ingestion
============

Processing pipelines for numeric variables
-----------

Linear scaling
-----------

It is important to normalize the data (do linear scaling), before passing it through a machine learning model. This is because the models are efficient if they are in the same range [-1, 1]. If they are not in that range, they have to be transformed (scaled).

There are different types of linear scaling (max-min, Clipping, Z-score, Winsorizing, etc.). They are normally used when the data is symmetric or uniformly distributed.


Linear Scaling Types
-----------
* Min-max: Makes a transformation so that the data falls into the range [-1, 1] by means of a formula. It is one of the most used. It works best for uniformly distributed data.
* Clipping: forces the data that is out of the range to be transformed into data within it. This method is not highly recommended because it discards outlier values ​​that may be working fine.
* Winsorizing: A variation of clipping that uses the quartiles as endpoints.
* Z-Score: it is one of the most common because it is based on the average and standard deviation. It works best for "normally" distributed (Gaussian bell shaped) data.


![Alt text](/Images/linear-scaling-types.png?raw=true "Linear Scaling Types")

-----------

This dataset from scikit-learn will be used: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html

```python
import timeit #para medir el tiempo de ejecución de los modelos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model #datasets para descargar un modelo y linear_model para hacer una regresión lineal

X, y = datasets.load_diabetes(return_X_y=True) #carga el dataset
raw = X[:, None, 2] #transformación en las dimensiones para que se ajuste al formato de entrada del 

```
```python
#reglas de escalamiento lineal, aplicamos max-min
max_raw = max(raw)
#raw = datos crudos
min_raw = min(raw)
scaled = (2*raw - max_raw - min_raw)/(max_raw - min_raw)

# es importante tener una noción de los datos originales antes y después de escalarlos:
fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].hist(raw)
axs[1].hist(scaled)

```

```python
(array([32., 66., 98., 90., 64., 50., 23., 12.,  5.,  2.]),
 array([-1. , -0.8, -0.6, -0.4, -0.2,  0. ,  0.2,  0.4,  0.6,  0.8,  1. ]),
 <BarContainer object of 10 artists>)s
```

![Alt text](/Images/linear-transformations-in-python.png?raw=true "linear transformations in python")


```python
# modelos para entrenamiento
def train_raw():
    linear_model.LinearRegression().fit(raw, y)

def train_scaled():
    linear_model.LinearRegression().fit(scaled, y)
```

```python
raw_time = timeit.timeit(train_raw, number=100) #repite la ejecución del código 100 veces y sobre eso calcula el tiempo
scaled_time = timeit.timeit(train_scaled, number=100)
print(f'train raw: {raw_time}')
print(f'train scaled: {scaled_time}')
```

It can be seen how by normalizing the data, the algorithm becomes more efficient.

Scikit Learn has a preprocessing part, in its documentation you will find how to standardize numerical and categorical data.

Scikit Learn Utilities: https://scikit-learn.org/stable/modules/preprocessing.html


Nonlinear transformation
-----------

When the data is not symmetric or uniform, but is very skewed, a transformation is applied so that they have a symmetric distribution and linear scaling can be applied.

There are different types of nonlinear functions: logarithms, sigmoids, polynomials, etc. These functions can be applied to the data to transform it and make it homogeneous.

Tanh(x)

The tanh is always in a range from -1 to 1 in Y, so when the values ​​of X are very high, they will be very close to |1|. You could also calibrate the data to fit the curve by dividing it by a parameter a.

![Alt text](/Images/Tanh.png?raw=true "tanh")

Square root

Other polynomial functions, for example the square root (x½), can also cause a distribution to normalize.

![Alt text](/Images/square-root.png?raw=true "square root")


Nonlinear transformations in Python
-----------

```python
df = pd.read_csv('cars.csv')

```


```python
# Here it can be seen how the distribution is strongly skewed
df.price_usd.hist()


```
![Alt text](/Images/heavily-biased.png?raw=true "heavily-biased")


```python
# Transformation with tanh(x)

# This line takes the column and applies it to an entire math function
p = 10000
df.price_usd.apply(lambda x: np.tanh(x/p)).hist()
```
![Alt text](/Images/apply.png?raw=true "apply")


In this documentation you will find several ways to do those non-linear transformations. That way you can apply the functions that Scikit Learn brings to make the transformations.

Map data to a Gaussian distribution: https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html


Processing pipelines for categorical variables
============
When you have categorical variables, you do a numerical mapping. For that there are 2 methods, so that they are easily interpretable in machine learning models:

Dummy: it is the most compact representation that can be had of the data. It is best used when the inputs are linearly independent variables (they do not have a significant degree of correlation). That is, when the categories are known to be independent of each other.
One-hot: it is more extensive. Allows you to include categories that were not in the dataset initially. So that if a category is filtered that was not included, it can still be represented numerically and not as an error in the model (this model is cooler and is the one used).
There are bugs in Pandas notation and they treat them as both models being the same, but in reality the Dummy is not used. Still, in Pandas the method is .get_dummies().

Application example of both:

![Alt text](/Images/dummy-one-hot.png?raw=true "dummy one-hot")


Categorical Data Processing in Python
-----------
```python
import pandas as pd

df = pd.read_csv('cars.csv')
```
Pandas dummies documentation: https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html

```python
pd.get_dummies(df['engine_type'])

| Primer encabezado | Segundo encabezado |
| ------------- | ------------- |
| Contenido de la celda  | Contenido de la celda  |
| Contenido de la celda  | Contenido de la celda  |

```



One-hot documentation with Scikit:  https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features

```python
import sklearn.preprocessing as preprocessing

encoder = preprocessing.OneHotEncoder(handle_unknown='ignore')
```

```python
encoder.fit(df[['engine_type']].values)

OneHotEncoder(handle_unknown='ignore')
```

```python
encoder.transform([['gasoline'],['diesel'], ['aceite']]).toarray()

array([[0., 0., 1.],
       [1., 0., 0.],
       [0., 0., 0.]])

```

Discrete numeric variables (integers) can also be encoded as categorical


```python
encoder.fit(df[['year_produced']].values)

OneHotEncoder(handle_unknown='ignore')
```

```python
encoder.transform([[2016], [2009], [190]]).toarray()

array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])



```

In this case, the dimensionality of the dataset is affected too much, so we must seek to reduce the data.



Covariance and correlation coefficient
============
If 2 variables are correlated, they would be providing the same information, so it would not be useful to have the 2 variables in the model if their correlation is very high.

The way to find the correlations is using the covariance:

![Alt text](/Images/covariance.png?raw=true "Covariance")

But since the scales of X and Y can be different, then the correlation coefficient (ρ) is used:

![Alt text](/Images/correlation-coefficient.png?raw=true "Correlation coefficient")

The higher the correlation coefficient (closer to 1), the higher the correlation and vice versa (closer to 0), and if the value is close to -1, then there is an inverse correlation:

![Alt text](/Images/inverse-correlation.png?raw=true "Inverse-correlation")

Covariance matrix
-----------

When there are many variables (which is usually the case), all possible covariances of the pairs of data in the dataset must be calculated. The result of this calculation, represented in a matrix, is the covariance matrix.

![Alt text](/Images/covariance-matrix.png?raw=true "Covariance matrix")

It is always used in exploratory data analysis.


Covariance matrix in Python
-----------
```python
 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler 

iris = sns.load_dataset('iris')
```

```python
 
sns.pairplot(iris, hue='species') ##this graph is useless if there are too many variables

```
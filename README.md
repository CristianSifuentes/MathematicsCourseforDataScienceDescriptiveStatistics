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
        * [Linear scaling](#mode)
        * [Linear Scaling Types](#mode)
        * [Linear transformations in Python](#mode)
        * [Nonlinear transformation](#mode)
        * [Nonlinear transformations in Python](#mode)
      * [Processing pipelines for categorical variables](#Processing-pipelines-for-categorical-variables)
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
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../MathematicsCourseforDataScienceDescriptiveStatistics/cars.csv"))

# Desviación estandar
print(df['price_usd'].std())

# Rango = valor max - valor min
rango = df['price_usd'].max() - df['price_usd'].min()
print(rango)


# Quartiles
median = df['price_usd'].median()
Q1 = df['price_usd'].quantile(q=0.25)
Q3 = df['price_usd'].quantile(q=0.75)
min_val = df['price_usd'].quantile(q=0)
max_val = df['price_usd'].quantile(q=1.0)
print(min_val, Q1, median, Q3, max_val)

iqr = Q3 - Q1
print(iqr)


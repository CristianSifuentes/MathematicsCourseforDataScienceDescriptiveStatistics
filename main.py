import pandas as pd 
import os
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../MathematicsCourseforDataScienceDescriptiveStatistics/cars.csv"))
print(df.dtypes)


print(df.describe())


print(df.head())

# promedio
print(df['price_usd'].mean())

# mediana
print(df['price_usd'].median())

#
print(df['price_usd'].plot.hist(bins=20))

print(sns.displot(df, x = 'price_usd', hue = 'manufacturer_name'))

print(sns.displot(df, x="price_usd", hue="engine_type"))

print(sns.displot(df, x='price_usd', hue = 'engine_type', multiple='stack'))

print(df.groupby('engine_type').count())


Q7_df = df[(df['manufacturer_name']=='Audi') & (df['model_name']=='Q7')]
sns.histplot(Q7_df, x='price_usd', hue = 'year_produced')
print(Q7_df)


sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))
sns.boxplot(x='color', y='price_usd', data=df, palette='Blues')
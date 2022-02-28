import pandas as pd 
import os


df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../MathematicsCourseforDataScienceDescriptiveStatistics/cars.csv"))
print(df.dtypes)


print(df.describe())


print(df.head())

print(df['price_usd'].mean())


print(df['price_usd'].median())

print(df['price_usd'].plot.hist(bins=20))
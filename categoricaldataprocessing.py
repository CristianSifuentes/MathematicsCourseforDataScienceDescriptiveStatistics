import os
import pandas as pd 
import sklearn.preprocessing as preprocessing

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../MathematicsCourseforDataScienceDescriptiveStatistics/cars.csv"))
print(df.dtypes)


pd.get_dummies(df['engine_type'])

encoder = preprocessing.OneHotEncoder(handle_unknown='ignore')

encoder.fit(df[['engine_type']].values)

encoder.transform([['gasoline'],['diesel'],['aceite']]).toarray()

encoder.fit(df[['year_produced']].values)

encoder.transform([[2016],[2009],[190]]).toarray()
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
#print(pd.get_dummies(data['whoAmI']))
data['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)
data.pop('whoAmI')
print(data.head())

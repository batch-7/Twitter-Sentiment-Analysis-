
import os
import pandas as pd
os.chdir("C:/Users/PC/Documents/dataset")
data = pd.read_csv("product1.csv")
data
 

print (data['emotion_in_tweet_is_directed_at'])
 

data.apply(lambda x: x.count(), axis=1)
 
print (data['emotion_in_tweet_is_directed_at'].isnull())
 
missing_values = ["n/a","na","--"]
os.chdir("C:/Users/PC/Documents/dataset")
data = pd.read_csv("product1.csv",na_values = missing_values)
data.isnull()
 
cnt =0
for row in data:
    try:
        int(row)
        df.loc[cnt]=np.nan
    except ValueError:
        pass
    cnt+=1
print (data.isnull().sum())
 
print(data.isnull().values.any())
print(data.isnull().sum().sum())
data["emotion_in_tweet_is_directed_at"].fillna("0",inplace = True)
print (data.isnull().sum())
 









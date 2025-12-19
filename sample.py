import pandas as pd
df=pd.read_csv("C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\NewCompanyDetails.csv")
df=df.drop_duplicates()
df=df.dropna()
df['revenue']=df['revenue'].replace('[^0-9]','',regex=True).astype(int)
df['total workers']=df['workers']+df['previous_workers']
df.to_csv("newdetails.csv")
print(df)

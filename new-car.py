import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt 
import seaborn as sns

class Car_data:
    
    def __init__(self):
        self.df = self.builddf()
    
    def builddf(self):
        df = pd.read_csv('carData.csv')
        subset = df [['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
        car = [tuple(x) for x in subset.to_numpy()]
        return df

car_data = Car_data()    
print("\n data frame \n", car_data.df)
print('\n mean \n', car_data.df.mean())
print('\n describe \n', car_data.df.describe())

#plt.hist(car_data.df.Year, bins = 20, color = ('yellow'), edgecolor = 'red')
#plt.xlabel('valeurs')
#plt.ylabel('nombres')
#plt.title('Year ')

#plt.hist(car_data.df.Selling_Price, bins = 5, color = ('black'), edgecolor = 'red')
#plt.xlabel('valeurs')
#plt.ylabel('nombres')
#plt.title('Selling price ')

#plt.hist(car_data.df.Kms_Driven, bins = 100, color = ('black'), edgecolor = 'red')
#plt.xlabel('valeurs')
#plt.ylabel('nombres')
#plt.title('kilometers ')

plt.hist(car_data.df.Present_Price, bins = 50, color = ('black'), edgecolor = 'red')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Present price "Argus" ')


#sns.set_theme(style="ticks")
#exercise = sns.load_dataset("car_data.df")
#g = sns.catplot(x="Year", y="Selling_Price", hue="Kms_Driven", data=car_data.df)

a= np.random.randn(100)
b=np.random.randn(100)
sns.jointplot(a,b)
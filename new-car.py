import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

class Car_data:
    
    def __init__(self):
        self.df = self.builddf()
    
    def builddf(self):
        df = pd.read_csv('carData.csv')
        subset = df [['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
        car = [tuple(x) for x in subset.to_numpy()]
        return df

car_data = Car_data()    
print("data frame", car_data.df)
print('mean', car_data.df.mean())
print('describe', car_data.df.describe())

plt.hist(car_data.df, bins = 5, color = ('yellow', 'black', 'white', 'blue', 'red', 'green', 'purple', 'orange', 'brown'), edgecolor = 'red')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("AirQualityUCI.csv", sep=";")
print(data)
x = data["Date"]
y = data["NO2(GT)"]
year=[]
month=[]
day=[]
xSplit=[]
colors=["c",'g','b','r','m','y']

for i in range(len(x)):
    xSplit.append(x[i].split("/"))
    
for i in range(len(xSplit)):
    day.append(xSplit[i][0])
    month.append(xSplit[i][1])
    year.append(xSplit[i][2])

data["Year"] = year
data["Month"] = month
data["Day"] = day
#print(data)
data2004=data.copy(deep=True)
data2005=data.copy(deep=True)
for i in range(len(data2004)):
    if data2004["Month"][i]!="03" or data2004["NO2(GT)"][i]==-200 or data2004["Year"][i]=="2005" or data2004["Time"][i]!="12.00.00":
        data2004.drop(i,inplace=True)

x=data2004["Day"]
y=data2004["NO2(GT)"]
plt.scatter(x,y, label="2004")

for i2 in range(len(data2005)):
    if data2005["Month"][i2]!="03" or data2005["NO2(GT)"][i2]==-200 or data2005["Year"][i2]=="2004" or data2005["Time"][i2]!="12.00.00":
        data2005.drop(i2,inplace=True)

x2=data2005["Day"]
y2=data2005["NO2(GT)"]
plt.scatter(x2,y2, c="r", label="2005")



plt.legend()
plt.show()
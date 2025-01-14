import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("AirQualityUCI.csv", sep=";")
# print(data)
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

#print(data["Month"])
for i in range(len(data)):
    #print(data["Month"][i],data["Year"][i])
    if data["Month"][i]!="04":
        #print(data["Month"][i])
        data.drop(i,inplace=True)
print(data)
x=data["Day"]
y=data["NO2(GT)"]
plt.scatter(x,y)
plt.show()
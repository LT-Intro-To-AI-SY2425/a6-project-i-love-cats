import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("AirQualityUCI.csv", sep=";")
print(data)
x = data["Date"]
y = data["NO2(GT)"]
years=[]
months=[]
days2004=[]
days2005=[]
xSplit=[]
Data2004=[]
Data2005=[]
for i in range(len(y)):
    xSplit.append(x[i].split("/"))
for i in range(len(xSplit)):
    #print(data["Time"][i],ySplit[i][1])
    if data["Time"][i]=="04.00.00" and int(xSplit[i][1])==3 and int(xSplit[i][2])==2004:
        Data2004.append(y[i])
        days2004.append(int(xSplit[i][0]))
    if data["Time"][i]=="04.00.00" and int(xSplit[i][1])==3 and int(xSplit[i][2])==2005:
        Data2004.append(y[i])
        days2004.append(int(xSplit[i][0]))
print(Data2004)
print(days2004)
fig,graph = plt.subplots(2)
graph[0].scatter(Data2004,days2004)
graph[0].set_xlabel("Nitrogen Dioxide concentration (ppm)")
graph[0].set_ylabel("Day of Month")
graph[1].scatter(Data2005,days2005)
graph[1].set_xlabel("Nitrogen Dioxide concentration (ppm)")
graph[1].set_ylabel("Day of Month")

plt.tight_layout()
plt.show()





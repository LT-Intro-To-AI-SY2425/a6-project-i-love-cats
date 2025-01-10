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
days=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
xSplit=[]
NO2=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
colors=["c",'g','b','r','m','y']
for i in range(len(y)):
    xSplit.append(x[i].split("/"))
fig, graph = plt.subplots(4)

for m in range(1,13):
    for i in range(len(xSplit)):
        #print(data["Time"][i],ySplit[i][1])
        if data["Time"][i]=="04.00.00" and int(xSplit[i][1])==m and data["NO2(GT)"][i]!=-200:
            NO2[m].append(y[i])
            days[m].append(int(xSplit[i][0]))
    if m==12:
        graph[0].scatter(days[m],NO2[m],c=colors[m-12])
        
    if m<3:
        graph[0].scatter(days[m],NO2[m],c=colors[m])
    if 2<m<6:
        graph[1].scatter(days[m],NO2[m],c=colors[m-3])
    if 5<m<9:
        graph[2].scatter(days[m],NO2[m],c=colors[m-6])
    if 8<m<12:
        graph[3].scatter(days[m],NO2[m],c=colors[m-9])
    for i in range(4):
        graph[i].set_xlabel("Day")
        graph[i].set_ylabel("NO2(ppm)")
#print(days)
plt.show()





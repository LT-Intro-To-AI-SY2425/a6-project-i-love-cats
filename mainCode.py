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
days=[[]]
xSplit=[]
Data=[[]]
colors=["r",'g','b','c','m','y']
for i in range(len(y)):
    xSplit.append(x[i].split("/"))
fig, graph = plt.subplots(4)

for m in range(12):
    for i in range(len(xSplit)):
        #print(data["Time"][i],ySplit[i][1])
        if data["Time"][i]=="04.00.00" and int(xSplit[i][1])==m and int(xSplit[i][2])==2005:
            Data[m].append(y[i])
            days[m].append(int(xSplit[i][0]))
    if m>11:
        graph[0].scatter(days[m],Data[m],label="Winter",c=colors[m-12])
    if 0<m<3:
        graph[0].scatter(days[m],Data[m],label="Winter",c=colors[m+1])
    if 3<m<6:
        graph[1].scatter(days[m],Data[m],label="Spring",c=colors[m-3])
    if 6<m<8:
        graph[2].scatter(days[m],Data[m],label='Summer',c=colors[m-6])
    if 8<m<12:
        graph[3].scatter(days[m],Data[m],label='Fall',c=colors[m-8])
    for i in range(4):
        graph[i].set_xlabel("Day of month")
        graph[i].set_ylabel("Concentration of NO2(ppm)")
plt.show()




